import argparse
import glob
import json
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-f', nargs=1)
parser.add_argument('-d', nargs=1)
parser.add_argument('-t', nargs=1)
args = parser.parse_args()

with open('rules') as rules_file:
  rules = json.load(rules_file)

path = args.d

if len(args.f) > 0:
  path = os.path.join(path, args.f)

for 