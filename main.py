

from selenium import webdriver
from datetime import datetime
from util import twoway, threeway


class odd():
    pass

driver = webdriver.Chrome('/home/claudio/PycharmProjects/Arbitrage/chromedriver')

def tennis():
    driver.get('https://www.oddschecker.com/it/tennis/partite-del-giorno')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/ul')
    for row in list.find_elements_by_class_name('_3f0k2k'):
        match= None
        match = odd()
        match.time =  datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text,"%H:%M").time()
        match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
        match.q1,match.q2=row.find_elements_by_class_name('_3fM9dR')
        match.p1,match.p2,match.q1,match.q2=match.p1.text,match.p2.text,match.q1.text,match.q2.text

        if match.time < datetime.now().time():
            continue

        if match.q1 == "--" or match.q2== "--":
            continue

        p1_amount, p2_amount, profit =twoway(match.q1,match.q2)

        if profit > 0:

            print(match.p1 +"("+match.q1+")" + " vs " + match.p2  +'('+match.q2+") at " + str(match.time) )
            print (p1_amount, p2_amount, profit)

def football():
    driver.get('https://www.oddschecker.com/it/calcio/partite-del-giorno')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/div')
    for row in list.find_elements_by_class_name('_3f0k2k'):
        match= None
        match = odd()
        match.time =  datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text,"%H:%M").time()
        match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
        match.win,match.draw,match.lost=row.find_elements_by_class_name('_3ba-Qo')
        match.p1,match.p2,match.win,match.draw, match.lost =match.p1.text,match.p2.text,match.win.text,match.draw.text, match.lost.text

        if match.time < datetime.now().time():
            continue

        if match.win == "--" or match.draw== "--" or match.lost== "--":
            continue
        w_amount, d_amount, l_amount, profit =threeway(match.win,match.draw, match.lost)

        if profit > 0:
            print(match.p1 + " vs " + match.p2 + '(' + match.win + ", " + match.draw + ". " + match.lost + " ) at " + str(match.time))
            print(w_amount , d_amount , l_amount , profit )

    #driver.find_element_by_class_name("_1-VXWc iconarrow_rightBlack iconarrow_rightBlacksize").click()

def baseball():
    driver.get('https://www.oddschecker.com/it/baseball/mlb')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div/div/div[2]/div/div')
    for row in list.find_elements_by_class_name('_3f0k2k'):
        match= None
        match = odd()
        match.time =  datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text,"%H:%M").time()
        match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
        match.q1,match.q2=row.find_elements_by_class_name('_3ba-Qo')
        match.p1,match.p2,match.q1,match.q2=match.p1.text,match.p2.text,match.q1.text,match.q2.text

        if match.time < datetime.now().time():
            continue

        if match.q1 == "--" or match.q2== "--":
            continue

        p1_amount, p2_amount, profit =twoway(match.q1,match.q2)

        #if profit > 0:

        print(match.p1 +"("+match.q1+")" + " vs " + match.p2  +'('+match.q2+") at " + str(match.time) )
        print (p1_amount, p2_amount, profit)

def main():
    tennis()
    football()
    baseball()

main()