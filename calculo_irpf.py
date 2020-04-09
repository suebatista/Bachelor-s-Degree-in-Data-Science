'''
Elaboração de um algoritmo para calcular o imposto de renda de um contribuinte a partir de seu salário bruto e do número de seus dependentes.
'''
salario_bruto=int(input("Qual seu salário bruto?"))
dependentes=int(input("Qual o número de dependentes?"))
def inss(salario_bruto):
    inss=0
    if salario_bruto<=1045:
        return 0.075*salario_bruto
        print("Seu INSS é de {}".format(inss))
    if salario_bruto < 2089.60:
            return 0.09*salario_bruto
    elif salario_bruto< 3134.40:
            return 0.12*salario_bruto
    elif salario_bruto<= 6101.06:
            return 0.14*salario_bruto
            
taxa_inss=inss(salario_bruto)
            
print("A sua taxa de contribuição previdenciária é de {}".format(taxa_inss))

salario_base = salario_bruto - taxa_inss - (dependentes*189.59)
print("Seu salário base é de {}".format(salario_base))

def irpf(salario_base,dependentes):
    if salario_base < 1903.99:
        print("Você não precisa declarar imposto de renda")
    elif salario_base <= 2826.65:
        return (0.075*salario_base) - 142.80
    elif salario_base <= 3751.05:
        return (0.15*salario_base) - 354.80 
    elif salario_base <= 4664.68:
        return (0.15*salario_base) - 636.13
    elif  salario_base >=4664.68:
        return (0.275*salario_base) - 869.36
        
taxa_irpf = round(irpf(salario_base,dependentes))
print("O valor de imposto de renda é de {}".format(taxa_irpf))

        