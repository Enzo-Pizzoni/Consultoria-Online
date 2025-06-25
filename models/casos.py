class Casos:
    def __init__(self, texto_cliente, retorno_gpt, tipo_caso):
        self._texto_cliente = texto_cliente
        self._retorno_gpt = retorno_gpt
        self._tipo_caso = tipo_caso
    
    #Texto Cliente
    def get_texto_cliente(self):
        return self._texto_cliente
    def set_texto_cliente(self, novo_texto):
        self._texto_cliente = novo_texto
    
    #Retorno do Chat GPT
    def get_retorno_gpt(self):
        return self._retorno_gpt
    def set_retorno_gpt(self, novo_retorno):
        self._retorno_gpt = novo_retorno
    
    #Tipo de caso
    def get_tipo_caso(self):
        return self._tipo_caso
    def set_tipo_caso(self, novo_tipo):
        self._tipo_caso = novo_tipo