# crie um programa que calcule a quantidade de bebidas e de carne
# para a organização de um churrasco

# 1) solicitar o numero de convidados
# 2) criar uma função que calcule a quantidade total de bebidas
# 3) criar um programa que calcule a quantidade total de carnes
# 4) mostrar quantas bebidas e carnes precisam ser comprados

convidados = int(input('digite o número de convidados:'))

def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro =2.25):
    total_ml = convidados * consumo_por_pessoa_ml # calcula o consumo de bebidas total por convidado/ml
    total_litro= total_ml/1000 # converte o consumo para litro

    garrafas = int(total_litro//volume_garrafa_litro) # divide o total do consumo pelo volume da garrafa
    if total_litro % volume_garrafa_litro > 0: # se o resultado for um numero decimal
        garrafas += 1 # acrescenta uma garrafa a compra
    return total_litro, garrafas # retorna omtotal em litros o numero de garrafas

# resultado=calcular_bebidas(convidados)
# print(resultado)

def calcular_carne(convidados, consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama # informa a quantidade total de carne em gramas
    total_kg = total_gramas/1000 # transforma o valor para quilo
    return total_kg

litro, garrafas = calcular_bebidas(convidados)
carne_kg = calcular_carne(convidados) 

print('\n___quantidade total para churrasco___')
print(f'numero de convidados: {convidados}')
print(f'refrigerantes necessários: {litro}')
print(f'garrafas de 2,5L: {garrafas} unidades')
print(f'carne necessária: {carne_kg:.2f} kg')





