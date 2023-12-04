# Imprimir varios arquivos diretamente

from win32 import win32print
from win32 import win32api
import os
import PyPDF2

# Definindo o caminho de impressão
CAMINHO_ARQUIVO = r"C:\Users\Tecnologia\Desktop\Python\Projeto Impressão\Imprimir"
CAMINHO_NOVO = r"C:\Users\Tecnologia\Desktop\Python\Projeto Impressão\Imprimir_novo"


# Função para remover de determinado numero de paginas do PDF
def selecionar_paginas(pdf_path, output_dir, numero_paginas):
    # Abra o arquivo PDF original em modo de leitura binária
    with open(pdf_path, 'rb') as pdf_file:
        # Crie um objeto PDFReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Crie um objeto PDFWriter para o novo PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Determine o número total de páginas no PDF
        num_paginas = len(pdf_reader.pages)

        # Adicione a primeira pagina ao novo PDF
        for pagina in pdf_reader.pages[:numero_paginas]:
            pdf_writer.add_page(pagina)

         # Crie um novo arquivo PDF para escrever o resultado no diretório de destino
        novo_pdf_name = os.path.splitext(os.path.basename(pdf_path))[
            0] + '_primeira_pagina.pdf'
        novo_pdf_path = os.path.join(output_dir, novo_pdf_name)

        with open(novo_pdf_path, 'wb') as novo_pdf_file:
            pdf_writer.write(novo_pdf_file)


# Itere sobre todos os arquivos PDF na pasta de origem e seleciona a primeira pagina
for arquivo in os.listdir(CAMINHO_ARQUIVO):
    if arquivo.endswith('.pdf'):
        pdf_path = os.path.join(CAMINHO_ARQUIVO, arquivo)
        selecionar_paginas(pdf_path, CAMINHO_NOVO, 1)


# Listando as impressoras disponiveis:
lista_printers = win32print.EnumPrinters(2)

for i, printer in enumerate(lista_printers):
    print(i, printer)

print('\n')
menu_impressora = input('Digite o numero da impressora desejada: ')
print('\n')

if menu_impressora.isdigit() == True:

    digito_impressora = int(menu_impressora)

    # escolhendo a impressora padrão
    impressora = lista_printers[digito_impressora]
    win32print.SetDefaultPrinter(impressora[2])

    # Imprimindo os arquivos
    lista_arquivos = os.listdir(CAMINHO_NOVO)

    for i, arquivo in enumerate(lista_arquivos):
        print(arquivo)
        win32api.ShellExecute(0, "print", arquivo, '', CAMINHO_NOVO, 0)
        print(f'Impressão conluida n° {str(arquivo)}')

else:
    print('Digite um numero inteiro')
