# -*- coding: utf-8 -*-

import Tkinter as tk
from ScrolledText import ScrolledText
import requests

#URL da API e chave de autenticação
url = u'https://cacaudigital.azure-api.net/Loyalty.gateway.api/Cadastro/'
api_key = u'ECX3ykaPZvlkneCxPwZV74EmZXY6sFSDXXWsEf8LTFve-47PGhkwkX9Fw3nWwOtEjzvaphPBWalZgVNMEHvbLA'

#Função para consultar um CPF na API
def consultar_cpf():
    #Obtendo o CPF digitado pelo usuário
    cpf = entrada_cpf.get()

    #Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, u'Erro: CPF deve conter 11 dígitos.')
        return

    #URL da consulta
    consulta_url = url + cpf

    #Fazendo a solicitação GET com a chave de autenticação
    headers = {u'x-api-key': api_key}
    response = requests.get(consulta_url, headers=headers)

    #Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        #Se sim, retornamos os dados da resposta formatados conforme necessário
        dados = response.json()
        resultado_formatado = [
            (u'Nome', dados.get(u'nome', '')),
            (u'\nNível', dados.get(u'idNivel', '')),
            (u'\nDescrição do Nível', dados.get(u'descricaoNivel', '')),
            (u'\nPromoções', [{u'Código da Promoção': promocao.get(u'codigoRef', ''), 
                            u'Quantidade': promocao.get(u'quantidade', ''), 
                            u'ID Resgate para consulta no banco': promocao.get(u'idResgate', '')} 
                            for promocao in dados.get(u'promocoes', [])])
        ]
        exibir_resultado(resultado_formatado)
    else:
        #Se não, exibimos uma mensagem de erro
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, format(response.text))

#Função para exibir os resultados na tela
def exibir_resultado(resultado):
    #Limpando o texto anterior, se houver
    texto_resultado.delete(1.0, tk.END)

    #Adicionando os resultados à área de texto
    for chave, valor in resultado:
        if isinstance(valor, list):
            texto_resultado.insert(tk.END, u'{}:\n'.format(chave))
            for item in valor:
                texto_resultado.insert(tk.END, u'  Código da Promoção: {}\n'.format(item.get(u'Código da Promoção', '')))
                texto_resultado.insert(tk.END, u'  Quantidade: {}\n'.format(item.get(u'Quantidade', '')))
                texto_resultado.insert(tk.END, u'  ID Resgate para consulta no banco: {}\n'.format(item.get(u'ID Resgate para consulta no banco', '')))
                texto_resultado.insert(tk.END, u'\n')
        else:
            texto_resultado.insert(tk.END, u'{}: {}\n'.format(chave, valor))

#Criando a janela principal
janela = tk.Tk()
janela.title(u'Consulta de CPF')

#Criando uma entrada de texto para o usuário digitar o CPF
entrada_cpf = tk.Entry(janela)
entrada_cpf.grid(row=0, column=0, padx=5, pady=5)

#Botão para acionar a consulta
botao_consultar = tk.Button(janela, text=u'Consultar CPF', command=consultar_cpf)
botao_consultar.grid(row=0, column=1, padx=5, pady=5)

#Criando uma área de texto para exibir os resultados
texto_resultado = ScrolledText(janela, width=50, height=20)
texto_resultado.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

#Iniciando o loop principal da interface gráfica
janela.mainloop()
