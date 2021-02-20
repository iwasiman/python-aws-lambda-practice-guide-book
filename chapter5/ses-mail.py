client = boto3.client('ses', region_name='{リージョン名}')
client.send_email({名前付き引数で諸々})