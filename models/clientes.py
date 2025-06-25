class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
    
    #Nome
    def get_nome(self):
        return self._nome
    def set_nome(self, novo_nome):
        self._nome = novo_nome
    
    #CPF
    def get_cpf(self):
        return self._cpf
    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf
    
    #Telefone
    def get_telefone(self):
        return self._telefone
    def set_telefone(self, novo_telefone):
        self._telefone = novo_telefone
    
    #Email
    def get_email(self):
        return self._email
    def set_email(self, novo_email):
        self._email = novo_email