import csv

#Exemplo de classe com possíveis atributos para o eleitor, sujeito a mudanças
class eleitor():
    
    def __init__(self, nome, chave, cpf):
        self.nome = nome
        self.chave = chave
        self.cpf = cpf
    
#Método para obter eleitores do arquivo .csv e armazenalos numa lista do objeto eleitor
def readDB(filename, e_list):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            nome = linha['Nome']
            chave = linha['chave-pub']
            cpf = linha['cpf']
            e = eleitor(nome, chave, cpf)
            e_list.append(e)

#metodo para pegar os eleitores de uma lista e armazená-los num arquivo .csv
def writeDB(filename, e_list):

    with open(filename, 'w') as novo_arquivo:

        escreve_csv = csv.writer(novo_arquivo, delimiter='\t')
        escreve_csv.writerow(['Nome', 'chave-pub', 'cpf'])

        for i in e_list:
            escreve_csv.writerow([i.nome, i.chave, i.cpf])

e_list = []
readDB("teste.csv", e_list)
writeDB("novo_teste.csv", e_list)




