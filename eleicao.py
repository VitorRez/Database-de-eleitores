import csv

class eleicao():

    def __init__(self, nome, cpf, unidade, validade):
        self.nome = nome
        self.cpf = cpf
        self.unidade = unidade
        self.validade = validade


class eleitor(eleicao):

    def __init__(self, nome, cpf, unidade, chave_pub, validade, datai, dataf, horai, horaf):
        super().__init__(nome, cpf, unidade, validade)
        self.chave_pub = chave_pub
        self.datai = datai
        self.dataf = dataf
        self.horai = horai
        self.horaf = horaf

class candidato(eleicao):

    def __init__(self, nome, cpf, unidade, validade, num_votos):
        super().__init__(nome, cpf, unidade, validade)
        self.num_votos = num_votos

def readDB_c(filename, cand_list):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == 1:
                nome = linha['Nome']
                cpf = linha['cpf']
                unidade = linha['unidade']
                validade = linha['unidade']
                num_votos = linha['num_votos']
                c = candidato(nome, cpf, unidade, validade, num_votos)
                cand_list.append(c)

def validator_e(filename, nome, cpf, unidade):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == 0 and linha['validade'] == 1 and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    e = eleitor(linha['nome'], linha['cpf'], linha['unidade'], linha['chave_pub'], linha['validade'], linha['datai'], linha['dataf'], linha['horai'], linha['horaf'])
                    return e



            



