import random
import os
import sys
import time
import webbrowser

def abrir_janelas():
    # listas d urls para navegador abrir
    urls = [
           "https://g1.globo.com/"
         
    ]
    for i in range(1):

        # loop q sorteia urls
        url = random.choice(urls) #opção qe url é sorteada da lista
        url = urls[i] # opção que abre todas as urls em ordem
        webbrowser.open(url) #abre url no navegador (uma por vez)

def evento_aleatorio():
    opcoes = 6      #numero de opções sorteadas                                                                   
    escolha_indesejada = random.randint(1, opcoes) #sorteio um numero de 1 a 6

    try:
         escolha = int(input(f"escolha um numero entre 1 e {opcoes}:"))  # tente rodar e input

            #use a escolha  for menor que 1 ou maior que 6 - mensagem de erro 
         if escolha  < 1 or escolha > opcoes:
            False ValueError ("numero fora do intervalo!")

    except ValueError as e :                                            #caso houver algum erro mande digitar novamnete
        print("entrada invalida :{e}. tente de novo")
        evento_aleatorio()

        #se o numero digitado for igual o numero sorteado
    if escolha == escolha_indesejada:
        print('ops,ja, era ,voce perdeu!')
        abrir_janelas() #chama função de abrir janelas 
        time.sleep(1)  #esperar 5 segundos
        # parar windows
        if sys.plataform =='win32':
             os.system("shutdown /s /t 1")
          # parar linux
        elif sys.plataform == 'linux' or sys.plataform == 'linux2':
             os.system('shutdown now')
        # parar mec
        elif sys.plataform == 'darwin':
            os.system('shutdown -h now')
         
        sys.exit()
    else:
        print('voce esta seguro por enquanto!')
        evento_aleatorio()

evento_aleatorio()
