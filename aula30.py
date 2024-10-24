# CONSTANTE = "Variáveis" que NÃO vão mudar

velocidade = input('Qual a velocidade atual do carro? ')  # velocidade atual do carro
local_carro = input('Qual o local do carro na estrada? ')  # local em que o carro está na estrada

velocidade_int = int(velocidade)
local_carro_int = int(local_carro)

RADAR_1 = 60  # CONSTANTE > velocidade máxima do radar 1
LOCAL_1 = 100 # CONSTANTE > local onde o radar 1 está
RADAR_RANGE = 1 # CONSTANTE > A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade_int > RADAR_1
carro_passou_radar_1 = local_carro_int >= (LOCAL_1 - RADAR_RANGE) and local_carro_int <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade acima do permitido')
else:
    print('Velocidade permitida')

if carro_passou_radar_1:
    print(f'Carro passou radar com velocidade {velocidade_int}')
else:
    print('O carro não está próximo do radar')

if carro_multado_radar_1:
    print('Carro multado em radar')
else:
    print('Carro não foi multado')