print ('---O jogo da forca vai começar---')
palavra = input('Digite a palavra chave: ').upper().strip()
#O upper serve para transformar todas as letras em maiusculas, o strip remove os espaços em excesso

#Aqui as listas são importantes pois elas fazem o vinculo do FOR para escrever a linha
tent = []
acerto = []
erro = 0

'''Enquanto o While for verdadeiro irá executar o comando'''
while True:

    '''Essa parte do programa é responsável por mostrar a linha da forca'''
    senha =""
    for letra in palavra:
        senha += letra if letra in acerto else "_ "
    print (senha)
    '''Essa parte do programa é responsável por mostrar a linha da forca'''

    '''Parte responsável por contar erros e criar forca'''
    if erro == 1:
        print('''
                ____
               /    |
              |     
              |     
              |     
              |        \n''')
       
    elif erro == 2:
        print('''
                ____
               /    |
              |     0
              |     |
              |     |
              |        \n''')
        
    elif erro == 3:
        print('''
                ____
               /    |
              |     0
              |     |
              |     |
              |    /    \n''')
        
    elif erro == 4:
        print('''
                ____
               /    |
              |     0
              |     |
              |     |
              |    / \   \n''')
        
    elif erro == 5:
        print('''
                ____
               /    |
              |     0
              |    -|
              |     |
              |    / \   \n''')
        
    elif erro == 6:
        print('''
                ____
               /    |
              |     0
              |    -|-
              |     |
              |    / \   \n''')
        
    elif erro == 7:
        print(f'\n\33[0;30;41mVocê perdeu!!! A palavra secreta era {palavra.title()}...\33[m')
        break
    '''Parte responsável por interromper o jogo caso exceda as chances'''

    '''Linha para perguntar qual a letra o usuário quer tentar'''
   # tentativa = input ('Escolha uma letra: ').upper().strip()
    '''Linha para perguntar qual a letra o usuário quer tentar'''

    '''Blocos responsáveis por incluir o hist. nas listas'''
    if senha == palavra:
        print ('\33[0;30;42mVocê venceu\33[m')
        break
    else: 
        tentativa = input ('Escolha uma letra: ').upper().strip()
    '''Linha para perguntar qual a letra o usuário quer tentar'''
    if tentativa in palavra:
        print ('\33[0;30;42mVocê acertou!!\33[m')
        acerto += tentativa
    else:
        tent += tentativa
        erro += 1
    '''Blocos responsáveis por incluir o hist. nas listas'''



