import PySimpleGUI as sg


#Definindo as janelas
def janela_entrada():
    layout = [
        [sg.Text('Essa é uma história baseada em chapeuzinho vermelho')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('História', layout=layout, finalize=True)



def janela_decisao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Qual caminho chapeuzinho deve seguir? Floresta ou Caminho seguro: ')],
        [sg.Button('Floresta'), sg.Button('Caminho seguro')]
    ]
    return sg.Window('História', layout=layout, finalize=True)



def janela_decisao2():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Pelo caminho seguro você encontrou um 100 dolares no chão, pegar ou não pegar? ')],
        [sg.Button('Pegar'), sg.Button('Não')]
    ]
    return sg.Window('História', layout=layout, finalize=True)

def janela_conclusao2():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você não pegou assim não pode devolver para o homem que estava próximo e teve que ir apé e não aguentou! ')],
        [sg.Text('YOU LOST')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)


def janela_consequencia3():
    sg.theme('Reddit')
    layout = [
        [sg.Text('O dono do dinheiro percebeu que você pegou, ele está indo atrás de você, oque fazer? ')],
        [sg.Button('Correr'), sg.Button('Devolver')]
    ]
    return sg.Window('História', layout=layout, finalize=True)


def janela_decisao3():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você correu mas ele foi mais rápido, sua mãe descobriu que você pegou o caminho da floresta')],
        [sg.Text('VOCÊ PERDEU!!!!')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)


def janela_conclusao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você devolveu o dinheiro e o homem que é amigo de sua mãe deu carona até a casa da vovó!')],
        [sg.Text                ('GANHOU!!!!')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)



def janela_escolha():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Chapeuzinho encontrou muitas frutas silvestres e mel na floresta e ela precisa comer, lembre-se que mel atrai urso e as frutas algumas são venenosas!')],
        [sg.Button('Frutas Silvestres'), sg.Button('Mel')]
    ]
    return sg.Window('História', layout=layout, finalize=True)



def janela_consequencia2():
    layout = [
        [sg.Text('As frutas era venenosas, você precisa de ajuda, para quem ligar?')],
        [sg.Button('Vovó'), sg.Button('Vizinho/Amigo')]
    ]
    return sg.Window('História', layout=layout, finalize=True)

def janela_consequencia7():
    layout = [
        [sg.Text('Seu vizinho sequestrou você!')],
        [sg.Text('YOU LOST')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)


def janela_escolha5():
    layout = [
        [sg.Text('Você ligou para sua vó mas ela contou para sua mãe que você foi pela floresta!')],
        [sg.Text('YOU LOST')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)

def janela_consequencia5():
    layout = [
        [sg.Text('O mel deu energia para continuar a viagem, e você chegou na casa da vovó!')],
        [sg.Text('YOU WIN')],
        [sg.Button('Parar'), sg.Button('Jogar Novamente')]
    ]
    return sg.Window('História', layout=layout, finalize=True)


##Condições
janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11, janela12 = janela_entrada(), janela_decisao, janela_escolha, janela_consequencia2, janela_decisao2, janela_consequencia3, janela_decisao3, janela_conclusao, janela_conclusao2, janela_escolha5, janela_consequencia7, janela_consequencia5
while True:



    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_decisao()

    if window == janela2 and event == 'Caminho seguro':
        janela5 = janela_decisao2()



    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == 'Não':
        janela9 = janela_conclusao2()

    if window == janela9 and event == 'Parar':
        break
    if window == janela9 and event == 'Jogar Novamente':
        janela1 = janela_entrada()

    if window == janela5 and event == 'Pegar':
        janela6 = janela_consequencia3()

    if window == janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == 'Correr':
        janela7 = janela_decisao3()
    if window == janela6 and event == 'Devolver':
        janela8 = janela_conclusao()

    if window == janela8 and event == 'Parar':
        break
    if window == janela8 and event == 'Jogar Novamente':
        janela1 = janela_entrada()

    if window == janela7 and event == sg.WIN_CLOSED:
        break
    if window == janela7 and event == 'Parar':
        break
    if window == janela7 and event == 'Jogar Novamente':
        janela1 = janela_entrada()




    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Floresta':
        janela3 = janela_escolha()
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'Mel':
        janela12 = janela_consequencia5()
    if window == janela12 and event == 'Parar':
        break
    if window == janela12 and event == 'Jogar Novamente':
        janela1 = janela_entrada()

    if window == janela3 and event == 'Frutas Silvestres':
        janela4 = janela_consequencia2()
    if window == janela4 and event == sg.WIN_CLOSED:
        break

    if window == janela4 and event == 'Vizinho/Amigo':
        janela11 = janela_consequencia7()

    if window == janela11 and event == 'Parar':
        break
    if window == janela11 and event == 'Jogar Novamente':
        janela1 = janela_entrada()

    if window == janela4 and event == 'Vovó':
        janela10 = janela_escolha5()

    if window == janela10 and event == 'Jogar Novamante':
        janela1 = janela_entrada()

    if window == janela10 and event == 'Parar':
        break

    if window == janela10 and event == sg.WIN_CLOSED:
        break