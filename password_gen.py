import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
                sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuario', size=(10, 1)),
                sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres', size=(20, 1)),
                sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]
        ]
        # Declarar janela
        self.janela = sg.Window('Hash Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self,valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXZabcdefghijklmnopqrstuvxz123456789!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        nova_senha = ''.join(chars)
        return nova_senha

    def salvar_senha(self, nova_senha, valores):
        with open('password.txt', 'a', newline='') as arquivo:
            arquivo.write(f"\nsite: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}")

        print('Arquivo salvo com sucesso')


gen = PassGen()
gen.Iniciar()
