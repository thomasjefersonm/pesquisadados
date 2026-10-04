from pesquisadados.main import DADOS, ICEBERG_PACOTE


def test_pasta_dados_existe():
    assert DADOS.exists()


def test_pacote_iceberg_compativel_spark_35():
    assert "3.5_2.12" in ICEBERG_PACOTE
