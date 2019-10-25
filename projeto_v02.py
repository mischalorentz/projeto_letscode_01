import time
print ('\33[0;30;46m--- Olá, jogadores! Vamos brincar de forca? ---\33[m\n')
time.sleep(1)
nome1 = input("\33[0;30;46m--- Jogador 1, qual o seu nome? ---\33[m\n")
time.sleep(0.5)

palavra = input("\33[0;30;46m---" + nome1 + ", escolha uma palavra: ---\33[m\n".lower())
time.sleep(0.5)
print("\33[0;30;46m---Agora o segundo jogador precisa adivinhar a palavra!---\33[m\n")
time.sleep(1)
nome2 = input("\33[0;30;46m---Jogador 2, qual o seu nome? ---\33[m\n")
time.sleep(0.5)
tentativas = 7

print("\33[0;30;46m---" + nome2 + ", comece a adivinhar... Você tem",tentativas, "tentativas.---\33[m\n")
time.sleep(1)

def grafico (tent): 
		if (tent == 6):
				print (" ________")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (tent == 5):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (tent == 4):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (tent == 3):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (tent == 3):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (tent == 2):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ ")
				print ("|________")
		elif (tent == 1):
				print (" ________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ \ ")
				print ("|________")
				print ("\n")
        
 
resposta = list(palavra)
posicoes = "_"* len(palavra) 
posicoes = list(posicoes)
adivinhacao = ''

while tentativas > 0:         
    erros = 0             
    for char in range (len(palavra)):
          
        if resposta[char] == adivinhacao:
            posicoes.pop(char)
            posicoes.insert(char, adivinhacao)
            print(posicoes)
        else:   
            erros += 1    
    
    if erros == 0:        
        print ("\33[0;30;42m Você venceu\33[m")  
        break              
    
    adivinhacao = input("\33[0;30;46m---Adivinhe uma letra:\33[m".lower()) 
                        

    if adivinhacao.lower ()not in palavra:  
 
        tentativas -= 1        
        print ("\33[0;30;41m Incorreto\33[m")    
        print ("\33[0;30;41m Você possui", tentativas, "mais\33[m")

        grafico(tentativas)
    
    if tentativas == 0:       
            print ("\33[0;30;41m Você perdeu\33[m") 
