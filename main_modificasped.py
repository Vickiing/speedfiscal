import pandas as pd

arquivo = r'C:\Users\vlsilva\Desktop\EFD_1_301_010224_173849 ret_nov.TXT'
planilha = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\NOTAS SEM CHAVE NOVEMBRO.19 OK.xlsx'

excel = pd.read_excel(planilha, index_col=False, sheet_name='Planilha1')
valor_nota = excel['Valor Contábil']
numero_nota = excel['Número NF']
chave_acesso = excel['Chave de Acesso']
planilha_concatenada = pd.concat([numero_nota, chave_acesso], axis=1)

def modifica_sped():
    #Função criada pra acessar o bloco C100 e inserir a chave de acesso no sped.
    arquivo_entrada = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\teste\EFD_1_301_010224_173849 ret_nov.TXT'
    arquivo_saida = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\teste\EFD_1_301_010224_173849 ret_nov - Modificado.TXT'
    print(f'Modificando sped para...: {arquivo_saida}')
    with open(arquivo_entrada, 'r', buffering=20000) as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            valores = linha.strip().split('|')
            if valores[1] == 'C100' and valores[9] == '':
                nota = int(valores[8])
                bloco = valores[1]
                modelo = '55'
                try:
                    #modifica chave de acesso
                    chave_correspondente = chave_acesso[planilha_concatenada[planilha_concatenada["Número NF"] == nota].index[0]]
                    valores[9] = chave_correspondente
                    valores[5] = modelo

                except IndexError:
                    valores[9] = ''
            linha_modificada = '|'.join(valores) + '\n'
            #resolve problema das linhas dos blocos 140 e 141 com base no valor contábil do arquivo excel
            if not ((valores[1] == 'C140' or valores[1] == 'C141') and valores[4] not in valor_nota.values):
                saida.write(linha_modificada)
            
    print('Modificação completada.')
            #print(f'Código: {bloco} - Nota: {nota} - Chave TXT: {valores[9]} - Chave Planilha: {chave_correspondente}')


def modifica_sped2():
    #criado pra testar as modificações do SPED, no bloco C180
    arquivo_entrada = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\EFD\EFD_1_5_140324_164545.TXT'
    arquivo_saida = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\EFD\EFD_MODIFICADO\EFD_1_5_140324_164545 - Modificado.TXT'
    print(f'Modificando arquivo sped para...: {arquivo_saida}')
    with open(arquivo_entrada, 'r', buffering=20000) as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            valores = linha.strip().split('|')
            if valores[1] == 'C180' and valores[7] == '':
                try:
                    #modifica os campos do bloco C180
                    valores[7] = '0'
                    valores[8] = '0'

                except IndexError:
                    valores[9] = ''

            linha_modificada = '|'.join(valores) + '\n'
            saida.write(linha_modificada)
    print('Modificação completada.')

#modifica_sped2()