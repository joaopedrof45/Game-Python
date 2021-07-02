from models.calcular import Calcular

def main() -> None:
    pontos : int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade : int = int(input('Informe o nivel de dificuldade desejada [1,2,3 ou 4]:'))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação:')
    calc.mostrar_operacao()

    resultado : int = int(input())

    if calc.checar_resultado(resultado):
        pontos= pontos+1

        print(f'Voce tem {pontos} ponto(s).')

    continuar:int = int(input('Desejar continuar jogando?[1 - sim , 0-não]'))


    if continuar == 1:
        jogar(pontos)
    else:
        print(f'Voce decidiu sair do jogo com {pontos} ponto(s) até logo!')




if __name__ == '__main__':
    main()
