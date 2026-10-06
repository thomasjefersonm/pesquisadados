# pesquisadados

Trabalho de Pesquisa – **Apache Spark com Delta Lake e Apache Iceberg**
Engenharia de Dados · Engenharia de Software 5ª fase · SATC · Prof. Jorge Luiz da Silva

> 📚 Documentação completa (MkDocs): https://thomasjefersonm.github.io/pesquisadados/

## Integrantes
- Thomas Jeferson da Silva Maggi
- Bruno Ghisi da Silva

## ⚠️ Aviso
Projeto acadêmico, executado em modo local (`local[*]`). Os dados são fictícios.

## Pré-requisitos
| Item | Versão |
|---|---|
| WSL (Ubuntu) | – |
| Java (JDK) | 17 |
| Pyenv | – |
| Python | 3.11 |
| Pipx | – |
| UV | – |
| Git | – |

Bibliotecas (definidas no `pyproject.toml`): `pyspark==3.5.3`, `delta-spark==3.2.1`, `jupyterlab`, `ipykernel`, `pytest`, `mkdocs`, `taskipy`, `ruff`, `isort`, `pip-audit`.
O Iceberg é baixado automaticamente pelo Spark: `org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1`.

## Instalação

1. Instalar o Java 17 (necessário para o Spark):
```bash
sudo apt update && sudo apt install -y openjdk-17-jdk
java -version
```

2. Instalar o Python 3.11 com o Pyenv:
```bash
pyenv install 3.11
pyenv global 3.11
```

3. Instalar o UV com o Pipx:
```bash
pipx install uv
```

4. Clonar o repositório:
```bash
git clone https://github.com/thomasjefersonm/pesquisadados.git
cd pesquisadados
```

5. Criar o ambiente virtual e instalar as dependências:
```bash
uv venv
uv sync
```

## Como usar
Abrir o JupyterLab:
```bash
uv run task lab
```
Executar os notebooks (Kernel → Restart & Run All):
- `src/delta/delta_lake.ipynb`
- `src/iceberg/apache_iceberg.ipynb`

> Também é possível usar a extensão Jupyter do VS Code selecionando o kernel `.venv`.

## Testes
```bash
uv run task test
```

## Padrão de código
```bash
uv run task lint
uv run task format
uv run task audit
```

## Documentação
```bash
uv run task docs     # visualizar em http://127.0.0.1:8000
uv run task deploy   # publicar no GitHub Pages (mkdocs gh-deploy)
```

## Estrutura
```
pesquisadados/
├── README.md
├── .python-version
├── .gitignore
├── pyproject.toml
├── mkdocs.yml
├── pesquisadados/      # pacote: sessões Spark Delta e Iceberg
├── src/
│   ├── delta/          # notebook Delta Lake
│   └── iceberg/        # notebook Apache Iceberg
├── data/               # CSVs do conjunto de dados
├── docs/               # páginas do MkDocs
├── tests/              # testes Pytest
├── assets/             # modelo ER
├── logs/  scripts/  examples/
```
.
## Referências
- https://github.com/jlsilva01/spark-delta
- https://github.com/jlsilva01/spark-iceberg
- https://docs.delta.io/
- https://iceberg.apache.org/docs/latest/spark-getting-started/
- https://docs.astral.sh/uv/
- https://www.mkdocs.org/
