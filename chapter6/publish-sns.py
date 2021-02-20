sns = boto3.resource('sns')
topic = sns.Topic('{トピック名のARN表記}')
topic.publish(Message='{トピックに送りたいメッセージ。ここではSQSに作ったキュー名}')