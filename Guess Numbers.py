## Desafio 1 - Adivinha Números ## Squad 3 - Os Bagual
import random                                                                     # Importa uma biblioteca para randomizar os números

def RandomizaNum(quant):                                                          # Função para randomizar os números
  if(quant == 1):                                                                 # Randomizar número de 1(um) algarismo - modo facíl
    num = random.randint(1,9)                                                     # Randomizador de número
    UmAlgarismo(num)                                                              # Chama a função para jogar com um algarismo
  elif(quant == 2):                                                               # Randomizar número de 2(dois) algarismos - modo médio
    num = random.randint(10,99)                                                   # Randomizador de número
    DoisAlgarismo(num)                                                            # Chama a função para jogar com dois algarismos
  elif(quant == 3):                                                               # Randomizar número de 3(três) algarismos - modo difícil
    num = random.randint(100,999)                                                 # Randomizador de número
    TresAlgarismo(num)                                                            # Chama função para jogar com três algarismos
  else:                                                                           # Randomizar número de 4(quatro) algarismos - modo impossível
    num = random.randint(1000,9999)                                               # Randomizador de número
    QuatroAlgarismo(num)                                                          # Chama função para jogar com quatro algarismos

def PedeTudo():                                                                   # Função inicial
  print("Modos de jogo:\nFácil = 1(um) algarismo\nMédio = 2(dois) algarismos\nDifícil = 3(três) algarismos\nImpossível = 4(quatro) algarismos") # Informa os modos de jogo e quantos algarismo eles tem
  quant_num = int(input("Digite o modo de jogo: 1=Fácil - 2=Médio - 3=Difícil - 4=Impossível"))  # Pede o tamanho do número que o usuário deseja
  while(quant_num < 1 or quant_num > 4):                                          # Enquanto não estiver dentro dos parametros, será perguntado para o usuário um novo número                                       
    print("FAVOR DIGITAR UM MODO DE JOGO DE 1 À 4")                               # Informa o número de algarismos que o usuário deve informar
    print("Modos de jogo:\nFácil = 1(um) algarismo\nMédio = 2(dois) algarismos\nDifícil = 3(três) algarismos\nImpossível = 4(quatro) algarismos") # Informa os modos de jogo e quantos algarismo eles tem
    quant_num = int(input("Digite o modo de jogo: 1=Fácil - 2=Médio - 3=Difícil - 4=Impossível"))# Pede o tamanho do número que o usuário deseja
  RandomizaNum(quant_num)                                                         # Chama a função randomizadora para randomizar o número e começar o jogo com o jogador

def VerificaNum(nivel):                                                           # Função para verificar o número que o jogador informar
  segue = False                                                                   # Variável para parar o while
  while not segue:                                                                # While para ficar perguntando a aposta do jogar 
    resp = int(input("Qual a sua aposta? "))                                      # Pergunta para o jogador a sua aposta
    if(nivel == 1):                                                               # Verifica se o modo de jogo escolhido foi o fácil
      if(resp >= 1 and resp <= 9):                                                # Verifica se a resposta do jogador está dentro do jogável para o modo de jogo escolhido
        return resp                                                               # Retorna a resposta do jogador
      else:                                                                       # Caso o número não esteja entre os números jogáveis
        print("Digite um número de 1 até 9")                                      # Informa quais os núemeros que podem ser utilizados para jogar
    if(nivel == 2):                                                               # Verifica se o modo de jogo escolhido foi o médio
      if(resp >= 10 and resp <= 99):                                              # Verifica se a resposta do jogador está dentro do jogável para o modo de jogo escolhido
        respo = str(resp)                                                         # Transforma a resposta do jogador em String
        return respo                                                              # Retorna a resposta do jogador
      else:                                                                       # Caso o número não esteja entre os números jogáveis
        print("Digite um número de 10 até 99")                                    # Informa quais os núemeros que podem ser utilizados para jogar
    if(nivel == 3):                                                               # Verifica se o modo de jogo escolhido foi o difícil
      if(resp >= 100 and resp <= 999):                                            # Verifica se a resposta do jogador está dentro do jogável para o modo de jogo escolhido
        respo = str(resp)                                                         # Transforma a resposta do jogador em String
        return respo                                                              # Retorna a resposta do jogador
      else:                                                                       # Caso o número não esteja entre os números jogáveis
        print("Digite um número de 100 até 999")                                  # Informa quais os núemeros que podem ser utilizados para jogar
    if(nivel == 4):                                                               # Verifica se o modo de jogo escolhido foi o
      if(resp >= 100 and resp <= 9999):                                           # Verifica se a resposta do jogador está dentro do jogável para o modo de jogo escolhido
        respo = str(resp)                                                         # Transforma a resposta do jogador em String
        return respo                                                              # Retorna a resposta do jogador
      else:                                                                       # Caso o número não esteja entre os números jogáveis
        print("Digite um número de 1000 até 9999")                                # Informa quais os núemeros que podem ser utilizados para jogar

