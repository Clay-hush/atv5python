# Sistema de Análise e Validação de Dados em Python

## Sobre o projeto

Este projeto foi desenvolvido como parte do Desafio Sprint 5, com o objetivo de aplicar conceitos de manipulação de arquivos, expressões regulares (Regex), tratamento de exceções e geração de relatórios em Python.

O sistema realiza a leitura de um arquivo CSV contendo informações de usuários e verifica se os dados estão em formatos válidos.

Os campos analisados são:

* Nome
* E-mail
* CPF
* Telefone
* Data de nascimento

Após a validação, o sistema apresenta estatísticas sobre os registros e gera um relatório em formato `.txt`.

## Tecnologias utilizadas

* Python 3
* Módulo `csv`
* Módulo `re`
* Manipulação de arquivos
* Expressões regulares
* Tratamento de exceções

## Estrutura do projeto

```text
sprint5-python/
│
├── main.py
├── dados.csv
├── relatorio.txt
└── README.md
```

## Validações com Regex

As expressões regulares foram utilizadas para verificar se os campos possuem o formato esperado.

### E-mail

```python
r"^[\w\.-]+@[\w\.-]+\.\w+$"
```

Verifica a presença de caracteres válidos, do símbolo `@` e de um domínio.

### CPF

```python
r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
```

Valida o formato:

```text
000.000.000-00
```

### Telefone

```python
r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
```

Valida formatos como:

```text
(98) 9999-9999
(98) 99999-9999
```

### Data

```python
r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
```

Valida datas no formato:

```text
dd/mm/aaaa
```

## Tratamento de exceções

O projeto utiliza tratamento de exceções para evitar que o programa seja encerrado inesperadamente.

### FileNotFoundError

É utilizado quando o arquivo CSV não é encontrado.

```python
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

### ValueError

É tratado para situações em que ocorre uma conversão ou utilização de valor inválido.

### KeyError

É tratado quando uma coluna obrigatória não existe no arquivo CSV.

### Exceção personalizada

Foi criada a classe:

```python
class FormatoInvalidoError(Exception):
    pass
```

Essa exceção é utilizada para representar uma regra específica do sistema: a existência de dados em formato inválido.

## Exemplo de entrada

O arquivo `dados.csv` possui a seguinte estrutura:

```csv
nome,email,cpf,telefone,data_nascimento
Ana Silva,ana.silva@email.com,123.456.789-09,(98) 99999-9999,15/03/2000
Carlos Souza,carlos@email.com,987.654.321-00,(98) 98888-8888,22/07/1998
João Santos,joaoemail.com,111.222.333-44,98999999999,31/12/2001
```

## Exemplo de saída

O programa apresenta um relatório semelhante a:

```text
==================================================
RELATÓRIO DE ANÁLISE DE DADOS
==================================================
Total de registros: 5
Registros válidos: 2
Registros inválidos: 3
Percentual de aprovação: 40.00%

REGISTROS INVÁLIDOS
--------------------------------------------------
Nome: João Santos | Problemas: e-mail inválido, telefone inválido
Nome: Maria Oliveira | Problemas: CPF inválido
Nome: Pedro Lima | Problemas: data inválida

==================================================
```

Além de exibir o relatório no terminal, o sistema salva os resultados no arquivo `relatorio.txt`.

