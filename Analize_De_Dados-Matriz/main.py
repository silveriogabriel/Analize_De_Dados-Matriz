'''
    Analize de dados de acordo com a tabela
    By: Gabriel Silvério
'''

#DEFININDO DADOS DA TABELA

matrizalfa = [['alfa-romero', 'alfa-romero', 'audi', 'audi',  'bmw',   'bmw',     'dodge', 'honda', 'honda', 'jaguar', 'mercedes-benz', 'mercedes-benz', 'mitsubishi', 'mitsubishi', 'nissan',    'nissan',    'nissan',   'porsche', 'porsche',     'porsche', 'subaru', 'subaru', 'toyota', 'toyota',  'volkswagen', 'volkswagen', 'Volvo',   'Volvo'],
              [   'Gas'     ,       'Gas'  ,  'Gas',  'Gas',  'Gas',   'Gas',       'Gas',   'Gas',   'Gas',    'Gas',        'Diesel',        'Diesel',        'Gas',        'Gas',    'Gas',       'Gas',       'Gas',       'Gas',     'Gas',         'Gas',    'Gas',    'Gas', 'Diesel',    'Gas',         'Gas',        'Gas',   'Gas', 'Diesel' ], 
              ['convertible',   'hatchback','wagon','sedan','sedan', 'sedan', 'hatchback', 'wagon', 'sedan',  'sedan',         'wagon',       'hardtop',      'sedan',      'sedan',  'wagon', 'hatchback', 'hatchback', 'hatchback', 'hardtop', 'convertible',  'sedan',  'wagon',  'sedan',  'wagon', 'convertible',      'wagon', 'sedan',   'sedan'],
              [        '111',         '154',  '110',  '140',  '101',   '101',       '145',    '76',   '100',    '262',           '123',           '123',         '88',        '116',    '152',       '200',       '160',       '143',     '207',         '207',    '111',    '111',     '73',    '156',          '90',         '88',   '114',     '106'],
             [[         '27',          '26',   '25',   '20',   '29',    '29',        '24',    '34',    '31',     '17',            '25',            '25',         '32',         '30',     '22',        '23',        '25',        '27',      '25',          '25',     '29',     '23',     '33',     '24',          '29',         '31',    '28',      '27'],
              [         '21',          '19',   '19',   '17',   '23',    '23',        '19',    '30',    '25',     '13',            '22',            '22',         '25',         '23',     '17',        '17',        '19',        '19',      '17',          '17',     '24',     '23',     '30',     '19',          '24',         '25',    '23',      '26']],
              [      '16500',       '16500','18920','23875','16430', '16925',     '12964',  '7295', '10345',  '36000',         '28248',         '28176',       '8189',       '9279',  '14399',     '19699',     '18399',     '22018',   '34028',       '37028',  '11259',  '11694',  '10698',  '15750',       '11595',      '12290', '12940',   '22470']]
#Cabeçalho

print('-=' * 40)
print('                            COMPUTAÇÃO APLICADA À ENGENHARIA (CAE)')
print('-=' * 40)
print()

#Definindo variaveis e listas necessarias

matrizbeta = [[], [], [], []]
media = 0
cont = 1
menor = 0
marcamenor = ''
condicao = False

#Laço para calcular a media dos valores


for i in range(len(matrizalfa[0])):
    if matrizalfa[0][i] not in matrizbeta[0]:
        if i != 0:
            matrizbeta[0].append(matrizbeta[0][-1] / cont)
        matrizbeta[0].append(matrizalfa[0][i])
        matrizbeta[0].append(int(matrizalfa[5][i]))
        condicao = True
    else:
        matrizbeta[0][-1] += int(matrizalfa[5][i])
        cont += 1
        condicao == False

    if condicao == True:
        cont = 1
        condicao = False
    if i == len(matrizalfa[0]) - 1:
        matrizbeta[0][-1] = matrizbeta[0][-1] / cont
media = media / len(matrizalfa[5])

#Laço para verificar o menor valor 

for i in range(len(precos)):
    if i == 0:
        menor = matrizbeta[0][i]
    if precos[i] < menor:
        menor = matrizbeta[0][i]
        marcamenor = marcas[i]

#marca para verificar milhas por galao

for i in range(len(matrizalfa[4])):
    for v in range(len(matrizalfa[4][i])):
        if i == 0:
            diferencalitros.append(int(matrizalfa[4][i][v]))
        else:
            diferencalitros[v] -= int(matrizalfa[4][i][v])

#laco para verificar veiculos que ultilizao combustiveis Diesel

for i in range(len(matrizalfa[1])):
    if matrizalfa[1][i] == 'Diesel':
        if matrizalfa[0][i] not in carrosdiesel:
            carrosdiesel.append(matrizalfa[0][i])

#Prints
print(f'A marca com o menor valor médio é {marcamenor} Com o valor de {menor:.2f}R$.\n')
print(f'Os carros com diferença de 2 milhas por galão sao:\n')
#Laço para diferenca de litros
for i in diferencalitros:
    if i < 2:
        print(f'marca: {matrizalfa[0][i]} Estilo:{matrizalfa[2][i]} Cavalos: {matrizalfa[3][i]}\n')
print(f'As marcas que ultilizão diesel como principal combustiveis sao: ',end='')
#Laço para mostrar carros a diesel
for i in carrosdiesel:
    print(i,end=', ')


print('\n')
input('\nPresione ENTER')
