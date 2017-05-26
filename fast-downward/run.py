#!/usr/bin/env python

import sys
import os
import subprocess
import re

DIR = os.path.dirname(os.path.abspath(__file__))
PLANNER = os.path.join(DIR, "fast-downward.py")
DOMAIN_FILE = sys.argv[1]
PROBLEM_FILE = sys.argv[2]
SEARCH_METHOD = sys.argv[3]


class Output:
    summary = ""
    full_output = ""
    plan_cost = -99999999999
    hashes = []
    
    def run_plan_script(self,domain_file, problem_file, search_method):
        sys.stdout.flush()
        try:
            out =  subprocess.check_output([sys.executable, PLANNER, domain_file, problem_file, "--search", search_method], stderr=subprocess.STDOUT)
        except Exception, e:
            out = str(e.output)
        return out
    
    def call(self,domain_file, problem_file, search_method):
        sys.stdout.flush()
        subprocess.call([sys.executable, PLANNER, domain_file, problem_file, "--search", search_method], stderr=subprocess.STDOUT)

            
    def cleanup(self):
        subprocess.check_call([sys.executable, PLANNER, "--cleanup"])

    def run_and_save_summary(self, domain_file, problem_file, search_method):
        self.full_output = self.run_plan_script(domain_file, problem_file, search_method)
        self.summary = re.findall(r"(Total time: [0-9]+.[0-9]+s|Peak memory: [\d]+ +[A-Z]{2}|Plan cost: [\d]+|Search stopped without finding a solution.|Usage error occurred.|Time limit reached.)",self.full_output)
        tmp = ''.join(self.summary)
        self.plan_cost = int(re.findall(r"(?<=Plan cost: )[\d]+", tmp)[0])
        
    def print_summary(self):
        print self.summary
        print self.full_output
        print "PLAN COST",self.plan_cost 
        
    def recalculate_hashes(self, domain_file, problem_file, search_method):
        #self.full_output = self.run_plan_script(domain_file, problem_file, search_method)
        #self.hashes  = re.findall(r"(\d+)[ \t\r\f\v](\d+)",self.full_output)
        
        with open("output.out","r") as output:
            #print output
           #string = output.read()
          # hashes_str = re.findall(r"(\d+)[ \t\r\f\v](\d+)",string)
           #self.hashes =[map(int,  i) for i in hashes_str]
           #size = len(self.hashes) 
           #for i in range(size):
            #       self.hashes[i][1] = self.plan_cost - self.hashes[i][1]
           #print self.plan_cost, self.hashes, size+1
            with open("stateDB.out","w") as new:
                for line in output.readlines():
                    [h,g] = line.split(" ")
                    g = str( self.plan_cost - int(g) )
                    new.write(h + " " + g + "\n" )
            #with open("stateDB.out","r") as output:
                   # print output
            
out = Output()   
     
#out.call(DOMAIN_FILE, PROBLEM_FILE, SEARCH_METHOD)
out.run_and_save_summary(DOMAIN_FILE, PROBLEM_FILE, SEARCH_METHOD)
out.print_summary()
#out.recalculate_hashes(DOMAIN_FILE, PROBLEM_FILE, SEARCH_METHOD)

