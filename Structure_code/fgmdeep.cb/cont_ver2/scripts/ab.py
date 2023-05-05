import os
import csv
import pandas as pd
import numpy as np

path = os.getcwd()
path = (os.path.dirname(path)+'/')
with open(path+'displacment') as f:
  lines = f.readlines()
  header = (lines[0])[2:-1].split(",")
  data = []
  df = pd.DataFrame(data, columns=header)
  df.to_csv(path+'displacementc.csv', index=False)
  
with open(path+'stressf') as f:
  lines = f.readlines()
  header = (lines[0])[1:-1].split(",")
  data = []
  df = pd.DataFrame(data, columns=header)
  df.to_csv(path+'stressc.csv', index=False)
