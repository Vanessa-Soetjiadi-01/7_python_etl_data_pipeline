import yfinance as yf

TICKERS = ["CBA.AX", "BHP.AX", "TLS.AX", "WOW.AX", "COL.AX", "WES.AX"]

def fetch_data():
  ticker_dict = {}
  for ticker in TICKERS:
    ticker_dict[ticker] = yf.download(ticker, period="1y")
  return ticker_dict