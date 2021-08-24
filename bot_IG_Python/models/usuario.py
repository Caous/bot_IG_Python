
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    """ Classe principal para herança e instância de usuário"""
    def __init__(self : object,nome: str,usuario: str,senha: str,sistema : int, logado: bool = False) -> None:
        self.nome = srt = nome
        self.__usuario = srt = usuario
        self.__senha = srt = cryp.hash( senha, rounds=200000, salt_size=16)
        self.__logado = bool = logado
        self.sistema = int = sistema

    @property
    def usuario(self: object) -> str:
        return self.__usuario

    @property
    def senha(self: object) -> str:
        return self.__senha

    @property
    def logado(self: object) -> bool:
        return self.__logado

    @property
    def setLogado(self, logado: bool) -> None:
        self.__logado = logado

    def __str__(self:object) -> str:
        return f'Usuário criado com o nome: {self.nome} \nUsuário para login: {self.usuario}'

    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False