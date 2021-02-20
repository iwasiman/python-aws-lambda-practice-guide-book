sqs = boto3.resource('sqs');
queue = sqs.get_query_by_name(QueueName='{作ったキュー名}')
queue.send_message(
    MessageBody={メッセージ本体。このサンプルでは宛先メアド},
    MessageAttributes={メッセージ属性。辞書型でデータ型と内容を好きなだけ...}
    )