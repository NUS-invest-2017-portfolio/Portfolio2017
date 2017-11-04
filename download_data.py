import pandas
import datetime
import pandas_datareader.data as web
import quandl

def download_data_price(tickers, start, end):
    data = web.DataReader(tickers, "yahoo", start, end)
    return data["Adj Close"]

def download_data_market_cap(tickers, start, end):
    quandl.ApiConfig.api_key = "YyFvB7HZAMdDsuEK_Mdm"
    data = quandl.get_table("ZACKS/MKTV", paginate = True, ticker = tickers,\
                          per_end_date = {"gte":start, "lte":end},\
                          qopts = {"columns":["ticker", "per_end_date", "mkt_val"]})
    return data
    
    
tickers = ["DD", "GS", "JNJ", "JPM",\
                   "VZ", "IBM", "V", "AXP",\
                   "HD", "DIS", "XOM", "KO",\
                    "PFE", "CSCO", "WMT", "PG",\
                    "CAT", "TRV", "UTX", "MMM",\
                   "MCD", "BA", "NKE", "UNH",\
                   "GE", "AAPL", "CVX", "MRK",\
                   "MSFT", "INTC"]
start = datetime.datetime(2017, 8, 1)
end = datetime.datetime(2017, 8, 3)

adj_close = download_data_price(tickers, start, end)
adj_close.to_csv("Adj Close.csv")


start = "2015-01-01"
end = "2016-12-31"
market_cap = download_data_market_cap(tickers, start, end)
market_cap.to_csv("Market Cap.csv")
