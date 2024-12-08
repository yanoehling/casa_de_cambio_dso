from abstratas.absTela import Tela
from funcoes import *
from excecoes import *
import PySimpleGUI as sg

from funcoes import eh_numerico

class TelaCliente(Tela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        
    def init_opcoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Radio("1 - Ver dados de um Cliente", "RD_cliente", key='1')],
            [sg.Radio("2 - Adicionar Cliente", "RD_cliente", key='2')],
            [sg.Radio("3 - Excluir Cliente", "RD_cliente", key='3')],
            [sg.Radio("4 - Listar todos Clientes", "RD_cliente", key='4')],
            [sg.Radio("5 - Alterar Cliente", "RD_cliente", key='5')],
            [sg.Radio("6 - Ver Transações de um Cliente", "RD_cliente", key='6')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CLIENTES").Layout(layout)

    
    def tela_opcoes(self):
        self.init_opcoes()
        botao, valores = self.open()
        opcao = 0
        if valores['1']:
            opcao = 1
        if valores['2']:
            opcao = 2
        if valores['3']:
            opcao = 3
        if valores['4']:
            opcao = 4
        if valores['5']:
            opcao = 5
        if valores['6']:
            opcao = 6
        if botao in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao


    def cadastrar_dados(self):
        layout = [ 
            [sg.Text('--------CADASTRAR INFORMAÇÕES DO CLIENTE--------')],
            [sg.Radio('1 - Cadastrar Pessoa Física', 'cli', key='1')],
            [sg.Radio('2 - Cadastrar Empresa/Organização', 'cli', key='2')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        nome, id = valores['nome'], valores['id']

        layout = [
            [sg.Text(f'NOME: '), sg.InputText('', key='nome')],
            [sg.Text(f'IDENTIDADE (cpf/cpnj): '), sg.InputText('', key='id')],
        ]
        pessoa = False
        if valores['1']:
            layout.append([sg.Text(f'IDADE: '), sg.InputText('', key='idade')])
            pessoa = True

        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        nome, id = valores['nome'], valores['id']
        if pessoa:
            idade = valores['idade']
        self.close()

        corretos = True
        for char in nome:
            if char.isnumeric() and pessoa:
                corretos = False
                raise NomeComNumero('pessoa')
        for char in id:
            if not char.isnumeric():
                corretos = False
                raise ComCaractere('identidade')
        if pessoa and not isinstance(idade, int):
            corretos = False
            raise NaoInteiro('idade')
        if corretos:
            lista = {"nome": nome, "id": id}
            if pessoa:
                lista["idade"] = idade
            return lista 


    def alterar_dados(self):
        sg.change_look_and_feel('DarkYellow')
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja alterar: '), sg.InputText('', key='nome')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id']):
            return valores['id']
    
    def mostrar_dados(self, dados_cliente):
        infos = f"""--------INFORMAÇÕES DO CLIENTE--------
NOME: {dados_cliente["nome"]}
ID: {dados_cliente["id"]}
"""
        if "idade" in dados_cliente:
            infos += f'IDADE: {dados_cliente["idade"]}'
        infos += '\n'

        sg.Popup(infos)

    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id']):
            return valores['id']
    
    def ver_transacoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja ver as transações: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id']):
            return valores['id']

    def ver_dados(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja achar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id']):
            return valores['id']
    
    def mostrar_msg(self, msg):
        super().mostrar_msg(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        botao, valores = self.__window.Read()
        return botao, valores
