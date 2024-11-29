#
def somar(num1,num2):
    soma = num1 + num2
    print(f"A soma dos valores é {soma}")
def subtrair(num1,num2):
    sub = num1 - num2
    print(f"A diferença dos valores é {sub}")

n1 = int(input("Informe o Primeiro valor: "))
n2 = int(input("Informe o Segundo valor: "))
somar(n1,n2)
subtrair(n1,n2)