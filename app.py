# Imprimir varios arquivos diretamente

import win32print
import win32api
import os
import tkinter as tk
from tkinter import filedialog
import time

# Crie uma janela vazia (não exibida)
root = tk.Tk()
root.withdraw()

# Pedindo que o usuario selecione a impressora que deseja usar
lista_printers = win32print.EnumPrinters(2)
lista_printers: dict
cont = 1

print("### Lista de Impressoras ###")
print('\n')

for printer in lista_printers:
    lista = print(cont, "-", printer[1])
    cont += 1


while True:

    print('\n')
    impressora_user = input(
        'Digite o numero referente a impressora que deseja usar: ')
    print('\n')

    if impressora_user.isdigit() is False:
        print('🛑🛑🛑 Digite um numero Inteiro 🛑🛑🛑')

    elif int(impressora_user) not in range(1, cont, 1):
        print('🛑🛑🛑 Digite uma impressora valida 🛑🛑🛑')

    else:
        impressora = lista_printers[int(impressora_user)]
        print(f'Voce selecionou a impressora: {impressora}')

        win32print.SetDefaultPrinter(lista_printers[])

    # Abra o diálogo de seleção de pasta e armazene o caminho selecionado
    # print('Selecione uma pasta que deseje imprimir:')
    # time.sleep(1)
    # CAMINHO_PASTA = filedialog.askdirectory()

    # Certifique-se de que o usuário tenha selecionado uma pasta
    # if CAMINHO_PASTA:
    #     ...
    #     # Imprimindo os arquivos
    #     # lista_arquivos = os.listdir(CAMINHO_PASTA)

    #     # for arquivo in enumerate(lista_arquivos):
    #     #     # win32api.ShellExecute(0, "print", arquivo[1], '', CAMINHO_PASTA, 0)
    #     #     print(f'Impressão conluida n° {str(arquivo)}')

    # else:
    #     print("Nenhuma pasta selecionada")
