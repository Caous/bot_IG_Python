from models.usuario import Usuario
from models.ocorrencia import Ocorrencia
from service.raspagemService import InstragamBot

nome = str(input('Informe seu nome: '))
usuario = str(input('Informe seu usuário ou e-mail de login: '))
senha = str(input('Informe sua senha de login: '))
sistema = int(input('Você efetua login no instagram por qual plataforma? \n1 - Instagram \n2 - Facebook'))

user = Usuario(nome =nome,usuario = usuario, senha = senha,sistema = sistema)

print(user.__doc__)
print(user)
print(f'Logado: {user.logado}')

try:
    acao = int(input('Por favor selecione com números qual operação deseja: \n1 - Hastag \n2 - Perfil\n'))
except (ValueError) as err:
    print('Ocorreu um erro com o valor inseridor verifica se o valor informado era númerico')

try:
    qtdLike = int(input('Por favor informe a quantidade de likes: '))
except (ValueError) as err:
    print('Ocorreu um erro com o valor inseridor verifica se o valor informado era númerico')

comentario = str(input('Por favor inserir o comentário desejado: '))

print(f'Por favor informas todas #Hastags que deseja ou perfis que deseja \nQuando desejar sair só escrever sair')

usuarios = []


while usuario != 'sair':
    usuario = input('Informar usuario ou hastag: ')
    if(usuario != 'sair'):
        usuarios.append(usuario)

print(f'Você deseja comentar as fotos/vídeos em tempo real?\n0 - Não \n1 - Sim')
comentarioTempoReal = int(input('Informe o número desejado: '))


ocorrencia = Ocorrencia(acao,usuarios,qtdLike,bool(comentarioTempoReal),comentario)

print(ocorrencia.qtdLikes)

print(ocorrencia)

print("Iniciando chamada do robô")

serviceApp = InstragamBot(user=user,ocorrencia=ocorrencia)

serviceApp.entrarIntagram()

print(f"Foram processado {ocorrencia.sucesso} e quantidade de erros: {ocorrencia.erro}")

print("Robô finalizado com sucesso")










