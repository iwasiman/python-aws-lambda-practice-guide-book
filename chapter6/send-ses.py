client = boto3.client('ses', region_name='{リージョン名}')
client.send_email(
    Source={送信元メアド},
    ReplyToAddress=[{配列でリプライ先}],
    Destination={'ToAddress': [{配列で送信先メアド}]},
    Message={辞書形式でタイトルやメール本文を指定。それぞれごとにキャラセットも指定}
)