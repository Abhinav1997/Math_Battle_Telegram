from selenium import webdriver
import operator
import time

ops = {'+':operator.add,'–':operator.sub,'×':operator.mul,'/':operator.truediv}

#Replace ENTER_YOUR_GAME_LINK_HERE with URL to the game
gameLink = 'ENTER_YOUR_GAME_LINK_HERE'

#Replace PATH_TO_CHROMEDRIVER with the path to the executable file of chromedriver or you can add it to PATH
chromedriverPath = 'PATH_TO_CHROMEDRIVER'

chrome = webdriver.Chrome(chromedriverPath)
chrome.get(gameLink)

playButton = chrome.find_element_by_class_name('icon_play')
correctButton = chrome.find_element_by_id('button_correct')
wrongButton = chrome.find_element_by_id('button_wrong')
playButton.click()

#Replace this with the score you want
score = 100

for i in range(score):
	time.sleep(1)
	x = int(chrome.find_element_by_id('task_x').text)
	y = int(chrome.find_element_by_id('task_y').text)
	op = chrome.find_element_by_id('task_op').text
	res = int(chrome.find_element_by_id('task_res').text)
	trueres = ops[op](x,y)

	if trueres == res:
		correctButton.click()
	else:
		wrongButton.click()
