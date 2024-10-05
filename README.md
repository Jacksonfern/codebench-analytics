# Codebench Analytics

Extração de métricas do Codebench.

## Setup

### Requisitos

Este projeto usa [Poetry](https://python-poetry.org/) para gerenciamento de dependências. Para instalá-lo, siga [este tutorial](https://python-poetry.org/docs/#installation). Além disso, é necessário Python instalado a partir da versão 3.11. Versões antigas talvez funcionem, basta editar o [`pyproject.toml`](pyproject.toml).

Após instalação do Poetry, rode os seguintes comandos:

```shell
poetry env use 3.11
poetry install
```

## Rodando

Para rodar o projeto rode o seguinte comando:

```shell
poetry run python codebench_analytics/main.py
```