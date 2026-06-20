from src.fetch import fetch_data
from src.transform import transform_data
from src.store import store_data
from src.report import report_data

def run_all():
  ticker_data = transform_data(fetch_data())

  store_data(ticker_data)
  report_data(ticker_data)

if __name__ == "__main__":
 run_all()