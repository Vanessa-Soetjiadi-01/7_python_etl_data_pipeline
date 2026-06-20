import matplotlib.pyplot as plt

def report_data(ticker_data):
  fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12,10))
  axes = axes.flatten()

  for i, (ticker, df) in enumerate(ticker_data.items()):
    ax = axes[i]
    ax.plot(df.index, df["Close"], label="Close")
    ax.plot(df.index, df["7_MA"], label="7-day MA")
    ax.plot(df.index, df["30_MA"], label="30-day MA")
    ax.set_title(ticker)
    ax.legend()
  
  plt.tight_layout() 
  fig.savefig("output/chart.png")