from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time
import requests


class Bot():

    def __init__(self,username,password):
        self.username = username
        self.password = password

        #Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--enable-javascript")
        # chrome_options.add_argument('--headless')

        
        #Firefox
        # Firefox_options = webdriver.FirefoxOptions()
        # Firefox_options.add_argument('--disable-extensions')
        # Firefox_options.add_argument('--profile-directory=Default')
        # # firefox_options.add_argument("--incognito")
        # Firefox_options.add_argument("--disable-plugins-discovery")
        # Firefox_options.add_argument("--start-maximized")
        # Firefox_options.add_argument("--enable-javascript")
        # # chrome_options.add_argument('--headless')



        self.bot = webdriver.Chrome(chrome_options=chrome_options,executable_path=ChromeDriverManager().install())

    def signIn(self):

        bot = self.bot
        actions = ActionChains(driver=bot)

        #TempMail
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(5)

        user = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user.click()
        user.clear()
        user.send_keys(self.username)

        next_bttn = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_bttn.click()

        time.sleep(3)

        password = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.click()
        password.clear()
        password.send_keys(self.password)

        login = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login.click()
        time.sleep(5)


        #TILL HERE WE ARE INSIDE TWITTER

    def url_get(self):

        bot = self.bot
        # notifications = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]/div/div/svg/g/path')
        # notifications.click()
        bot.get('https://twitter.com/notifications/mentions')
        bot.refresh()
        time.sleep(4)

        get_tweet = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
        get_tweet.click()
        time.sleep(3)

        get_text = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div')
        get_url = get_text.text

        print(get_url)
        L = get_url.split()
        print(L)
        self.url = L[0]
        print(self.url)
    
    def youtube(self):
        bot = self.bot
        #APT
        
        bot.get_screenshot_as_png()
        url = "https://socialdownloader.p.rapidapi.com/api/youtube/video"

        querystring = {"video_link":self.url}

        headers = {
            "X-RapidAPI-Host": "socialdownloader.p.rapidapi.com",
            "X-RapidAPI-Key": "541ba0b10cmsh69a95ab9288a5c4p1fc871jsn8c1849223ba5"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

        
    def screenshot(self):
        bot = self.bot
        bot.get('https://twitter.com/notifications/mentions')
        bot.refresh()
        time.sleep(4)


        get_tweet = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
        get_tweet.click()
        time.sleep(3)

        name_of_reqester = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[2]/div/div/div[1]/article/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/div/div/span').text


        target = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]')
        target.click()

        ss = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section').screenshot_as_png

        bot.get('https://twitter.com/compose/tweet')
        tweet = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet.send_keys(ss)

    def quotes(self):
        bot = self.bot


        url = "https://motivational-quotes1.p.rapidapi.com/motivation"

        payload = {
            "key1": "value",
            "key2": "value"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
            "X-RapidAPI-Key": "541ba0b10cmsh69a95ab9288a5c4p1fc871jsn8c1849223ba5"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        
        bot.get('https://twitter.com/compose/tweet')
        time.sleep(2)
        tweet = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        tweet.send_keys(response.text)



t = Bot('Udi_Codes', 'Wildlife@44')
t.signIn()
# t.url_get()
# t.youtube()
# t.screenshot()
t.quotes()