import csv
from Crypto.PublicKey import RSA

#classe para armazenar todos os dados do .csv
class eleicao():

    def __init__(self, nome, cpf, unidade, chave_pub, validade, candidato, data, horai, horaf):
        self.nome = nome
        self.cpf = cpf
        self.unidade = unidade
        self.chave_pub = chave_pub
        self.validade = validade 
        self.candidato = candidato
        self.data = data
        self.horai = horai
        self.horaf = horaf

#le de um arquivo .csv e lista todas as pessoas cadastradas como candidatos
def readDB(filename, cand_list):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == "1":
                e = eleicao(linha['nome'], linha['cpf'], linha['unidade'], linha['chave_pub'], linha['validade'], linha['candidato'], linha['data'], linha['horai'], linha['horaf'])
                cand_list.append(e)

#altera o arquivo .csv quando algum dado for alterado (chave publica, validade, etc)
#não consegui implementar ainda uma forma de fazer isso sem armazenar todos os dados do arquivo, logo, trecho sujeito a mudanças
def writeDB(filename, e_list):
    
    with open(filename, "w+") as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow(['nome','cpf','unidade','chave_pub','validade','candidato','data','horai','horaf','num_votos'])
        for i in e_list:
            escreve_csv.writerow([i.nome, i.cpf, i.unidade, i.chave_pub, i.validade, i.candidato, i.data, i.horai, i.horaf])

#verifica se o individuo é um eleitor válido (não está votando uma segunda vez, vota naquela "unidade" e possui nome e cpf válido)
#se o eleitor for válido, é gerada uma chave publica de RSA, exportada no formato PEM
#ao final altera o arquivo .csv
def validator_e(filename, nome, cpf, unidade):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        e = None
        e_list = []
        for linha in leitor_csv:
            if linha['candidato'] == '0' and linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    chave = RSA.generate(2048)
                    linha['chave_pub'] = chave.publickey().exportKey("PEM")
                    linha['validade'] = 0
                    e = eleicao(linha['nome'], linha['cpf'], linha['unidade'], linha['chave_pub'], linha['validade'], linha['candidato'], linha['data'], linha['horai'], linha['horaf'])
            e_geral = eleicao(linha['nome'], linha['cpf'], linha['unidade'], linha['chave_pub'], linha['validade'], linha['candidato'], linha['data'], linha['horai'], linha['horaf'])
            e_list.append(e_geral)

    writeDB(filename, e_list)
    return e

cand_list = []
readDB("teste.csv", cand_list)
for i in cand_list:
    print(i.nome)
i = 1
while i == 1:
    nome = input()
    cpf = input()
    unidade = input()
    e = validator_e("teste.csv", nome, cpf, unidade)
    print(e.nome)
    i = int(input())






            



