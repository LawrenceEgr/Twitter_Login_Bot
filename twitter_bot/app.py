#by LawrenceEgr*/
from selenium import webdriver
from selenium.webdriver.common import keys
import time

class TwitterBot:
  def __init__(self,email,username,password) :
      self.email = email
      self.username = username 
      self.password = password
      self.bot = webdriver.Firefox()
      

  def login(self):
      bot = self.bot
      bot.get('https://twitter.com/i/flow/login') 
      time.sleep(5)  
      email = bot.find_element_by_name('text')
      email.clear()
      email.send_keys(self.email)
      email.send_keys(keys.Keys.RETURN)
      time.sleep(5)
  def userName(self):
       bot = self.bot
       
       username =   bot.find_element('text')
       username.clear()
       username.send_keys(self.username)
       username.send_keys(keys.Keys.RETURN)
       time.sleep(10)

  def loginPassword(self):
       bot = self.bot
       
       password =  bot.find_element("password")
       password.clear()
       password.send_keys(self.password)
       password.send_keys(keys.Keys.RETURN)
       time.sleep(7)

  def like_tweet(self,hashtag):
      bot = self.bot
      bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
      time.sleep(4)
      for i in range(1,5):
       bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
       time.sleep(5)
       tweets = bot.find_elements_by_class_name('css-1dbjc4n  r-18u37iz')
       links = [elem.get_attribute('css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-io23vh')
                for elem in tweets]
       print(links)
      #for link in links:
          #bot.get('https://twitter.com' + link)
          #try:
           #   bot.find_element_by_class_name('r-4qtqp9 r-yyyyoo r-ixvlist r-dnmrzs r-bnwqin r1plcruibr r-lrvbr r-1hdvoqi').click()
           #   time.sleep(5)
         # except Exception as ex:
           #   time.sleep(60)




ed = TwitterBot('your_email', 'your_username' , 'Your_password')
ed.login()
ed.userName()
ed.loginPassword()  
ed.like_tweet('UDA')   
