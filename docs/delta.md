# Delta Lake

O **Delta Lake** é um formato de tabela aberto que armazena os dados em Parquet e mantém um log de transações (`_delta_log`) em JSON. Cada operação gera uma nova **versão** da tabela.

## Configuração no Spark
```python
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

builder = (
    SparkSession.builder.master("local[*]")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog")
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()
```

## DDL
```sql
CREATE TABLE pedidos (...) USING delta LOCATION 'data/delta/pedidos';
```

## INSERT
Adiciona o pedido 106.
```sql
INSERT INTO pedidos VALUES
(106, 2, 'Webcam', 1, 350.00, DATE'2026-09-10', 'PENDENTE');
```
Um novo arquivo Parquet é escrito e uma entrada `WRITE` é adicionada ao `_delta_log`.

## UPDATE
Pedidos pendentes do cliente 1 passam a PAGO (pedido 104).
```sql
UPDATE pedidos SET status = 'PAGO'
WHERE id_cliente = 1 AND status = 'PENDENTE';
```
O Delta reescreve os arquivos afetados e marca os antigos como removidos no log.

## DELETE
Remove o pedido cancelado (105).
```sql
DELETE FROM pedidos WHERE status = 'CANCELADO';
```

## Histórico (time travel)
```sql
DESCRIBE HISTORY pedidos;
SELECT * FROM pedidos VERSION AS OF 0;
```

Notebook completo: `src/delta/delta_lake.ipynb`.
