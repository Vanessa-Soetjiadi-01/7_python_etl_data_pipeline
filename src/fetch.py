import yfinance as yf

TICKERS = ["CBA.AX", "BHP.AX", "TLS.AX", "WOW.AX", "COL.AX", "WES.AX"] # hard coded

def fetch_data():
  ticker_dict = {}
  for ticker in TICKERS:
    data = yf.download(ticker, period="1y")
    data.columns = data.columns.droplevel(1)
    ticker_dict[ticker] = data
  return ticker_dict