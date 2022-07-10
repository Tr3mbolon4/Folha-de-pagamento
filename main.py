print('='*43)
print('       Alexandre Santana Dos Santos:')
print( ' *'*52)
print('     cybersegurança em formação| linux | python | C++ | hardware | redes | Ethical Hacking')
print('   *'*39)
print('        C O D I G O - P Y T H O N')
print('='*50)
print('='*50)
print('='*50)



salario = int(input('Digite seu Salario: '))
print('='*50)
vale = int(input('Quantos Pegou de vale: '))
print('='*50)
desconto_compras = float(input('desconto de compras: '))
hrs_extras = float(9.63)
print('='*50)
print('Digite somente HRS Extra de segunda a Sabados que são 50%!')
hrs_estras2 = float(input('Total de horas Extras: '))
print('='*50)
hrs_estras_100_2 = 19.26
print('Digite Somente HRS feriados e Domingo que são 100%')
hrs_estras_100 = float(input('Total de horas Extras: '))
resultado_hrs = hrs_extras * hrs_estras2
resultado_hrs_100 = hrs_estras_100 * hrs_estras_100_2
resultado_total = resultado_hrs + resultado_hrs_100 + salario
resultado_liquido = resultado_total * 0.08
bruto = resultado_hrs + resultado_hrs_100 + salario

def soma(*numeros):
  resultado = 0
  for num in numeros:
    resultado += num
  return resultado
print('='*50)
print('__________Resultado A receber_________')
x = soma(resultado_liquido + vale + desconto_compras - resultado_total )
print('SALARIO LIQUIDO: ', x)
print(f' Horas Extras 50% R$:{resultado_hrs}')
print(f' Horas Extras 100% R$:{resultado_hrs_100}')
print(f' Salario Bruto sem desconto R$:{bruto}')


    