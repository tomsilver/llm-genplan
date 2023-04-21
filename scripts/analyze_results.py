"""Create a table summarizing results saved to a directory."""

import argparse
import glob
import pickle
from pathlib import Path
from typing import Any, Callable, Dict, Optional

import numpy as np
import pandas as pd

from llm_genplan.structs import TaskMetrics


def _main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", default="results", type=str)
    args = parser.parse_args()
    results = _load_results(args.results_dir)
    _create_summary_table(results)


def _load_results(
    results_dir: str,
    derived_cols: Optional[Dict[str, Callable[[TaskMetrics], Any]]] = None,
) -> pd.DataFrame:
    all_data = []
    git_commit_hashes = set()
    for filepath in sorted(glob.glob(f"{results_dir}/*")):
        with open(filepath, "rb") as f:
            outdata = pickle.load(f)
        git_commit_hashes.add(outdata["git_commit_hash"])
        results = outdata["results"].copy()
        env, seed, experiment_id = Path(filepath).stem.split("__")
        for task_id, task_results in results.items():
            datum = {
                "env": env,
                "seed": seed,
                "experiment_id": experiment_id,
                "task_id": task_id,
                **task_results,
            }
            if derived_cols is not None:
                for col, derive_fn in derived_cols.items():
                    datum[col] = derive_fn(datum)
            all_data.append(datum)
    if not all_data:
        raise ValueError(f"No data found in {results_dir}/")
    # Group & aggregate data.
    pd.set_option("display.max_rows", 999999)
    df = pd.DataFrame(all_data)
    print(f"Git commit hashes seen in {results_dir}/:")
    for commit_hash in git_commit_hashes:
        print(commit_hash)
    # Uncomment the next line to print out ALL the raw data.
    # print(df)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    return df


def _create_summary_table(
    raw_results: pd.DataFrame, save_summary: bool = True
) -> pd.DataFrame:
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
    print(f"\nTOTAL RESULTS: {df.shape[0]}")
    if save_summary:
        summary_nested.to_csv("results_summary.csv")
        print("\n\nWrote out table to results_summary.csv")
    return means.reset_index()


if __name__ == "__main__":
    _main()
