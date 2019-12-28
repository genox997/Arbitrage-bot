

from selenium import webdriver
from datetime import datetime
from util import twoway, threeway
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class odd():
   pass


class under_over_object():
    pass

def init(): 
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    global driver
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1500, 1080)
    global odds_opportunities
    odds_opportunities = []


def sanitize_list(mylist):
    initial_len = int(len(mylist) / 2)
    for x in range(initial_len):
        if not (str.split(mylist[int(len(mylist)/2)][0])[1] == str.split(mylist[0][0])[1]):
            mylist.pop(int(len(mylist)/2))
        else:
            return mylist
    return mylist

def tennis():
    driver.get('https://www.oddschecker.com/it/tennis/partite-del-giorno')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div/div')
    for row in list.find_elements_by_class_name('_3f0k2k'):
        try:
            match= None
            match = odd()
            wait = WebDriverWait(driver, 10)
            #wait.until(
         #   ec.visibility_of_element_located((By.CLASS_NAME, "_1ob6_g")))
            match.time =  datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text,"%H:%M").time()
            match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
            match.q1,match.q2=row.find_elements_by_class_name('_3fM9dR')
            match.p1,match.p2,match.q1,match.q2=match.p1.text,match.p2.text,match.q1.text,match.q2.text
        except:
            print("crashed tennis")
            continue
        if match.time < datetime.now().time():
            continue

        if match.q1 == "--" or match.q2== "--":
            continue

        match.p1_amount, match.p2_amount, match.profit =twoway(match.q1,match.q2)
        if match.profit > 0:
            odds_opportunities.append(match)


def football():
    driver.get('https://www.oddschecker.com/it/calcio/partite-del-giorno')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/div')
    for row in list.find_elements_by_class_name('_3f0k2k'):
        try:
            match = odd()
            wait = WebDriverWait(driver, 10)
            wait.until(
                ec.visibility_of_element_located((By.CLASS_NAME, "_1ob6_g")))

            match.time =  datetime.strptime(row.find_element_by_class_name("_1ob6_g").text,"%H:%M").time()
            match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
            match.win,match.draw,match.lost=row.find_elements_by_class_name('_3ba-Qo')
            match.p1,match.p2,match.win,match.draw, match.lost =match.p1.text,match.p2.text,match.win.text,match.draw.text, match.lost.text
        except:
            print("crashed football")
            continue

        if match.time < datetime.now().time():
            continue

        if match.win == "--" or match.draw== "--" or match.lost== "--":
            continue
        match.w_amount, match.d_amount, match.l_amount, match.profit =threeway(match.win,match.draw, match.lost)

        if match.profit > 0:
            odds_opportunities.append(match)


        # all_odds_link=row.find_element_by_class_name('_1V7UJb').get_attribute("href")
        # driver2.get(all_odds_link)
        # wait = WebDriverWait(driver2, 10)
        # uo_button = wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="event-header"]/div[2]/div/div[2]/div/div/button[3]')))
        # uo_button.click()
        # time.sleep(6)
        # under_over_list=driver2.find_elements_by_class_name('_1O7BsP')
        # under_over_odds=[]
        #
        # for uo_row in under_over_list:
        #     higher_q = uo_row.find_element_by_class_name("_2oad2B").text
        #     odd_name = uo_row.find_element_by_class_name("_2I4p8L").text
        #     name_odd = (odd_name, higher_q)
        #     under_over_odds.append(name_odd)
        #
        # under_over_odds.sort()
        # under_over_odds=sanitize_list(under_over_odds)
        # print (under_over_odds)
        # lenght = int(len(under_over_odds) /2)
        #
        # for i in range(lenght-1):
        #     p1_amount, p2_amount, profit = twoway(under_over_odds[i][1],under_over_odds[i+lenght][1])
        #     if profit > 0:
        #         print(match.p1 + " vs " + match.p2 + " " + under_over_odds[i][0] + "( " + under_over_odds[i][1] + ") "
        #               + under_over_odds[i+lenght][0] + "( " + under_over_odds[i+lenght][1]
        #               + ") at " + str(match.time) )
        #         print ( p1_amount, p2_amount, profit)

        #driver2.quit()


def basket():
    driver.get('https://www.oddschecker.com/it/basket')
    list = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div/div[3]/div')
    #('//*[@id="body"]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/ul')
    for row in list.find_elements_by_class_name('_3f0k2k '):
        try:
            match = None
            match = odd()
            match.time = datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text, "%H:%M").time()
            match.p1, match.p2 = row.find_elements_by_class_name('_2tehgH')
            match.q1, match.q2 = row.find_elements_by_class_name('_3fM9dR')
            match.p1, match.p2, match.q1, match.q2 = match.p1.text, match.p2.text, match.q1.text, match.q2.text
        except:
            print("crashed baseball")
            continue

        #if match.time < datetime.now().time():
            #continue

        if match.q1 == "--" or match.q2 == "--":
            continue

        match.p1_amount, match.p2_amount, match.profit = twoway(match.q1, match.q2)
        if match.profit > 0:
            odds_opportunities.append(match)

def baseball():
    driver.get('https://www.oddschecker.com/it/baseball/mlb')
    list = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div/div/div[2]/div/div')

    for row in list.find_elements_by_class_name('_3f0k2k'):
        try:
            match= None
            match = odd()
            match.time =  datetime.strptime(row.find_element_by_xpath('.//div[@class="_1ob6_g"]').text,"%H:%M").time()
            match.p1,match.p2 =row.find_elements_by_class_name('_2tehgH')
            match.q1,match.q2=row.find_elements_by_class_name('_3ba-Qo')
            match.p1,match.p2,match.q1,match.q2=match.p1.text,match.p2.text,match.q1.text,match.q2.text
        except:
            print("crashed baseball")
            continue

        if match.time < datetime.now().time():
            continue

        if match.q1 == "--" or match.q2== "--":
            continue

        match.p1_amount, match.p2_amount, match.profit = twoway(match.q1, match.q2)
        if match.profit > 0:
            odds_opportunities.append(match)

def catch():
    init()
    tennis()
    football()
    basket()
    baseball()
    driver.quit()
    return odds_opportunities

def print_odds():
    odds=catch()
    for odd in odds:
        if hasattr(odd, 'w_amount'):
            src_msg = "Match: " + odd.p1  + " vs " + odd.p2 + "\n" \
                      + "1: " + odd.win + " X: " + odd.draw + " 2: " + odd.lost + "\n" \
                      + "Bet: " +  str(odd.w_amount) + "(1) " +  str(odd.d_amount) + "(X) " +  str(odd.l_amount) + "(2) \n" \
                      + "Profit = " + str(odd.profit) + "%"


        else:
            src_msg= "Match: " + odd.p1  + " vs " + odd.p2 + "\n" \
                      + "1: " + odd.q1 + " 2: " + odd.q2 + "\n" \
                      + "Bet: " + str(odd.p1_amount) + " (1)  " + str(odd.p2_amount) + " (2)  \n" \
                      + "Profit = " + str(odd.profit) + "%"
        print(src_msg)
        



if __name__ == "__main__":
    print_odds()
    

