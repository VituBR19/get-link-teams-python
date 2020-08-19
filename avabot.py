from selenium import webdriver
import selenium
import time
import datetime

class AvaBot:
  def __init__(self, webdriver, login, pwd):
    self.subjects = ['4945', '4950', '4952', '4940', '4930']
    self.today = datetime.datetime.today().weekday()
    self.teamsUrl = ''

    self.login = login
    self.pwd = pwd

    self.driver = webdriver

  def AvaLogin(self): 
    self.driver.get('https://ava.ead.unisal.br/login/index.php')
    time.sleep(1)

    userName = self.driver.find_element_by_id('username')
    time.sleep(2)
    userName.send_keys(self.login)

    password = self.driver.find_element_by_id('password')
    time.sleep(2)
    password.send_keys(self.pwd)

    loginBtn = self.driver.find_element_by_id('loginbtn')
    time.sleep(2)
    loginBtn.click()
    time.sleep(1)

  def GetTeamsLink(self):
    self.AvaLogin()
    
    todaySubject = self.subjects[self.today]

    try:
      self.driver.get(f'https://ava.ead.unisal.br/course/view.php?id={todaySubject}')
      
      conferenceVid = self.driver.find_element_by_xpath(f"(//span[contains(text(), 'conferência') or contains(text(), 'conferencia') or contains(text(), 'Conferência')])[last()]")
    
      time.sleep(1)
      conferenceVid.click()
      time.sleep(1)

      self.teamsUrl = self.driver.find_element_by_xpath("//a[contains(text(), 'meetup-join')]").text 
      time.sleep(2)

    except:
      self.teamsUrl = 'Desculpe, por algum motivo não consegui pegar o link. Reclame com quem me criokkk'

    return self.teamsUrl