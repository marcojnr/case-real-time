from pyspark.sql.functions import *
from pyspark.sql.types import *

connectionString = "<sua_connection_string_event_hub>"
ehConf = {
  "eventhubs.connectionString" : connectionString
}

# Lê stream do Event Hub
df_raw = (spark.readStream
          .format("eventhubs")
          .options(**ehConf)
          .load())

# Corpo do evento vem em df_raw.body binário → converter para string
df_json = df_raw.withColumn("body", col("body").cast("string"))

# Definir schema simples
schema = StructType([
    StructField("transaction_no", IntegerType()),
    StructField("date", StringType()),
    StructField("product_no", IntegerType()),
    StructField("product_name", StringType()),
    StructField("price", DoubleType()),
    StructField("quantity", IntegerType()),
    StructField("customer_no", IntegerType()),
    StructField("country", StringType()),
    StructField("event_time", StringType())
])

df_parsed = df_json.select(
    from_json(col("body"), schema).alias("data")
).select("data.*")

# Escreve na camada bronze
(df_parsed.writeStream
 .format("delta")
 .option("checkpointLocation", "/mnt/checkpoints/pedidos_bronze")
 .option("path", "/mnt/delta/pedidos_bronze")
 .outputMode("append")
 .start())
