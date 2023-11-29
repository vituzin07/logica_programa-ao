kwh = int(input('Insira a quantidade de KwH consumida: '))
tipo = str(input('Insira o tipo de instalação(R, I, C.): '))
preço=''
if tipo=='R'and kwh<=500:
    preço = 0,40
    print(f'Você deve pagar:{preço}')
elif tipo=='R'and  kwh>500:
    preço = 0,65
    print(f'Você deve pagar:{preço}')
    
if tipo =='I' and kwh<=1000:
    preço = 0,55
    print(f'Você deve pagar:{preço}')
elif tipo =='I' and kwh>1000:
    preço = 0,60
    print(f'Você deve pagar:{preço}')

if tipo == 'C' and kwh<=5000:
    preço = 0,55
    print(f'Você deve pagar:{preço}')
elif tipo == 'C' and kwh>5000:
    preço = 0,60
    print(f'Você deve pagar:{preço}')