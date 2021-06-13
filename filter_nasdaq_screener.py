import numpy as np

import csv

# filter by year < 2020
# filter by market cap  < 100B

with open('nasdaq_screener_filtered.txt', 'w') as fout:
  with open('nasdaq_screener_1623605545361.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(len(data))
    for i in range(1, len(data)):
      if float(data[i][5]) > 100 * 1e9:
          continue
      if len(data[i][7]) != 0 and  int(data[i][7]) >= 2020:
          continue
      print(data[i])
      fout.write(data[i][0])
      fout.write("\n")

