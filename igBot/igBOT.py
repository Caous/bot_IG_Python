from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstragamBot:

    def __init__(self):
        #Pegar o usuário de login do Instagram
        username = str(input('Informe usuário ou e-mail de login: '))

        # Pegar a senha do login do Instagram
        password = str(input('Informe senha de login: '))

        #Declarando variáveis para recuperar
        #Variável Usuário
        self.username = username
        # Variável Senha
        self.password = password
        #Recuperando o driver para abrir o navegador (Firefox)
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Public\\Documents\\Bot_Python\\geckodriver\\geckodriver.exe")

    def entrarIntagram(self):
        #Navegar/Abrir a página do instagram
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        self.login()

    def login(self):
        #método para logar no Instagram
        driver = self.driver

        #Levando em conta que podemos logar no instagram de duas formas o usuário irá escolher uma com números e vamos recuperar o sistema desejado
        print("Você deseja entrar com uma conta direta do instragram ou via facebook")
        print("(1) - Instagram"
              "(2) - Facebook")

        #Tipo de autenticação
        tipAutentic = str(input('Sistema: '))  # hashtag

        #Caso deseje logar via instagram
        if(tipAutentic == "1"):
            #Irá buscar o campo usuário para colocar o valor
            user_element = driver.find_element_by_xpath("//input[@name='username']")
            user_element.clear()

            #Usuário colocando o valor
            user_element.send_keys(self.username)

            # Irá buscar o campo senha para preencher
            pass_element = driver.find_element_by_xpath("//input[@name='password']")
            pass_element.clear()
            # Senha colocando o valor
            pass_element.send_keys(self.password)
            pass_element.send_keys(Keys.RETURN)
            time.sleep(5)
        else:
        # Caso deseje logar via facebook
            #irá clicar no link para logar no facebook
            driver.find_element_by_class_name('KPnG0').click()
        # Irá buscar o campo usuário para colocar o valor
            user_element = driver.find_element_by_xpath("//input[@name='email']")
            user_element.clear()
        # Usuário colocando o valor
            user_element.send_keys(self.username)
        # Irá buscar o campo senha para colocar o valor
            pass_element = driver.find_element_by_xpath("//input[@name='pass']")
            pass_element.clear()
        # Senha colocando o valor
            pass_element.send_keys(self.password)
            pass_element.send_keys(Keys.RETURN)
            time.sleep(5)

        #Irá selecionar o menu a informação que o usuário quer fazer no sistema
        self.menu()

    def menu(self):
        # Recupera qual ação o usuário que no sistema
        print("Por favor informar com os números o sistema desejado")
        print("(1) - Hastag"
              "(2) - Perfil"
              "(3) - Comentar perfil em tempo real")

        # Recupera o sistema que selecionou
        capHastPerfil = str(input('Sistema: '))  # hashtag

        #Caso queira explorar hastag
        if (capHastPerfil == "1"):
            #Recupera a hastag que deseja explorar
            hashtag = str(input('Informe á Hashtag: '))

            # Recupera a quantidade de like que quer dar no IG
            likes = int(input('Informe á quantidade de Likes: '))

            # Recupera um comentário geral para todas fotos
            comment = str(input('Informe o comentário desejado: '))

            self.searchHastg(hashtag, likes, comment)

        # Caso queira explorar um perfil
        if (capHastPerfil == "2"):
            # Recupera o perfil que deseja explorar
            perfil = str(input('O perfil: '))  # hashtag

            # Recupera a quantidade de like que quer dar no IG
            likes = int(input('Informe á quantidade de Likes: '))

            # Recupera um comentário geral para todas fotos
            comment = str(input('Informe o comentário desejado: '))

            self.curtir(perfil, likes, comment)

        # Caso queira explorar um perfil e comentar em tempo real
        if (capHastPerfil == "3"):
            # Recupera o perfil que deseja explorar
            perfil = str(input('O perfil: '))  # hashtag

            # Recupera a quantidade de like que quer dar no IG
            likes = int(input('Informe á quantidade de Likes: '))  # amount of photos to like

            self.curtirCommentTimeReal(perfil, likes)

    def searchHastg(self, _hastag,likes=1, comment=''):

         driver = self.driver
         #Acessa a url com a hastag que deseja
         driver.get('https://www.instagram.com/explore/tags/'+_hastag+'/')
         time.sleep(5)


         #Executa um script para rolar a pagina abaixo desta forma carregando as imagens
         for i in range(1, 3):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                #Para de executar o robô por 2 segundos para carregar as fotos
                time.sleep(2)

         item = 1

        #Loop para passar por todas fotos informadas pelo usuário (Quantidade de likes)
         while item <= likes:

             try:
                 #Se for a primeira foto irá abrir e carregar a foto
                 if(item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()
                 time.sleep(3)

                 #Clica no botão do like
                 driver.find_element_by_class_name('fr66n').click()
                 time.sleep(1)

                #Caso tenha um comentário ele irá preencher o campo e clicar em comentar
                 if(comment != ""):

                    #Clicando no campo do comentário
                    driver.find_element_by_class_name('Ypffh').click()
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)

                    #Enviando comentário
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                #Passa para o a próxima foto
                 driver.find_element_by_class_name(
                     'coreSpriteRightPaginationArrow').click()  # click on next photo button
                 item = item + 1
             except:
                 time.sleep(60)  # if connection errors occur

         print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
         self.menu()

    def curtir(self, usuario,likes=1, comment=''):

        driver = self.driver
        # Acessa a url com o perfil que deseja
        driver.get('https://www.instagram.com/'+ usuario+'/')
        time.sleep(5)

        # Executa um script para rolar a pagina abaixo desta forma carregando as imagens
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
        while item <= likes:

            try:
                # Se for a primeira foto irá abrir e carregar a foto
                if (item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()  # click on photo to open and upload
                time.sleep(3)

                # Clica no botão do like
                driver.find_element_by_class_name('fr66n').click()  # click the like button
                time.sleep(1)

                # Caso tenha um comentário ele irá preencher o campo e clicar em comentar
                if (comment != ""):
                    # Clicando no campo do comentário
                    driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)

                    #Enviando comentário
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                # Passa para o a próxima foto
                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()  # click on next photo button
                item = item + 1
            except:
                time.sleep(60)  # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
        self.menu()

    def curtirCommentTimeReal(self, usuario,likes=1):

        driver = self.driver
        # Acessa a url com o perfil que deseja
        driver.get('https://www.instagram.com/'+ usuario+'/')
        time.sleep(5)

        # Executa um script para rolar a pagina abaixo desta forma carregando as imagens
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)

        item = 1

        # Vai tentar seguir o perfil informado porque as vezes você já segue o perfil, então não vai conseguir seguir
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Seguir")]').click()
            time.sleep(3)
        except:
            time.sleep(2)

        # Loop para passar por todas fotos informadas pelo usuário (Quantidade de likes)
        while item <= likes:

            try:
                # Se for a primeira foto irá abrir e carregar a foto
                if (item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()
                time.sleep(3)

                # Clica no botão do like
                driver.find_element_by_class_name('fr66n').click()
                time.sleep(1)

                #Irá carregar no console qual a descrição da foto da pessoa
                description = driver.find_element_by_xpath("//div[@class='C4VMK']")
                print(description.text)

                #O usuário informa o comentário em tempo real após ler a descrição
                comment = str(input('Informe o comentário desejado: '))
                if (comment != ""):
                    driver.find_element_by_class_name('Ypffh').click()
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)

                    #Enviando comentário
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                # Passa para o a próxima foto
                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()  # click on next photo button
                item = item + 1
            except:
                time.sleep(60)  # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
        self.menu()

#Iniciar a classe do robô
starRobo = InstragamBot()
#Chamando o robô
starRobo.entrarIntagram()