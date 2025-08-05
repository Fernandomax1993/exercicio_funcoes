import os
from time import sleep


menu = {
        '[1]-Arroz, Feijão , e bife':   - 35.99,
        '[2]-Macarrão com Carne moida': - 29.99,
        '[3]-lagosta a moda da casa':   - 120.00 , 
        '[4]-Churrasco':                -  65.99
    }

total = 0.0

     
     
while True:
    os.system("cls")
    print('=-='*30)

    print(' Bem vindo ao restaurante Xavis')

    print('=-='*30)

    for k,v in menu.items():
        print(f"{k} - (R${v})")
    
    
    opcao = int(input('Escolha uma opção (opção [0] para sair) : '))
    if opcao == 0:
        break
    if opcao <= len(menu.keys()):
        descricao = list(menu.keys())[opcao-1]
        valor     = list(menu.values())[opcao-1]
        print(f'vc escolheu:',descricao,valor)
        sleep(2)
        
        total+=valor
    else:
        os.system("cls")
        print("Opção inválida!")
        sleep(2)
print(f'o total foi {total:.2f}')




