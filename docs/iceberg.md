# Apache Iceberg

O **Apache Iceberg** é um formato de tabela aberto criado pela Netflix. Ele organiza a tabela em **metadados → manifest lists → manifests → arquivos de dados**, e cada alteração gera um novo **snapshot**.

## Configuração no Spark
Usa o pacote `org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1` e um catálogo do tipo `hadoop` chamado `local`:
```python
spark = (
    SparkSession.builder.master("local[*]")
    .config("spark.jars.packages",
            "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1")
    .config("spark.sql.extensions",
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", "data/warehouse")
    .getOrCreate()
)
```

## DDL
```sql
CREATE NAMESPACE IF NOT EXISTS local.loja;
CREATE TABLE local.loja.pedidos (...) USING iceberg;
```

## INSERT
```sql
INSERT INTO local.loja.pedidos VALUES
(106, 2, 'Webcam', 1, 350.00, DATE'2026-09-10', 'PENDENTE');
```
Gera um snapshot com operação `append`.

## UPDATE
```sql
UPDATE local.loja.pedidos SET status = 'PAGO'
WHERE id_cliente = 1 AND status = 'PENDENTE';
```
Gera um snapshot `overwrite` (copy-on-write por padrão).

## DELETE
```sql
DELETE FROM local.loja.pedidos WHERE status = 'CANCELADO';
```

## Snapshots (time travel)
```sql
SELECT snapshot_id, operation FROM local.loja.pedidos.snapshots;
SELECT * FROM local.loja.pedidos VERSION AS OF <snapshot_id>;
```

## Delta x Iceberg
| | Delta Lake | Apache Iceberg |
|---|---|---|
| Metadados | `_delta_log` (JSON) | metadata.json + manifests (Avro) |
| Versões | version | snapshot |
| Integração Spark | pacote pip `delta-spark` | JAR via `spark.jars.packages` |

Notebook completo: `src/iceberg/apache_iceberg.ipynb`.
