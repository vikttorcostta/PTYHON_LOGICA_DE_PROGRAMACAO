# LIVRO: ALGORÍTOMOS - LÓGICA PARA DESENVOLVIMENTO DE COMPUTADORES 29 EDIÇÃO
# PAULO VICTOR COSTA DE MELO
# 19 DEZEMBRO 2023

print("CALCULO DO SALARIO DO PROFESSOR")

horas_trabalhadas_por_mes = int(input("Informe a quantidade de horas trabalhadas por mes -> "))
valor_hora_aula = int(input("Informe o valor da hora -> "))
percentual_de_desconto = int(input("Informe o percentual de -> "))

salario_bruto = horas_trabalhadas_por_mes * valor_hora_aula
total_de_desconto = percentual_de_desconto / 100

salario_liquido = salario_bruto - total_de_desconto

print("O salario bruto", salario_bruto)
print("O Salario liquido", salario_liquido)

