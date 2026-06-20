def transform_data(ticker_data):
  for ticker in ticker_data:
    ticker_data[ticker]["7_MA"]=ticker_data[ticker]["Close"].rolling(window=7).mean()
    ticker_data[ticker]["30_MA"]=ticker_data[ticker]["Close"].rolling(window=30).mean()
    ticker_data[ticker]["daily_change"]=ticker_data[ticker]["Close"].pct_change()
  return ticker_data