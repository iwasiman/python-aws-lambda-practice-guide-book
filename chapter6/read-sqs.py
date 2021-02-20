sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='{作ったキュー名}')
n = queue.attributes['ApproximateNumberOfMessages'] # 貯まったキューの数