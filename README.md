# Codebench Analytics

Projeto para extração de métricas do [Codebench](https://codebench.icomp.ufam.edu.br/).

## Setup

Este projeto usa [Poetry](https://python-poetry.org/) para gerenciamento de dependências. Para instalá-lo, siga [este tutorial](https://python-poetry.org/docs/#installation). Além disso, é necessário Python instalado a partir da versão 3.11. Versões antigas talvez funcionem, basta editar o [`pyproject.toml`](pyproject.toml).

Após instalação do Poetry, rode os seguintes comandos:

```shell
poetry env use 3.11
poetry install
```

Alternativamente você pode rodar `make setup`, que basicamente faz a mesma coisa.

## Execução

Este projeto possui três tipos de operações: `execution`, `actions` e `solution`.

* `execution`: extrai métricas relacionadas à execução de código na IDE do Codebench, tais como testes e submissões
* `actions`: extrai métricas relacionadas à interação dos alunos na IDE do Codebench, tais como teclas digitadas, botões clicados, etc.
* `solutions`: extrai métricas de código das soluções pré-cadastradas no Codebench pelos professores ou monitores.

### Extraindo métricas de execução ou ação

Para rodar o projeto para extrair métricas de execução ou ação, rode o seguinte comando:

```shell
poetry run codebench_analytics (execution|action) [-p <caminho/ate/dataset/codebench>] [-k (exam|homework)]
```

O parâmetro `-p` (ou `--path`) especifica o diretório base para o dataset do Codebench. Para definir múltiplos diretórios, basta repetir o argumento:

```shell
poetry run codebench_analytics -p codebench/dataset/2021-1 -p codebench/dataset/2022-2
```

Já o parâmetro `-k` (ou `--kind`) especifica os tipos de atividades que devem ser consideradas na geração do dataset, os quais podem ser provas (exam) ou trabalhos (homework). Se esse parâmetro não for definido, os dois tipos serão considerados. Se apenas um parâmetro for definido, somente a ativdade especificada será considerada. Por exemplo, o comando abaixo considera apenas as atividades do tipo prova durante a geração das métricas

```shell
poetry run codebench_analytics (execution|action) -p codebench/dataset/2021-1 -p codebench/dataset/2022-2 -k exam
```

Após o término da execução, você verá uma pasta chamada `output` na raiz do projeto.

### Extraindo métricas de código da solução

Para rodar o projeto apenas para extração de métricas de código, rode o seguinte comando:

```shell
poetry run codebench_analytics solution -p <csv/com/solucoes/do/instrutor>
```
