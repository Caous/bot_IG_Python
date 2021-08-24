
from models.usuario import Usuario
from models.ocorrencia import Ocorrencia

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstragamBot:

    def __init__(self,user:Usuario, ocorrencia: Ocorrencia):
        """Recuperando o driver para abrir o navegador (Firefox) e preechendo objetos"""
        self.user: Usuario = user
        self.ocorrencia : Ocorrencia = ocorrencia

        try:
            self.driver = webdriver.Firefox(executable_path="C:\\Users\\Public\\Documents\\Bot_Python\\geckodriver\\geckodriver.exe")
        except (FileNotFoundError) as err:
            print(f'Não foi possível encontrar o arquivos de execução do navegador FireFox, verifique o caminho '
                  f'\n Unable to find FireFox browser execution file, check path')

    def entrarIntagram(self):
        """Navegar/Abrir a página do instagram"""

        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        self.login()

    def login(self):
        """Método para logar no Instagram"""
        driver = self.driver

        """ Levando em conta que podemos logar no instagram de duas formas o usuário irá escolher uma com números e vamos recuperar o sistema desejado
            Tipo de autenticação
            Caso deseje logar via instagram"""

        if(self.user.sistema == 1):

            #Irá buscar o campo usuário para colocar o valor
            user_element = driver.find_element_by_xpath("//input[@name='username']")
            user_element.clear()

            # Preenchendo valor
            user_element.send_keys(self.user.usuario)

            # Irá buscar o campo senha para preencher
            pass_element = driver.find_element_by_xpath("//input[@name='password']")
            pass_element.clear()

            print(f"Por favor senhor(a) {self.user.nome} confirme sua senha novamente ela não será armezanada")
            confirma_senha = str(input("Informe sua senha: "))

            # Checa a senha para ver se está correta
            checa_senha = self.user.checa_senha(confirma_senha)

            if(checa_senha):
                # Preenchendo senha
                pass_element.send_keys(confirma_senha)
                pass_element.send_keys(Keys.RETURN)
                time.sleep(5)
            else:
                print(f'Por favor verificar senha novamente (senha incorreta)')
                senha_confirmar = str(input("Informe sua senha: "))
                checa_senha = self.user.checa_senha(senha_confirmar)
                if (checa_senha):
                    # Preenchendo senha
                    pass_element.send_keys(confirma_senha)
                    pass_element.send_keys(Keys.RETURN)
                    time.sleep(5)
                else:
                    print('Sua senha não está correta tente novamente mais tarde')
                    return

        elif(self.user.sistema == 2):

            # Caso deseje logar via facebook
            #irá clicar no link para logar no facebook
            driver.find_element_by_class_name('KPnG0').click()

            # Irá buscar o campo usuário para colocar o valor
            user_element = driver.find_element_by_xpath("//input[@name='email']")
            user_element.clear()

            # Preenchendo valor
            user_element.send_keys(self.user.usuario)

            # Irá buscar o campo senha para colocar o valor
            pass_element = driver.find_element_by_xpath("//input[@name='pass']")
            pass_element.clear()

            print(f"Por favor senhor(a) {self.user.nome} confirme sua senha novamente ela não será armezanada")
            confirma_senha = str(input("Informe sua senha: "))

            checa_senha = self.user.checa_senha(confirma_senha)

            if (checa_senha):
                # Preenchendo senha
                pass_element.send_keys(confirma_senha)
                pass_element.send_keys(Keys.RETURN)
                time.sleep(5)
            else:
                print(f'Por favor verificar senha novamente (senha incorreta)')
                senha_confirmar = str(input("Informe sua senha: "))
                checa_senha = self.user.checa_senha(senha_confirmar)
                if (checa_senha):
                    # Preenchendo senha
                    pass_element.send_keys(confirma_senha)
                    pass_element.send_keys(Keys.RETURN)
                    time.sleep(5)
                else:
                    print('Sua senha não está correta tente novamente mais tarde')
                    return

        self.menu()

    def menu(self):
        """Recupera qual ação o usuário que no sistema"""

        if (self.ocorrencia.acao == 1):
            "Caso queira explorar por hasttag"
            self.busca_por_hastag()

        elif (self.ocorrencia.acao == 2):
            "Caso queira explorar um perfil"
            self.busca_por_usuario()

    def busca_por_hastag(self,):

        for hastags in self.ocorrencia.usuarios:

            driver = self.driver

            #Acessa a url com a hastag que deseja
            driver.get('https://www.instagram.com/explore/tags/'+hastags+'/')
            time.sleep(5)


            #Executa script para rolar a pagina para baixo desta forma carregando as imagens
            for i in range(1, 3):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                #Para de executar o robô por 2 segundos para carregar as fotos
                time.sleep(2)

            item = 1

            #Loop para passar por todas fotos informadas pelo usuário (Quantidade de likes)
            while item <= self.ocorrencia.qtdLikes:

                try:
                 #Se for a primeira foto irá abrir e carregar a foto
                 if(item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()
                 time.sleep(3)

                 #Clica no botão do like
                 driver.find_element_by_class_name('fr66n').click()
                 time.sleep(1)

                #Caso tenha um comentário ele irá preencher o campo e clicar em comentar
                 if(self.ocorrencia.comentarios != ""):

                    #Clicando no campo do comentário
                    driver.find_element_by_class_name('Ypffh').click()
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(self.ocorrencia.comentario)

                    #Enviando comentário
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)
                 if(self.ocorrencia.comentarioTempoReal):
                     # Clicando no campo do comentário
                     comentario = str(input("Informe o comentário: "))
                     driver.find_element_by_class_name('Ypffh').click()
                     field = driver.find_element_by_class_name('Ypffh')
                     field.clear()
                     field.send_keys(comentario)

                     # Enviando comentário
                     driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                     time.sleep(9)

                #Passa para o a próxima foto
                 driver.find_element_by_class_name(
                     'coreSpriteRightPaginationArrow').click()  # click on next photo button
                 item = item + 1

                except:
                 time.sleep(60)  # if connection errors occur
                 #self.ocorrencia.setErro(item)
            #self.ocorrencia.setSucesso(item)
            print(f'Número de fotos curtidas e comentadas: \033[0;33m{item - 1}\033[m')

    def busca_por_usuario(self):



        driver = self.driver

        for usuario in self.ocorrencia.usuarios:
            # Acessa a url com o perfil que deseja
            driver.get('https://www.instagram.com/'+ usuario+'/')
            time.sleep(5)

            #Executa script para rolar a pagina para baixo desta forma carregando as imagens
            for i in range(1, 3):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            # Para de executar o robô por 2 segundos para carregar as fotos
            time.sleep(2)

            #Vai tentar seguir o perfil informado porque as vezes você já segue o perfil, então não vai conseguir seguir
            try:
                driver.find_element_by_xpath('//button[contains(text(), "Seguir")]').click()
                time.sleep(3)
            except:
                time.sleep(2)

            item = 1

            # Loop para passar por todas fotos informadas pelo usuário (Quantidade de likes)
            while item <= self.ocorrencia.qtdLikes:

                try:
                # Se for a primeira foto irá abrir e carregar a foto
                    if (item == 1):
                        driver.find_element_by_class_name('v1Nh3').click()  # click on photo to open and upload
                    time.sleep(3)

                # Clica no botão do like
                    driver.find_element_by_class_name('fr66n').click()  # click the like button
                    time.sleep(1)

                # Caso tenha um comentário ele irá preencher o campo e clicar em comentar
                    if (self.ocorrencia.comentarios != ""):
                        # Clicando no campo do comentário
                        driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                        field = driver.find_element_by_class_name('Ypffh')
                        field.clear()
                        field.send_keys(self.ocorrencia.comentarios)

                        #Enviando comentário
                        driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                        time.sleep(9)
                    if (self.ocorrencia.comentarioTempoReal):
                    # Clicando no campo do comentário
                        driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                        field = driver.find_element_by_class_name('Ypffh')
                        field.clear()
                        field.send_keys(self.ocorrencia.comentarios)

                    # Enviando comentário
                        driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                        time.sleep(9)

                # Passa para o a próxima foto
                    driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()  # click on next photo button
                    item = item + 1

                except:
                    time.sleep(60)  # if connection errors occur
                    #self.ocorrencia.setErro(item)
        #self.ocorrencia.setSucesso(item)
        print(f'Número de fotos curtidas e comentadas: \033[0;33m{item - 1}\033[m')
