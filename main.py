import csv
import re


class FormatoInvalidoError(Exception):
    """Exceção personalizada para dados em formato inválido."""
    pass


def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))


def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))


def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    return bool(re.match(padrao, telefone))


def validar_data(data):
    padrao = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    return bool(re.match(padrao, data))


def validar_registro(registro):
    erros = []

    try:
        if not validar_email(registro["email"]):
            erros.append("e-mail inválido")

        if not validar_cpf(registro["cpf"]):
            erros.append("CPF inválido")

        if not validar_telefone(registro["telefone"]):
            erros.append("telefone inválido")

        if not validar_data(registro["data_nascimento"]):
            erros.append("data inválida")

        if erros:
            raise FormatoInvalidoError(", ".join(erros))

        return True, "Registro válido"

    except KeyError as erro:
        raise KeyError(f"Coluna ausente no CSV: {erro}")

    except FormatoInvalidoError as erro:
        return False, str(erro)


def gerar_relatorio(registros_validos, registros_invalidos, total):
    percentual = (registros_validos / total * 100) if total > 0 else 0

    linhas = []

    linhas.append("=" * 50)
    linhas.append("RELATÓRIO DE ANÁLISE DE DADOS")
    linhas.append("=" * 50)
    linhas.append(f"Total de registros: {total}")
    linhas.append(f"Registros válidos: {registros_validos}")
    linhas.append(f"Registros inválidos: {registros_invalidos}")
    linhas.append(f"Percentual de aprovação: {percentual:.2f}%")
    linhas.append("")

    linhas.append("REGISTROS INVÁLIDOS")
    linhas.append("-" * 50)

    for registro in registros_invalidos:
        linhas.append(
            f"Nome: {registro['nome']} | "
            f"Problemas: {registro['problemas']}"
        )

    linhas.append("")
    linhas.append("=" * 50)

    return "\n".join(linhas)


def main():
    arquivo = "dados.csv"

    total = 0
    validos = 0
    invalidos = []

    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            leitor = csv.DictReader(file)

            for registro in leitor:
                total += 1

                try:
                    valido, mensagem = validar_registro(registro)

                    if valido:
                        validos += 1
                    else:
                        invalidos.append({
                            "nome": registro["nome"],
                            "problemas": mensagem
                        })

                except KeyError as erro:
                    print(f"Erro no registro: {erro}")

        relatorio = gerar_relatorio(
            validos,
            invalidos,
            total
        )

        with open("relatorio.txt", "w", encoding="utf-8") as file:
            file.write(relatorio)

        print(relatorio)

    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo}' não foi encontrado.")

    except ValueError:
        print("Erro: valor inválido encontrado nos dados.")

    except KeyError as erro:
        print(f"Erro: coluna obrigatória ausente: {erro}")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    else:
        print("\nAnálise concluída com sucesso.")

    finally:
        print("\nProcessamento finalizado.")


if __name__ == "__main__":
    main()
