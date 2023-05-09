"""Create a table summarizing results saved to a directory."""

import argparse
import glob
import pickle
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from llm_genplan.genplan import GENPLAN_ERROR_TYPES


def _main() -> None:
    matplotlib.rcParams.update({"font.size": 16})
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", default="results", type=str)
    args = parser.parse_args()
    gen_plan_results, evaluation_results = load_results(args.results_dir)
    _create_success_table(evaluation_results)
    _create_interactive_debug_plot(gen_plan_results)
    _create_genplan_error_table(gen_plan_results)
    _create_num_training_tasks_plot(gen_plan_results)


def load_results(
    results_dir: str,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load the raw results into dataframes."""
    all_gen_plan_data = []
    all_evaluation_data = []
    git_commit_hashes = set()
    for filepath in sorted(glob.glob(f"{results_dir}/*")):
        with open(filepath, "rb") as f:
            outdata = pickle.load(f)
        env, seed, experiment_id = Path(filepath).stem.split("__")
        if env.endswith("-ablated"):
            env = env[: -len("-ablated")]
        git_commit_hashes.add(outdata["git_commit_hash"])
        # Evaluation results.
        successes: List[float] = []  # include success rate in genplan dataframe
        for task_id, task_results in outdata["eval_metrics"].items():
            eval_datum = {
                "env": env,
                "seed": seed,
                "experiment_id": experiment_id,
                "task_id": task_id,
                **task_results,
            }
            successes.append(task_results["success"])
            all_evaluation_data.append(eval_datum)
        # Gen plan results.
        gen_plan_metrics = outdata["gen_plan_metrics"].copy()
        genplan_datum = {
            "env": env,
            "seed": seed,
            "experiment_id": experiment_id,
            "success_rate": np.mean(successes),
            **gen_plan_metrics,
        }
        all_gen_plan_data.append(genplan_datum)
    if not all_evaluation_data:
        raise ValueError(f"No data found in {results_dir}/")
    # Group & aggregate data.
    pd.set_option("display.max_rows", 999999)
    genplan_df = pd.DataFrame(all_gen_plan_data)
    eval_df = pd.DataFrame(all_evaluation_data)
    print(f"Git commit hashes seen in {results_dir}/:")
    for commit_hash in git_commit_hashes:
        print(commit_hash)
    genplan_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    eval_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    return genplan_df, eval_df


def _create_success_table(raw_results: pd.DataFrame, save_summary: bool = True) -> None:
    # Remove the non-numeric columns that we don't need anymore.
    df = raw_results.drop(columns=["task_id"])
    # Group by env, seed, and experiment ID.
    grouped = df.groupby(["env", "seed", "experiment_id"])
    # Average over eval tasks.
    eval_means = grouped.mean().reset_index()
    # Get statistics over seed.
    grouped = eval_means.groupby(["env", "experiment_id"])
    means = grouped.mean()
    stds = grouped.std(ddof=0)
    sizes = grouped.size().to_frame()
    summary = means.copy()
    # Add standard deviations to the printout.
    for col in means:
        for row in means[col].keys():
            mean = means.loc[row][col]
            std = stds.loc[row][col]
            summary.loc[row, col] = f"{mean:.2f} ({std:.2f})"
    summary["num_seeds"] = sizes
    pd.set_option("expand_frame_repr", False)
    print("\n\nAGGREGATED DATA OVER EVAL TASKS AND SEEDS:")
    summary = summary.reset_index()
    envs = summary.env.unique()
    metrics = ["success", "num_seeds"]
    # env -> experiment_id X metric -> value
    reshaped_data: Dict = {env: {} for env in envs}
    for _, row in summary.iterrows():
        for metric in metrics:
            reshaped_data[row.env][(row.experiment_id, metric)] = row[metric]
    summary_nested = pd.DataFrame(reshaped_data).transpose()
    print(summary_nested)
    # Report the total number of results.
    print(f"\nTOTAL RESULTS: {raw_results.shape[0]}")
    if save_summary:
        summary_nested.to_csv("results_summary.csv")
        print("\n\nWrote out table to results_summary.csv")


def _create_interactive_debug_plot(df: pd.DataFrame):
    # Make plot for main approach only.
    df = df.loc[df["experiment_id"] == "chatgpt4"]
    max_x = df["num_interactive_debugs"].max()
    x_to_ys: Dict[int, List[float]] = {x: [] for x in range(max_x + 1)}
    for _, row in df.iterrows():
        for x in range(max_x + 1):
            if x < row.num_interactive_debugs:
                y = 0.0
            else:
                y = row.success_rate
            x_to_ys[x].append(y)
    xs = sorted(x_to_ys)
    ys = np.array([np.mean(x_to_ys[x]) for x in xs])
    errs = [np.std(x_to_ys[x], ddof=1) / np.sqrt(np.size(x_to_ys[x])) for x in xs]
    outfile = "num_automated_debug.png"
    with plt.style.context("bmh"):
        plt.figure()
        plt.plot(xs, ys, marker="o")
        plt.fill_between(xs, ys - errs, ys + errs, alpha=0.25)
        plt.ylim((-0.1, 1.1))
        plt.xticks(xs)
        plt.xlabel("# Debug Steps")
        plt.ylabel("% Eval Tasks Solved")
        plt.title("Automated Debugging")
        plt.tight_layout()
        plt.savefig(outfile, dpi=500)
        print(f"Wrote out to {outfile}.")


def _create_genplan_error_table(
    raw_results: pd.DataFrame, save_summary: bool = True
) -> None:
    group_dfs: List[pd.DataFrame] = []
    for group_name in ["All", "Success", "Fail"]:
        mask = raw_results["experiment_id"] == "chatgpt4"
        if group_name == "All":
            filtered_results = raw_results
        elif group_name == "Success":
            mask &= raw_results["success_rate"] >= (1.0 - 1e-6)
        else:
            assert group_name == "Fail"
            mask &= raw_results["success_rate"] < (1.0 - 1e-6)
        filtered_results = raw_results.loc[mask]
        df = filtered_results[GENPLAN_ERROR_TYPES]
        tot_errs_by_type = df.sum()
        tot_errs = tot_errs_by_type.sum()
        summary = tot_errs_by_type / tot_errs
        group_df = summary.to_frame().rename(columns={0: group_name})
        group_dfs.append(group_df)
    summary_df = pd.concat(group_dfs, axis=1)
    print(summary_df)
    if save_summary:
        summary_df.to_csv("error_types_summary.csv")
        print("\n\nWrote out table to error_types_summary.csv")


def _create_num_training_tasks_plot(df: pd.DataFrame):
    # Make plot for main approach only.
    df = df.loc[df["experiment_id"] == "chatgpt4"]
    min_x = df["num_influential_training_tasks"].min()
    max_x = df["num_influential_training_tasks"].max()
    x_to_count = {x: 0 for x in range(min_x, max_x + 1)}
    total = 0.0
    for _, row in df.iterrows():
        # Successes only.
        if row.success_rate < 1.0 - 1e-6:
            continue
        x_to_count[row.num_influential_training_tasks] += 1
        total += 1.0
    xs = sorted(x_to_count)
    heights = [x_to_count[x] / total for x in xs]
    outfile = "num_necessary_training_tasks.png"
    with plt.style.context("bmh"):
        plt.figure()
        plt.bar(xs, heights)
        plt.xticks(xs)
        plt.xlabel("# Used Training Tasks")
        plt.ylabel("Fraction")
        plt.title("Training Tasks Used for Successes")
        plt.tight_layout()
        plt.savefig(outfile, dpi=500)
        print(f"Wrote out to {outfile}.")


if __name__ == "__main__":
    _main()
