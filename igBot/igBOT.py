from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstragamBot:
    def __init__(self):
        username = str(input('Informe usuário ou e-mail de login: '))  # hashtag
        password = str(input('Informe senha de login: '))  # amount of photos to like

        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Gustavo Nascimento\\Desktop\\geckodriver\\geckodriver.exe")


    def entrarIntagram(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        self.login()

    def login(self):
        driver = self.driver

        print("Você deseja entrar com uma conta direta do instragram ou via facebook")
        print("(1) - Instagram"
              "(2) - Facebook")
        tipAutentic = str(input('Sistema: '))  # hashtag

        if(tipAutentic == "1"):
            user_element = driver.find_element_by_xpath("//input[@name='username']")
            user_element.clear()
            user_element.send_keys(self.username)
            pass_element = driver.find_element_by_xpath("//input[@name='password']")
            pass_element.clear()
            pass_element.send_keys(self.password)
            pass_element.send_keys(Keys.RETURN)
            time.sleep(5)
        else:
            driver.find_element_by_class_name('KPnG0').click()
            user_element = driver.find_element_by_xpath("//input[@name='email']")
            user_element.clear()
            user_element.send_keys(self.username)
            pass_element = driver.find_element_by_xpath("//input[@name='pass']")
            pass_element.clear()
            pass_element.send_keys(self.password)
            pass_element.send_keys(Keys.RETURN)
            time.sleep(5)


        self.menu()




    def menu(self):
        print("Por favor informar com os números o sistema desejado")
        print("(1) - Hastag"
              "(2) - Perfil"
              "(3) - Comentar perfil em tempo real")
        capHastPerfil = str(input('Sistema: '))  # hashtag

        if (capHastPerfil == "1"):
            hashtag = str(input('Informe á Hashtag: '))  # hashtag
            likes = int(input('Informe á quantidade de Likes: '))  # amount of photos to like
            comment = str(input('Informe o comentário desejado: '))  # comment in photo
            self.searchHastg(hashtag, likes, comment)
        if (capHastPerfil == "2"):
            perfil = str(input('O perfil: '))  # hashtag
            likes = int(input('Informe á quantidade de Likes: '))  # amount of photos to like
            comment = str(input('Informe o comentário desejado: '))  # comment in photo
            self.curtir(perfil, likes, comment)
        if (capHastPerfil == "3"):
            perfil = str(input('O perfil: '))  # hashtag
            likes = int(input('Informe á quantidade de Likes: '))  # amount of photos to like
            self.curtirCommentTimeReal(perfil, likes)

    def searchHastg(self, _hastag,likes=1, comment=''):

         driver = self.driver
         driver.get('https://www.instagram.com/explore/tags/'+_hastag+'/')
         time.sleep(5)



         for i in range(1, 3):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)

         item = 1

         while item <= likes: # loop with how many photos to like

             try:
                 if(item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()  # click on photo to open and upload
                 time.sleep(3)
                 driver.find_element_by_class_name('fr66n').click()  # click the like button
                 time.sleep(1)

                 if(comment != ""):
                    driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                 driver.find_element_by_class_name(
                     'coreSpriteRightPaginationArrow').click()  # click on next photo button
                 item = item + 1
             except:
                 time.sleep(60)  # if connection errors occur

         print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
         self.menu()



    def curtir(self, usuario,likes=1, comment=''):
        driver = self.driver
        driver.get('https://www.instagram.com/'+ usuario+'/')
        time.sleep(5)

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)

        try:
            driver.find_element_by_xpath('//button[contains(text(), "Seguir")]').click()
            time.sleep(3)
        except:
            time.sleep(2)

        item = 1

        while item <= likes:  # loop with how many photos to like

            try:
                if (item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()  # click on photo to open and upload
                time.sleep(3)
                driver.find_element_by_class_name('fr66n').click()  # click the like button
                time.sleep(1)

                if (comment != ""):
                    driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()  # click on next photo button
                item = item + 1
            except:
                time.sleep(60)  # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
        self.menu()

        #hrefs = driver.find_elements_by_tag_name('a');
        #pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #[href for href in pic_hrefs if usuario in href]


        #for pic_href in pic_hrefs:
        #    driver.get(pic_href)
        #    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #    time.sleep(5)
        #    try:
        #        driver.find_element_by_class_name('fr66n').click()  # click on photo to open and upload


        #        time.sleep(20)
        #    except Exception as e:
        #        time.sleep(5)

    def curtirCommentTimeReal(self, usuario,likes=1):
        driver = self.driver
        driver.get('https://www.instagram.com/'+ usuario+'/')
        time.sleep(5)

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)

        item = 1

        try:
            driver.find_element_by_xpath('//button[contains(text(), "Seguir")]').click()
            time.sleep(3)
        except:
            time.sleep(2)

        while item <= likes:  # loop with how many photos to like

            try:
                if (item == 1):
                    driver.find_element_by_class_name('v1Nh3').click()  # click on photo to open and upload
                time.sleep(3)
                driver.find_element_by_class_name('fr66n').click()  # click the like button
                time.sleep(1)
                description = driver.find_element_by_xpath("//div[@class='C4VMK']")
                print(description.text)

                #description = driver.find_elements_by_class_name("C4VMK")


                #print(description.text)

                comment = str(input('Informe o comentário desejado: '))  # comment in photo
                if (comment != ""):
                    driver.find_element_by_class_name('Ypffh').click()  # click the field to insert comment
                    field = driver.find_element_by_class_name('Ypffh')
                    field.clear()
                    field.send_keys(comment)
                    driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
                    time.sleep(9)

                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()  # click on next photo button
                item = item + 1
            except:
                time.sleep(60)  # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')
        self.menu()





#starRobo = InstragamBot('lunaleopoldo2020', 'joca1826')
#starRobo = InstragamBot('gustavosn2000@hotmail.com', 'gugusn200')
starRobo = InstragamBot()
starRobo.entrarIntagram()