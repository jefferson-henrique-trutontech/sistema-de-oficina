import PySimpleGUI as sg


def cadastrar():
    def cadastrar_produtos():
        layout = [
            [sg.Text('CADASTRO DE PRODUTOS', expand_x=True,
                     justification='center')],
            [sg.Radio('Peça', 'tipo_produto', True, enable_events=True), sg.Radio(
                'Serviço', 'tipo_produto', enable_events=True)],
            [sg.Text('Nome'), sg.Input(size=(20))],
            [sg.Text('Valor'), sg.Input(size=(7))]
        ]

        window = sg.Window('CADASTRAR PRODUTOS', layout)

        while True:
            ev, vl = window.read()

            if ev == sg.WIN_CLOSED:
                break
            elif vl[0] == True:  # TIPO PEÇA
                print('peça')
            elif vl[0] == False:  # TIPO SERVIÇO
                print('serviço')

    layout = [
        [sg.Text('SISTEMA DE CADASTRO', expand_x=True, justification='c')],
        [sg.Button('Produtos'), sg.Button(
            'Clientes'), sg.Button('Funcionários')]
    ]
    window = sg.Window('CADASTRAR', layout)
    while True:
        ev, vl = window.read()
        if ev == sg.WIN_CLOSED:
            break
        if ev == 'Produtos':
            cadastrar_produtos()


cadastrar()
