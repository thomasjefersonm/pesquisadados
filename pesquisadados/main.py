"""Funções para criar SparkSessions com Delta Lake e Apache Iceberg."""

from pathlib import Path

from pyspark.sql import SparkSession

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"
ICEBERG_PACOTE = "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1"


def spark_delta(app: str = "delta") -> SparkSession:
    """Cria uma SparkSession configurada para Delta Lake."""
    from delta import configure_spark_with_delta_pip

    builder = (
        SparkSession.builder.appName(app)
        .master("local[*]")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    return configure_spark_with_delta_pip(builder).getOrCreate()


def spark_iceberg(app: str = "iceberg") -> SparkSession:
    """Cria uma SparkSession com um catálogo Iceberg local chamado `local`."""
    return (
        SparkSession.builder.appName(app)
        .master("local[*]")
        .config("spark.jars.packages", ICEBERG_PACOTE)
        .config(
            "spark.sql.extensions",
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        )
        .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.local.type", "hadoop")
        .config("spark.sql.catalog.local.warehouse", str(DADOS / "warehouse"))
        .getOrCreate()
    )
