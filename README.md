# forex_price_chart

### 為替情報(USD/JPY)を翌朝6:00(JST)にTwitterへ投稿する

- [Lambda](https://aws.amazon.com/jp/lambda/?nc2=h_ql_prod_fs_lbd) : Runtime = [Python](https://www.python.org/) 3.8 / [ServerlessFramework](https://app.serverless.com/)
- [EventBridge](https://aws.amazon.com/jp/eventbridge/?nc2=h_ql_prod_serv_eb) : cron(0 21 ? * MON-FRI *)
- CloudWatchLogs

　

![https://github.com/whitecat-22/forex_price_chart/blob/main/2021-06-10.PNG](https://github.com/whitecat-22/forex_price_chart/blob/main/2021-06-10.PNG)

　

- twitterへの投稿結果：

![https://github.com/whitecat-22/forex_price_chart/blob/main/twitter_20210610.PNG](https://github.com/whitecat-22/forex_price_chart/blob/main/twitter_20210610.PNG)
