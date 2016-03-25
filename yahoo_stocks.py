import csv
import os
from yahoo_finance import Share

curr_dir = os.path.dirname(os.path.realpath(__file__))

def read_SP_500():
    with open(os.path.join(curr_dir, 'sp500.csv'), 'rb') as f:
        reader = csv.reader(f)
        return list(reader)[0]

sp500 = read_SP_500()

for ticker in sp500:
    print ticker + ": " + Share(ticker).get_price()
