import yfinance as yf
import numpy as np
import time


# skip bio/drug related, spac
# only focus basic change not just news
ignore_list = ['ACIU', 'AGEN', 'ALDX', 'AMYT', 'APTO', 'ATNX', 'AUTL','AVNS',
        'BTX', 'CCXI', 'CELC', 'CERC', 'CLDR', 'CNST', 'CRIS', 'CUE', 
        'DGICB', 'DISCB', 'ELLO', 'EXFO', 'FREQ', 'HGEN', 'IMMP', 'IPHA', 
        'JFIN', 'LBTYB', 'LSXMB', 'LTRPB', 'NGM', 'NMRD', 'PRQR','PRTC', 'PRVB', 'RDIB', 'SFTW', 'TH', 'VRNA', 'YRD']

with open("nasdaq_screener_filtered.txt", "r") as f:
  ticker_list = f.read().splitlines() 
  print(ticker_list )
  ticker_num = len(ticker_list )
  #time_start = time.time()
  for i in range(0, ticker_num):
    if ticker_list[i] in ignore_list:
        continue
    tickerData = yf.Ticker(ticker_list[i])
    tickerDf = tickerData.history(period='1d', start='2021-4-15', end='2021-6-13')
    #print(i, time.time() - time_start)
    #print("--------- " , ticker_list[i])
    #print(tickerDf.iloc[0]['Volume'])
    for j in range(31, len(tickerDf)):
        sum_vol = np.sum(tickerDf.iloc[j-31:j-1]['Volume'])
        if tickerDf.iloc[j]['Volume'] > sum_vol: 
#            print(" -----------  ", ticker_list[i], tickerDf.iloc[j].name)
            print(ticker_list[i], tickerDf.iloc[j].name)
    

# good candidate will be  large volume + high turnover rate + company basic changes!!
# 6/13, find GEO

