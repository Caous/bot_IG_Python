
class Ocorrencia:
    """ Classe para determinar qual ocorrência irá efetuar"""
    def __init__(self : object,acao: int,usuarios: list,qtdLike : int , comentarioTempoReal: bool, comentarios: str = '', erros: int = 0, sucessos : int = 0) -> None:
        self.__acao = int = acao
        self.__usuarios = list = usuarios
        self.__qtdLikes = int = qtdLike
        self.__comentarios = srt = comentarios
        self.__erros = int = erros
        self.__sucessos = int = sucessos
        self.__comentarioTempoReal = bool = comentarioTempoReal

    @property
    def acao(self: object) -> int:
        return self.__acao

    @property
    def usuarios(self: object) -> list:
        return self.__usuarios

    @property
    def qtdLikes(self: object) -> int:
        return self.__qtdLikes

    @property
    def comentarios(self: object) -> str:
        return self.__comentarios

    @property
    def erro(self: object) -> int:
        return self.__erros

    @property
    def sucesso(self: object) -> int:
        return self.__sucessos

    @property
    def comentarioTempoReal(self:object) -> bool:
        return self.__comentarioTempoReal

    @property
    def setErro(self, erro: int) -> None:
        self.__erros = erro

    @property
    def setSucesso(self, sucesso: int) -> None:
        self.__sucessos = sucesso






    def __str__(self:object) -> str:
        return f'Model ocorrencia criada'