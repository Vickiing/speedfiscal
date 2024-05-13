"""
Criar classe Txt para referenciar arquivos do SPED Fiscal.
Proposito: Testar a modificação no sped, diretamente por atributo da classe Txt.
"""
arquivoTXT = r'SPED\EFD_1_5_100524_145101.TXT'

class Txt:
    def __init__(self, bloco=None):
        self.bloco = bloco


    def set_bloco(self, bloco):
        self.bloco =  bloco


    def ler_txt(self,bloco):
        with open(arquivoTXT, 'r') as txt:
            for linha in txt:
                valores = linha.strip().split('|')
                if bloco == valores[1]:
                    self.bloco = valores[1]
                    linha_inteira = valores
                    print(f'BLOCO: {self.bloco} - LINHA COMPLETA: {linha_inteira}')


    def contar_linhas_bloco(self, bloco):
    #precisa verificar se o resultado dessa função é consistente com o erro que o sped informou.
        self.bloco = bloco
        self.set_bloco(bloco)
        with open(arquivoTXT, 'r') as txt:
            for linha in txt:
                valores = linha.strip().split('|')
                if valores[1] == bloco:
                    valores[1] = txt.readlines()
                    print(len(valores))


    def __str__(self) -> str:
        return f'{self.bloco}'
    


efd = Txt()
efd.contar_linhas_bloco('E110')
#print(efd.bloco)
print(efd.ler_txt('E110'))
