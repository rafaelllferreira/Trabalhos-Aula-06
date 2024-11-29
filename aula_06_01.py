#
while True:
    try:
     num1 = int(input("informe o primeiro número: "))
     num2 = int(input("informe o segundo número: "))
     soma = num1 / num2
    except ZeroDivisionError:
      print("Verifique o segundo valor digitado, pois ele não pode ser zero")
    else:
     print(f"A divisão dos dois números é: {soma} ")
     break
