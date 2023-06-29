from clickhouse_driver import Client

host = "b295svw027.europe-west4.gcp.clickhouse.cloud"
user = "default"
password = "8Sp5vsMldZ_tx"
database = "improvado"

client = Client(host,
                user=user,
                password=password,
                secure=True,
                verify=False,
                database=database)