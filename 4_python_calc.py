num_1=int(input("Digitar ano de nascimento: "))
num_2=int(input("Digitar ano atual: "))
idade=num_2-num_1

if idade <= 20 <= 30:
    print("Sua idade é :",idade,"você é bem experiente!")
else:
    print("Sua idade é :",idade,"você é bem jovem!")