sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='{作ったキュー名}')
messages = queue.receive_messages(MessageAttributeNames=['All'], MaxNumberOfMessages = 10)
for m in messages:
    xxxx = m.body # メッセージ本文
    yyyy = m.message_attributes.get('{作った属性名}').get('StringValue') #キュー内に自由につけた属性が読み取れる