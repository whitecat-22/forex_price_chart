# forex_price_chart

### 為替情報(USD/JPY)を翌朝6:00(JST)にTwitterへ投稿する

◆使用技術：

- [Lambda](https://aws.amazon.com/jp/lambda/?nc2=h_ql_prod_fs_lbd) : Runtime = [Python](https://www.python.org/) 3.8 / [ServerlessFramework](https://app.serverless.com/)
- [EventBridge](https://aws.amazon.com/jp/eventbridge/?nc2=h_ql_prod_serv_eb) : cron(0 21 ? * MON-FRI *)
- [CloudWatchLogs](https://aws.amazon.com/jp/cloudwatch/?nc2=h_ql_prod_mg_cw)

※twitterへの投稿には、[twitter API](https://developer.twitter.com/en/docs/twitter-api) および、[tweepy](https://www.tweepy.org/)を利用しています。

　

![https://github.com/whitecat-22/forex_price_chart/blob/main/2021-06-10.PNG](https://github.com/whitecat-22/forex_price_chart/blob/main/2021-06-10.PNG)

　

- twitterへの投稿結果：

![https://github.com/whitecat-22/forex_price_chart/blob/main/twitter_20210610.PNG](https://github.com/whitecat-22/forex_price_chart/blob/main/twitter_20210610.PNG)
