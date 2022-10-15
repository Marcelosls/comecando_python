import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    #gera numero aleatorio entre 1 e 50
    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível:"))

    if nivel == 1:
        total_de_tentativas = 20
        dificuldade = "FÁCIL"
    elif nivel == 2:
        total_de_tentativas = 10
        dificuldade = "MÉDIO"
    else:
        total_de_tentativas = 5
        dificuldade = "DÍFICIL"

    #loop
    #while rodada <=total_de_tentativas:
    for rodada in range (1, total_de_tentativas+1):
        print("tentativas {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite o seu numero entre 1 e 50:"))
        print("você digitou", chute)

        if chute < 1 or chute > 50:
           print("você deve digitar um numero entre 1 e 50")
           continue
        #condições
        acertou = chute == numero_secreto
        errou = chute != numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('PARABÉNS!! VOCE VENCEU O JOGO!')
            #ASCII FOGOS DE ARTIFICIL
            print("""                          .''.       
                   .''.      .        *''*    :_\/_:     . 
                  :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
              .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
             :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
             : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
              '..'  ':::'     * /\ *     .'/.\'.   '
                  *            *..*         :
                    *
                      *""")
            break
        else:
            if maior:
                print('SEU NUMERO FOI MAIS ALTO!')
            elif menor:
                print('SEU NUMERO FOI MAIS BAIXO!')
            pontos_perdidos = abs(chute - numero_secreto)*10  # pontos perdidos da rodada
            pontos = pontos - pontos_perdidos  # subtraindo os pontos perdidos da pontuação total
    if errou:
        print("o numero secreto era:", numero_secreto)

    print("FIM DE JOGO VOCÊ FEZ {} PONTOS! NA DIFICULDADE {}".format(pontos, dificuldade))

if __name__=="__main__":
    jogar()