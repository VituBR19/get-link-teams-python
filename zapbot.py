from selenium import webdriver
from avabot import AvaBot
import selenium
import time
import datetime

class ZapzapBot:
  def __init__ (self):    
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    
    self.login = input('Digite seu RA: ')
    self.pwd = input('Digite sua senha: ')
    
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    self.avabot = AvaBot(self.driver, self.login, self.pwd)
    
    self.mensagem = self.avabot.GetTeamsLink()

    self.WatchChatForCommandLink()

  def WatchChatForCommandLink(self):
    self.driver.get('https://web.whatsapp.com/')
    time.sleep(10)

    # ADS TURMA - GTADS1AN

    goToGrupo = self.driver.find_element_by_xpath("//span[@title='Teste de bot']")
    goToGrupo.click()

    grupo = self.driver.find_element_by_xpath("//span[@title='Teste de bot']").find_element_by_xpath('../../../..')
    
    while( True ):
      chat = grupo.find_elements_by_class_name('_3ko75')
      
      print('waiting for link command...')
      
      if(chat[1].text == '!link'):
        self.EnviarMensagem()

      time.sleep(3)

  def EnviarMensagem(self):
    chatBox = self.driver.find_element_by_class_name("_3uMse")
    chatBox.click()
    
    print(self.mensagem)
    
    chatBox.send_keys(self.mensagem)

    buttonSend = self.driver.find_element_by_xpath("//span[@data-icon='send']")
    buttonSend.click()

bot = ZapzapBot()