def UmAlgarismo(num):                                                             # Função para jogar com apenas um digito
  resposta = VerificaNum(1)                                                       # Chama função para o jogador informar uma aposta
  while(resposta != num):                                                         # Enquanto a resposta do jogador for diferente do número aleatório, o jogo continua
    if(resposta > num):                                                           # Verifica se a resposta do jogador é maior que o número sorteado
      print("Você errou. Digite um número menor")                                 # Informa que o jogador errou o número, dizendo para ele tentar um número menor
    else:                                                                         # Em conjunto com a verificação se a resposta do jogador, desta vez é para quando o número for menor que o sorteado
      print("Você errou. Digite um número maior")                                 # Informa que o jogador errou o número, dizendo para ele tentar um número menor
    resposta = VerificaNum(1)                                                     # Chama função para o jogador informar uma aposta
  print("Acertou mizeravi!!!!")                                                   # Informa que o usuário acertou o número
  jogar = input("Deseja jogar novamente? Digite sim ou não.").lower()             # Pergunta se o jogador quer jogar novamente - Transforma a resposta do jogador para LowerCase
  if(jogar == 'sim'):                                                             # Verifica se a resposta do jogador para jogar novamente for sim
    PedeTudo()                                                                    # Se o jogador quer jogar novamente o programa é reiniciado voltando para a função de ínicio
  else:                                                                           # Resposta do jogador foi parar de jogar
    print("Obrigado por jogar!")                                                  # Da tchau para o jogador

def DoisAlgarismo(num):                                                           # Função para jogar com dois digitos
  numStr = str(num)                                                               # Transforma o número aleatório em String
  resposta = VerificaNum(2)                                                       # Chama função para o jogador informar uma aposta
  while(resposta != numStr):                                                      # Enquanto a resposta do jogador for diferente do número aleatório, o jogo continua
    for i in range(2):                                                            # For para pegar cada número que o usuário digitou
      for j in range(2):     
        if(resposta[i] == numStr[j]):                                             # Verifica se um dos algarismos que o usuário digitou é igual ao primeiro algarismo do número aleatório
          print(i+1,"º número correto na ", j+1, "º posição")                     # Informa para o jogador qual número está correto em qual posição
    resposta = VerificaNum(2)                                                     # Chama função para o jogador informar uma aposta
  print("Acertou mizeravi!!!")                                                    # Informa que o jogador acertou o número
  jogar = input("Deseja jogar novamente? Digite sim ou não.").lower()             # Pergunta se o jogador quer jogar novamente - Transforma a resposta do jogador para LowerCase
  if(jogar == 'sim'):                                                             # Verifica se a resposta do jogador para jogar novamente for sim
    PedeTudo()                                                                    # Se o jogador quer jogar novamente o programa é reiniciado voltando para a função de ínicio
  else:                                                                           # Resposta do jogador foi parar de jogar
    print("Obrigado por Jogar!")                                                  # Da tchau para o jogador

def TresAlgarismo(numer):                                                         # Função para jogar com três digitos
  num = str(numer)                                                                # Transforma o número aleatório em String
  resposta = VerificaNum(3)                                                       # Chama função para o jogador informar uma aposta
  while(resposta != num):                                                         # Enquanto a resposta do jogador for diferente do número aleatório, o jogo continua
    for i in range(3):                                                            # For para pegar cada número que o usuário digitou
      for j in range(3):                                                          # For para pegar cada número aleatório
        if(resposta[i] == num[j]):                                                # Verifica se um dos algarismos que o usuário digitou é igual a algum algarismo do número aleatório
          print(i+1, "º número correto na ", j+1,"º posição")                     # Informa para o jogador qual número está correto na em qual posição
    resposta = VerificaNum(3)                                                     # Chama função para o jogador informar uma aposta
  print("Acertou mizeravi!!!")                                                    # Informa que o jogador acertou o número
  jogar = input("Deseja jogar novamente? Digite sim ou não.").lower()             # Pergunta se o jogador quer jogar novamente - Transforma a resposta do jogador para LowerCase
  if(jogar == 'sim'):                                                             # Verifica se a resposta do jogador para jogar novamente for sim
    PedeTudo()                                                                    # Se o jogador quer jogar novamente o programa é reiniciado voltando para a função de ínicio
  else:                                                                           # Resposta do jogador foi parar de jogar
    print("Obrigado por jogar!")                                                  # Da tchau para o jogador

def QuatroAlgarismo(numer):                                                       # Função para jogar com quatro digitos
  num = str(numer)                                                                # Transforma o número aleatório em String
  resposta = VerificaNum(4)                                                       # Chama função para o jogador informar uma aposta
  while(resposta != num):                                                         # Enquanto a resposta do jogador for diferente do número aleatório, o jogo continua
    for i in range(4):                                                            # For para pegar cada número que o usuário digitou
      for j in range(4):                                                          # For para pegar cada número aleatório
        if(resposta[i] == num[j]):                                                # Verifica se um dos algarismos que o usuário digitou é igual a algum algarismo do número aleatório
          print(i+1, "º número correto em alguma posição")                        # Informa que o jogador acertou o número
    resposta = VerificaNum(4)                                                     # Chama função para o jogador informar uma aposta
  print("Acertou mizeravi!!!")                                                    # Informa que o jogador acertou o número
  jogar = input("Deseja jogar novamente? Digite sim ou não").lower()              # Pergunta se o jogador quer jogar novamente - Transforma a respota do jogaro para LowerCase
  if(jogar == 'sim'):                                                             # Verifica se a resposta do jogador para jogar novamente for sim
    PedeTudo()                                                                    # Se o jogador quer jogar novamente o programa é reiniciado voltando para a função de ínicio
  else:                                                                           # Resposta do jogador foi parar de jogar
    print("Obrigado por jogar!")                                                  # Da tchau para o jogador
  
PedeTudo()                                                                        # Chama a função principal para iniciar o programa
