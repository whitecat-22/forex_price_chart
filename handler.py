try:
    #from notifiers import unzip_requirements
    import unzip_requirements
except ImportError:
    print('Import Error - unzip_requirements')
    pass
except Exception as e:
    print(e)
    pass

import csv
import datetime
import os
from os.path import join, dirname
import pandas as pd
import mplfinance as mpf
import pandas_datareader as data
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta

from notifiers import twitter

import json
import logging

import yfinance as yf
yf.pdr_override()

# settins for logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Load env variants
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
currency_code = os.environ.get("CURRENCY_CODE")

# Get today's date for getting the currency price and csv&image filename
today = datetime.date.today()

# tmp directory is present by default on Cloud Functions, so guard it
if not os.path.isdir('/tmp'):
    os.mkdir('/tmp')

FILENAME = '%s.csv' % str(today)


def generate_currency_chart_image():
    """
    Generate a six-month currency chart image with mplfinance
    """
    dataframe = pd.read_csv(
        f"/tmp/{str(today)}.csv", index_col=0, parse_dates=True)
    # The return value `Date` from yahoofinance is sorted by asc, so change it to desc for plot
    dataframe = dataframe.sort_values('Date')
    mpf.plot(dataframe, type='candle', figratio=(12, 4),
             volume=False, mav=(5, 25), style='checkers',
             savefig=f"/tmp/{str(today)}.png")


def generate_csv_with_datareader():
    """
    Generate a csv file of OHLCV with date with yahoofinance API
    """
    # 価格推移の開始日を指定(6ヶ月を指定)
    start_date = today - relativedelta(months=6)
    end_date = today + relativedelta(days=1)
    # yahoofinanceのライブラリ経由でAPIを叩く(currency_codeは環境変数で通貨ペアコードを指定)
    df = data.DataReader(currency_code, 'yahoo', start=start_date, end=end_date)
    df = df[['High', 'Low', 'Open', 'Close']]
    df.tail()

    # APIで取得したデータを一旦CSVファイルにする
    df = df.sort_values(by='Date', ascending=False)
    df.to_csv(f"/tmp/{str(today)}.csv")
    # print(df)

def lambdahandler(event, context):
    """
    lambda_handler
    """
    logging.info(json.dumps(event))

    print('event: {}'.format(event))
    print('context: {}'.format(context))
    """
    The main function that will be executed when this Python file is executed
    """
    generate_csv_with_datareader()
    generate_currency_chart_image()

    #if "challenge" in event["body"]:
    #    return event["body"]["challenge"]

    with open(f"/tmp/{str(today)}.csv", 'r', encoding="utf-8") as file:
        # Skip header row
        reader = csv.reader(file)
        header = next(reader)
        for i, row in enumerate(csv.DictReader(file, header)):
            # Send only the most recent data to Slack notification
            if i == 0:
                twitter.Twitter(today, row).post()

    return {
        'statusCode': 200,
        'body': 'ok'
    }

if __name__ == "__main__":
    print(lambdahandler(event=None, context=None))
