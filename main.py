import math
import os

cte_magnetica = 4e-7 * math.pi
vel_luz = 3e+8

def imprime_tela_inicial():
    print("\n**********************************************************")
    print("********** CALCULADORA - ONDAS ELETROMAGNETICAS **********")
    print("**********************************************************")
    
    print("\nAutoria: Mariane S. Carvalho\tTurma: 610")

    print("\nO programa em questão é uma calculadora dedicada à análise de ondas eletromagnéticas, incorporando conceitos fundamentais e cálculos associados a essas ondas. A ideia principal da aplicação é fornecer uma interface simplificada para o cálculo de diferentes parâmetros de ondas eletromagnéticas, como amplitude do campo elétrico e magnético, intensidade, frequência, comprimento de onda, número de onda e frequência angular.")
    print("\nComo utilizar:\n\t1 - Execute o programa para ver a tela inicial;\n\t2 - Escolha uma opção do menu de navegação digitando o número correspondente e pressione Enter;\n\t3 - Forneça o valor solicitado pelo programa referente à opção escolhida, utilizando notacao cientifica (Ex: 3.24E-4) ou nao (Ex: 0.000324);\n\t4 - Veja os resultados calculados na tela;\n\t5 - Pressione uma tecla para continuar ou escolha a opção para encerrar o programa.")
    print("\n---------------------------------------------------------------------------------------------------------------")

def menu_nav():
    print("\nSelecione a entrada:\n\n\t1 - Amplitude do campo eletrico (Em)\n\t2 - Amplitude do campo magnetico (Bm)\n\t3 - Intensidade da OEM (I)\n\t4 - Frequencia (f)\n\t5 - Comprimento de onda (λ)\n\t6 - Numero de onda (k)\n\t7 - Frequencia angular (ω)\n\t8 - Encerrar programa")

def calcula_intensidade(opcao_calculo, valor_fornecido):
    intensidade = 0

    if opcao_calculo == 1:  # calculado a partir do campo eletrico
        intensidade = (math.pow(valor_fornecido, 2)) / (2 * cte_magnetica * vel_luz)
    else:   # calculado a partir do campo magnetico
        intensidade = vel_luz * math.pow(valor_fornecido, 2) / (2 * cte_magnetica)

    print(f"I = {intensidade:.2E} W/m²")

def calcula_campo_mag(opcao_calculo, valor_fornecido):
    campo_magnetico = 0

    if opcao_calculo == 1:  # calculado a partir do campo eletrico
        campo_magnetico = valor_fornecido / vel_luz
    else:   # calculado a partir da intensidade
        campo_magnetico = math.sqrt((valor_fornecido * 2 * cte_magnetica) / vel_luz)
    
    print(f"Bm = {campo_magnetico:.2E} T")

def calcula_campo_eletrico(opcao_calculo, valor_fornecido):
    campo_eletrico = 0

    if opcao_calculo == 1:  # calculado a partir do campo magnetico
        campo_eletrico = valor_fornecido * vel_luz
    else:   # calculado a partir da intensidade
        campo_eletrico = math.sqrt(valor_fornecido * 2 * cte_magnetica * vel_luz)
    
    print(f"Em = {campo_eletrico:.2E} V/m")

def calcula_frequencia(opcao_calculo, valor_fornecido):
    freq = 0

    if opcao_calculo == 1:  # calculado a partir do comprimento de onda
        freq = vel_luz / valor_fornecido
    elif opcao_calculo == 2:    # calculado a partir do numero de onda
        freq = vel_luz * valor_fornecido / (2 * math.pi)
    elif opcao_calculo == 3:    # calculado a partir da freq. angular
        freq = valor_fornecido / (2 * math.pi)

    print(f"f = {freq:.2E} Hz")

def calcula_comprimento_onda(opcao_calculo, valor_fornecido):
    comprimento = 0

    if opcao_calculo == 1:  # calculado a partir da frequencia
        comprimento = vel_luz / valor_fornecido
    elif opcao_calculo == 2:    # calculado a partir do numero de onda
        comprimento = (2 * math.pi) / valor_fornecido
    elif opcao_calculo == 3:    # calculado a partir da freq. angular
        comprimento = (vel_luz * 2 * math.pi) / valor_fornecido

    print(f"λ = {comprimento:.2E} m")

def calcula_numero_onda(opcao_calculo, valor_fornecido):
    num_onda = 0

    if opcao_calculo == 1:  # calculado a partir da frequencia
        num_onda = (2 * math.pi * valor_fornecido) / vel_luz
    elif opcao_calculo == 2:    # calculado a partir do comprimento de onda
        num_onda = (2 * math.pi) / valor_fornecido
    elif opcao_calculo == 3:    # calculado a partir da freq. angular
        num_onda = valor_fornecido / vel_luz

    print(f"k = {num_onda:.2E} rad/m")

def calcula_freq_angular(opcao_calculo, valor_fornecido):
    freq_angular = 0

    if opcao_calculo == 1:  # calculado a partir da frequencia
        freq_angular = 2 * math.pi * valor_fornecido
    elif opcao_calculo == 2:    # calculado a partir do comprimento de onda
        freq_angular = (2 * math.pi * vel_luz) / valor_fornecido
    elif opcao_calculo == 3:    # calculado a partir do numero de onda
        freq_angular = valor_fornecido * vel_luz

    print(f"ω = {freq_angular:.2E} rad/s")


def main():
    imprime_tela_inicial()

    while(True):
        menu_nav()

        input_menu = int(input("\ndigite a opcao desejada: "))

        print()

        if input_menu == 1:
            valor = float(input("Digite o valor de Em, em V/m: "))
            
            print()

            calcula_intensidade(1, valor)
            calcula_campo_mag(1, valor)

        elif input_menu == 2:
            valor = float(input("Digite o valor de Bm, em T: "))
            
            print()

            calcula_intensidade(2, valor)
            calcula_campo_eletrico(1, valor)
        
        elif input_menu == 3:
            valor = float(input("Digite o valor de I, em W/m²: "))
            
            print()

            calcula_campo_eletrico(1, valor)
            calcula_campo_mag(2, valor)

        elif input_menu == 4:
            valor = float(input("Digite o valor de f, em Hz: "))

            print()

            calcula_comprimento_onda(1, valor)
            calcula_numero_onda(1, valor)
            calcula_freq_angular(1, valor)

        elif input_menu == 5:
            valor = float(input("Digite o valor de λ, em m: "))

            print()

            calcula_frequencia(1, valor)
            calcula_numero_onda(2, valor)
            calcula_freq_angular(2, valor)

        elif input_menu == 6:
            valor = float(input("Digite o valor de k, em rad/m: "))

            print()

            calcula_frequencia(2, valor)
            calcula_comprimento_onda(2, valor)
            calcula_freq_angular(3, valor)

        elif input_menu == 7:
            valor = float(input("Digite o valor de ω, em rad/s: "))

            print()

            calcula_frequencia(3, valor)
            calcula_comprimento_onda(3, valor)
            calcula_numero_onda(3, valor)

        elif input_menu == 8:
            break

        print()
        os.system("pause")
    
main()
    
