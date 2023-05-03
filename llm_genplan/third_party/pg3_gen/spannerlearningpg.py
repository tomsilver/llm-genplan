#!/usr/bin/env python
import sys, random
import numpy as np
import os

#*****************#
# Functions declarations
#*****************#
def get_objects(num_spanners, num_nuts, num_locations, seed):
   str_objects="\n"

   # -- man
   str_objects=str_objects+"     bob - man\n"

   # -- spanner
   for i in range(1, num_spanners+1):
      str_objects=str_objects+" spanner"+str(i)
   str_objects=str_objects+" - spanner\n    "

   # -- nuts
   for i in range(1,num_nuts+1):
      str_objects=str_objects+" nut"+str(i)
   str_objects=str_objects+" - nut\n    "

   # -- locations
   for i in range(1,num_locations+1):
      str_objects=str_objects+" location"+str(i)
   str_objects=str_objects+" - location\n    "

   str_objects=str_objects+" shed gate - location\n    "

   return(str_objects)
   


#*****************#
def get_init(num_spanners, num_nuts, num_locations, seed):
   #np.random.seed(seed)
   #random.seed(seed)

   str_init="\n"
   str_init=str_init+"    (at bob shed)\n"

   for i in range(1,num_spanners+1):      
      str_init=str_init+"    (at spanner"+str(i)+" location"+ str(random.randint(1,num_locations))+")\n"
      str_init=str_init+"    (useable spanner"+str(i)+")\n"

   for i in range(1,num_nuts+1):
      str_init=str_init+"    (loose nut"+str(i)+")\n"	
      str_init=str_init+"    (at nut"+str(i)+" gate)\n"

   str_init=str_init+"    (link shed location1)\n"
   str_init=str_init+"    (link location"+str(num_locations)+" gate)\n"

   for i in range(1,num_locations):
      str_init=str_init+"    (link location"+str(i)+" location"+str(i+1)+")\n"
      
   return(str_init)

#*****************#
def get_goals(num_spanners, num_nuts, num_locations, seed):
   str_goal=""
   str_goal=str_goal+"\n  (and\n"

   for i in range(1,num_nuts+1):
      str_goal=str_goal+ "   (tightened nut"+str(i)+")\n"
            
   str_goal=str_goal+")"
   return(str_goal)
#*****************#

#*****************#
# MAIN
#*****************#
# Reading the command line arguments

if __name__ == '__main__':

   for seed in range(10):
      np.random.seed(seed)
      random.seed(seed)

      #Training problems:
      # Number of training problems: 5
      # Number of spanners: 3 - 5 
      # Number of nuts: 3 - 5
      # Number of locations: 3 - 5
      for prob_idx in range(10):
         num_spanners = np.random.randint(3, 6)
         num_nuts = np.random.randint(3, num_spanners+1)
         num_locations = np.random.randint(3, 6)

         name="prob" + str(prob_idx)

         problem_string = "(define (problem "+name+")" + "\n" + " (:domain spanner)" + "\n" + " (:objects "+ get_objects(num_spanners, num_nuts, num_locations, seed)+")" \
                           + "\n" + " (:init " + get_init(num_spanners, num_nuts, num_locations, seed)+")" + "\n" + " (:goal"+ get_goals(num_spanners, num_nuts, num_locations, seed)+"))"

         filename = "spannerlearning/seed{}/problem{}.pddl".format(seed, prob_idx)
         os.makedirs(os.path.dirname(filename), exist_ok=True)
         with open(filename, "w") as f:
               f.write(problem_string)


      #Test problems:
      # Number of test problems: 30
      # Number of spanners: 10 - 20
      # Number of nuts: 10 - 20
      # Number of locations 20 - 30
      for prob_idx in range(30):
         num_spanners = np.random.randint(10, 21)
         num_nuts = np.random.randint(10, num_spanners+1)
         num_locations = np.random.randint(20, 31)
         name="prob" + str(prob_idx)

         problem_string = "(define (problem "+name+")" + "\n" + " (:domain spanner)" + "\n" + " (:objects "+ get_objects(num_spanners, num_nuts, num_locations, seed)+")" \
                           + "\n" + " (:init " + get_init(num_spanners, num_nuts, num_locations, seed)+")" + "\n" + " (:goal"+ get_goals(num_spanners, num_nuts, num_locations, seed)+"))"

         filename = "spannerlearning_test/seed{}/problem{}.pddl".format(seed, prob_idx)
         os.makedirs(os.path.dirname(filename), exist_ok=True)
         with open(filename, "w") as f:
               f.write(problem_string)

