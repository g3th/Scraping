from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time, requests


login="https://auth.hulu.com/web/login?next=https://secure.hulu.com/account"
browser= webdriver.Chrome()
browser.set_window_size(350,900); browser.get(login)
email=browser.find_element_by_xpath('//*[@id="email_id"]')
passw=browser.find_element_by_xpath('//*[@id="password_id"]')
logclick=browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[1]/div/button')

email.send_keys("myemail@email.com"); passw.send_keys("mypass")
logclick.click()

def canned_soup():
	url = page
	headers = {'User-Agent': 'Mozilla 5.0'}
	request = requests.get(url, headers=headers)
	soup = BS(request.text,"html.parser")
	return soup

def tab_one():
	browser.switch_to.window(browser.window_handles[0])

def tab_two():
	browser.switch_to.window(browser.window_handles[1])

page = input("Series URL:")
season = input("Season: ")
episodes = int(input ("Eps: "))
series_id= page[-36:]
browser.execute_script('window.open("'+page+'");'); tab_two();time.sleep(10)  
n=1; eps=[]
while n<=episodes:
	btn=browser.find_element_by_xpath('//*[@id="LevelTwo__scroll-area"]/div/div/div[4]/div[1]/div/div/div/button')
	btn.click()
	ssea=browser.find_element_by_xpath('//*[@id="'+series_id+'::'+str(season)+'"]')
	ssea.click(); time.sleep(2)
	play='//*[@id="LevelTwo__scroll-area"]/div/div/div[4]/div[2]/div/div/div['+str(n)+']/figure/div/button'
	video=browser.find_element_by_xpath(play)
	video.click()
	n=n+1
	time.sleep(3);eps.append(browser.current_url)
	browser.close();tab_one()
	browser.execute_script('window.open("'+page+'");'); tab_two(); time.sleep(3)

with open("C:/Users/User/Desktop/hululist.txt","w+") as hulu:
	for lines in eps:
		hulu.write(lines+"\n")


#//*[@id="LevelTwo__scroll-area"]/div/div/div[4]/div[1]/div/div/div/ul
#//*[@id="52b8dd8a-eff2-4ed2-9b8d-7c0039df1c53::2"]
#//*[@id="52b8dd8a-eff2-4ed2-9b8d-7c0039df1c53::4"]
