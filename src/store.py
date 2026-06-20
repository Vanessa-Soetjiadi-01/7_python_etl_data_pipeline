import sqlite3

def store_data(ticker_data):
  conn = sqlite3.connect("stock.db")
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
                ticker,
                date,
                open,
                high,
                low,
                close,
                volume,
                ma_7,
                ma_30,
                daily_change
                )
  """)

  for ticker, df in ticker_data.items():
    for idx, row in df.iterrows():
      cursor.execute("INSERT OR IGNORE INTO stocks VALUES (?,?,?,?,?,?,?,?,?,?)", (ticker, str(idx), row["Open"], row["High"], row["Low"], row["Close"], row["Volume"], row["7_MA"], row["30_MA"], row["daily_change"]))

  conn.commit()
  conn.close()