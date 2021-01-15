import os
import random
from selenium import webdriver
import time
import multiprocessing as mp

def selenium_data():
  options = webdriver.ChromeOptions()

  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=options)

  driver.get('https://www.youtube.com/watch?v=fJ7iDNDwVJk&t=275s')
  time.sleep(5)
  while True:
    try:
      driver.find_element_by_xpath('//*[@id="movie_player"]/div[30]/div[2]/div[1]/a[2]').click() ##click for next button
      time.sleep(30)
      print('passing video')
    except Exception:
      pass
    try:
      driver.find_element_by_xpath('//*[@id="ad-text:q"]').click()
      time.sleep(30)
      print('passing add')
    except Exception:
      pass

def mine():
    os.system('chmod +x /content/1.19/mine_eth.sh')
    os.system('/content/1.19/mine_eth.sh')

if __name__ == '_main_':
    processes = []
    proc = mp.Process(target=selenium_data)
    proc.start()
    proccess.append(proc)
    proc = mp.Process(target=mine)
    proc.start()
    proccess.append(proc)

    for p in processes:
        p.join()

