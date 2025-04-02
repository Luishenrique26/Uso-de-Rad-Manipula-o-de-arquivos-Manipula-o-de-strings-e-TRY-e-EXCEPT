def divide(x, y):
    try:
        resultado = x / y 
    except ZeroDivisionError:
        print("Opa, para aí!, Voce está tentando dividir por zero!!!") 
    else:
        print("certa ! A sua resposta :", resultado)
    finally:
       #Este bloco sempre será executado!
       #independente de ocorrer erro ou não.
     print('isso sempre aparecerá')

divide(3, 2)
divide(3, 0)

   