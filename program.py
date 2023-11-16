import re
import ttg

def identificar_variaveis(formula):

    # Elementos a serem desconsiderados da formúla para filtragem das variáveis proposicionais
    # elementos_reservados é do tipo list, pois a ordem dos elementos importa
    elementos_reservados = ['not', '-', '~', 'nor', 'xor', 'or', '!=', 'nand', 'and', '=>', 'implies', '=', '(', ')']
    
    for elemento in elementos_reservados:
      formula = formula.replace(elemento, ' ')

    # Regex: Sequências de caracteres que são compostas apenas por letras minúsculas 
    # re.findall retorna uma lista de todas as correspondências encontradas
    # Utilizado para desconsideração de 'espaços'
    variaveis = re.findall(r'\b[a-z]+\b', formula) 

    # set: cria conjunto sem duplicatas
    # sorted: ordena o conjunto
    variaveis = sorted(set(variaveis))

    return variaveis

def identificar_operacoes(formula):

    # Inicializa um dicionário para contar as operações
    operacoes = {'~': 0, 'nor': 0, 'xor': 0, 'or': 0, 'nand': 0, 'and': 0, '=>': 0, '=': 0}

    # Substitui variantes por operações padrão para facilitar a contagem
    formula_revisada = formula.replace('!=', 'xor').replace('implies', '=>').replace('-', '~').replace('not', '~')

    # Conta as operações na fórmula e as remove para não que os já contados não interfiram nos próximos
    for operacao in operacoes:
        operacoes[operacao] = formula_revisada.count(operacao)
        formula_revisada = formula_revisada.replace(operacao, ' ')

    return operacoes

def gerar_tabela_verdade(variaveis, formula):
  try:
    table = (ttg.Truths(variaveis, [formula]))
    print(table)
    return
  except Exception as e:
    print("Não foi possível gerar a tabela verdade desta formula, verifique-a")
    return

def main():
  while True:
    formula = input("Digite a fórmula: ")

    # Transforma a fórmula em minúsculo
    formula_minusc = formula.lower()

    # Identifica as variáveis proposicionais a partir de uma cópia da formula
    variaveis = identificar_variaveis(formula_minusc[:])

    # Identifica as operações a partir de uma cópia da formula
    operacoes = identificar_operacoes(formula_minusc[:])

    # Apresenta os resultados
    print(f"Fórmula em minúsculo: {formula_minusc}")
    print(f"Variáveis: {variaveis}")
    print("Operações:")
    for operacao, count in operacoes.items():
      if count > 0:
        plural = 'es' if count > 1 else ''
        ocorrencias = f"{count} vez{plural}"
        print(f"     {operacao}: {ocorrencias}")

    # Gera tabela verdade utilizando a biblioteca ttg
    gerar_tabela_verdade(variaveis, formula_minusc)

    continuar = input("Deseja digitar outra fórmula? (Digite s para SIM, Ou qualquer outro caracter para NÃO) ").lower()
    if continuar != 's':
      break

main()