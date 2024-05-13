import sys
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


dados = {
    'Loja': [],
    'Valor_ICMS': [],
    'Valor_FECP': []
}




def func_verificaST(arquivo_sped):
    
    loja = None
    icms = None
    fecp = None

    with open(arquivo_sped, 'r') as sped:
        for linha in sped:
            valores = linha.strip().split('|')

            if valores[1] == '0000':
                loja = valores[6]

            if valores[1] == 'E250' and valores[2] == '001' and valores[4] == '31052024' and valores[5] == '0230':
                icms = valores[3]

            if valores[1] == 'E250' and valores[2] == '006' and valores[4] == '31052024' and valores[5] == '7501':
                fecp = valores[3]

    dados['Loja'].append(loja)
    dados['Valor_ICMS'].append(icms)
    dados['Valor_FECP'].append(fecp)


caminho_base = r'SPED/'
arquivo = os.listdir(caminho_base)
caminho_completo = [os.path.join(caminho_base, arquivo) for arquivo in arquivo]


def criar_df():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(func_verificaST, caminho_completo))

    df = pd.DataFrame(dados)
    return df

def executar():
    dataframe = criar_df()
    dataframe.fillna(0, inplace=True)
    print(dataframe.sort_values(by='Loja'))

executar()