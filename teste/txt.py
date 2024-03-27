"""
Criar classe Txt para referenciar arquivos do SPED Fiscal.
Proposito: Testar a modificação no sped, diretamente por atributo da classe Txt.
"""
arquivoTXT = r'C:\Users\vlsilva\Documents\PYTHON PROJETOS\fiscal\speedfiscal\teste\EFD_1_301_010224_173849 ret_nov.TXT'

class Txt:
    def __init__(self, bloco=None):
        self.bloco = bloco
    
    def ler_txt(self,bloco):
        with open(arquivoTXT, 'r') as txt:
            for linha in txt:
                valores = linha.strip().split('|')
                if bloco == valores[1]:
                    self.bloco = valores[1]
                    linha_inteira = valores
                    #print(f'BLOCO: {self.bloco} - LINHA COMPLETA: {linha_inteira}')
            

    def contar_linhas_bloco(self, bloco):
    #precisa verificar se o resultado dessa função é consistente com o erro que o sped informo.
        self.bloco = bloco
        with open(arquivoTXT, 'r') as txt:
            for linha in txt:
                valores = linha.strip().split('|')
                if valores[1] == bloco:
                    valores[1] = txt.readlines()
                    print(len(valores[1]))



    def __str__(self) -> str:
        return f'{self.bloco}'
    

    
efd = Txt()
efd.contar_linhas_bloco('C110')

