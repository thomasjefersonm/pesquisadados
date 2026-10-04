# Apache Spark (PySpark)

O **Apache Spark** é um motor de processamento distribuído de dados em memória. O **PySpark** é a API Python do Spark.

## Conceitos principais
- **SparkSession**: ponto de entrada da aplicação.
- **DataFrame**: tabela distribuída com colunas nomeadas.
- **Spark SQL**: permite consultar DataFrames e tabelas com SQL.
- **Transformações** (lazy) e **Ações** (executam o processamento).
- **Catálogo**: onde as tabelas são registradas.

## Criando a sessão
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("exemplo").master("local[*]").getOrCreate()
```

## Lendo os dados do projeto
```python
pedidos = spark.read.csv("data/pedidos.csv", header=True, inferSchema=True)
pedidos.printSchema()
pedidos.filter("status = 'PAGO'").show()
```

## Por que Delta e Iceberg?
Arquivos Parquet/CSV comuns não suportam `UPDATE` e `DELETE` com transações. Os formatos de tabela **Delta Lake** e **Apache Iceberg** adicionam uma camada de metadados que traz transações **ACID**, histórico de versões (*time travel*) e evolução de schema ao Spark.

No projeto, as sessões configuradas estão em `pesquisadados/main.py` (`spark_delta()` e `spark_iceberg()`).
