from datetime import timedelta, datetime

tipo_carro = input("Qual o tamanho do carro P, M, G: ")

tempo_P = 30
tempo_M = 45
tempo_G = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes= tempo_P)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes= tempo_M)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes= tempo_G)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

else:
    print("Tamanho invalido")