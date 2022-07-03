nome = input()
salario = float(input())
vendas = float(input())
comissao = 0.15 * vendas
salariofinal = comissao + salario
print("TOTAL = R$ %.2f"%salariofinal)
