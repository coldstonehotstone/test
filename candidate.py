import yfinance as yf
import numpy as np
import time


# skip bio/drug related, spac
# only focus basic change not just news
ignore_list = ['ACIU', 'AGEN', 'AGMH', 'ALDX', 'ALT','AMYT', 'APTO', 'ATNX', 'AUTL','AVAL', 'AVNS',
        'BTX', 'CAI', 'CCXI', 'CELC', 'CERC', 'CLDR', 'CNST', 'CRIS', 'CUE', 
        'DGICB', 'DISCB', 'ELLO', 'EXFO', 'FREQ', 'GERN', 'GRUB', 'HGEN', 'IMMP', 'IPHA', 
        'JFIN', 'JFU', 'LBTYB', 'LSXMB', 'LTRPB', 'NGM', 'NMG', 'NMRD', 'PRQR','PRTC', 'PRVB', 'QTS',
        'RAPT', 'RDIB', 'SFTW', 'SYKE', 'TH', 'VRNA', 'XYF', 'YRD']


start_date = '2021-1-1'
end_date = '2022-1-1'
tickerData = yf.Ticker('GEO')
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
print (tickerDf)
print (len(tickerDf))
if len(tickerDf) < 5 * 13:
    print("less than 5 * 13")

def CheckVolume(tickerDf):
    #print(i, time.time() - time_start)
    #print("--------- " , ticker_list[i])
    #print(tickerDf.iloc[0]['Volume'])
    N = len(tickerDf)
    for j in range(N-5, N):
        sum_vol = np.sum(tickerDf.iloc[j-25:j]['Volume'])
        if tickerDf.iloc[j]['Volume'] > sum_vol: 
            return True
    return False

def IsNineWeeklyBuy(tickerDf):
    N = len(tickerDf)
    for i in range(9):
        if np.sum(tickerDf.iloc[N-(i+1)*5: N - i*5]['Close']) > np.sum(tickerDf.iloc[N-(i+5)*5:N-(i+4)*5]['Close']):
            return False
    return True

def IsNineDailyBuy(tickerDf):
    N = len(tickerDf)
    if N < 5 * 13:
        return False
    for i in range(9):
        if tickerDf.iloc[N-i-1]['Close'] > tickerDf.iloc[N-i-4-1]['Close']:
            #print(N-i, N-i-4, tickerDf.iloc[N-i]['Close'], tickerDf.iloc[N-i-4]['Close'])
            return False
    return True

def CheckNine(tickerDf):
    if IsNineDailyBuy(tickerDf):
        if IsNineWeeklyBuy(tickerDf):
            return True 
    return False 


time_start = time.time()
with open("nasdaq_screener_filtered.txt", "r") as f:
  ticker_list = f.read().splitlines() 
  #print(ticker_list )
  ticker_num = len(ticker_list )
  for i in range(0, ticker_num):
    if i % 500 == 0:
        print(i, time.time() - time_start)
    if ticker_list[i] in ignore_list:
        continue
    tickerData = yf.Ticker(ticker_list[i])
    tickerDf = tickerData.history(period='1w', start=start_date, end=end_date)
    if CheckVolume(tickerDf):
        print("From Volume ", time.time() - time_start, "\t", i, "/", ticker_num , ": ", ticker_list[i])
    
    if CheckNine(tickerDf):
        print("From Nine", time.time() - time_start, "\t", i, "/", ticker_num , ": ", ticker_list[i])

# good candidate will be  large volume + high turnover rate + company basic changes!!
# 6/13, find GEO

