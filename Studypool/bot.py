import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from Studypool import const
from Studypool import Telegram_bot as tele 


class parse (webdriver.Chrome):
    def __init__(self, driver_path = const.driver_path, teardown = False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(parse, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def frst_page(self):
        self.get(const.Base_url)


    def open_popup(self):
        # open the Login popup 
        btn = self.find_element(
            By.CSS_SELECTOR,
            'a[onclick="open_login(); return false;"]'
        )
        btn.click()

    def login(self):
        # search for the button to login using Gmail
        btn = self.find_element(
            By.CSS_SELECTOR,
            'button[class="btn-social btn-google"]'
        )
        btn.click()

    def details(self, mail, password):
        # send the Gmail 
        box = self.find_element(
            By.ID,
            'identifierId'
        )
        box.clear()
        box.send_keys(mail)
        btn = self.find_element(
            By.CSS_SELECTOR,
            'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]'
        )
        btn.click()
        time.sleep(15)
        box = self.find_element(
            By.CSS_SELECTOR,
            'input[class="whsOnd zHQkBf"]'
        )
        box.clear()
        box.send_keys(password)
        btn = self.find_element(
            By.CSS_SELECTOR,
            'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]'
        )
        btn.click()

    def ten_rep_popup(self):
        ex = self.find_element(
            By.CSS_SELECTOR,
            'div[class="close-button"]'
        )
        ex.click()
    
    def open_ques_list(self):
        btn = self.find_element(
            By.CSS_SELECTOR,
            'a[href="/questions/newest"]'
        )
        btn.click()


    def apply_filter(self, pr1 = "", pr2 = ""):
        filter_elements = self.find_elements(
            By.CSS_SELECTOR,
            'div[class="priority-filter-btn"]'
        )
        for ele in filter_elements:
            txt = ele.find_element(
                By.CSS_SELECTOR,
                'div[class="priority-filter-name"]'
            )
            if txt.text == pr1 or txt.text == pr2:
                ele.click()
            

    def access_ques(self):
        try:
            cur = set()
            questions = self.find_elements(
                By.CSS_SELECTOR,
                'div[class="question-list-entry"]'
            )
            qu = list()
            dn = 0
            for q in questions:
                qu.clear()
                subj = q.find_element(
                    By.CSS_SELECTOR,
                    'div[class="upper-line category-name"]'
                )
                id = q.find_element(
                    By.CSS_SELECTOR,
                    'div[class="__react_component_tooltip place-top type-dark"]'
                )
                if id.get_attribute("id") not in const.initial:
                    dn = 1
                    tele.send(mes = f"New question available with the subject of: {subj.text}")
                cur.add(id.get_attribute("id"))
            # look for hot questions
            questions = self.find_elements(
                By.CSS_SELECTOR,
                'div[class="question-list-entry hot-urgent-question"]'
            )
            for q in questions:
                qu.clear()
                subj = q.find_element(
                    By.CSS_SELECTOR,
                    'div[class="upper-line category-name"]'
                )
                id = q.find_element(
                    By.CSS_SELECTOR,
                    'div[class="__react_component_tooltip place-top type-dark"]'
                )
                if id.get_attribute("id") not in const.initial:
                    dn = 1
                    tele.send(mes = f"ALERT!!! New HOT question available with the subject of: {subj.text}")
                cur.add(id.get_attribute("id"))
            if dn == 0:
                tele.upd()
            const.initial = cur
        except:
            tele.upd()
    

    def check_notifications(self):
        span = self.find_element(
            By.ID,
            "n2"
        )
        val = span.get_attribute("innerHTML")
        if int(val) > const.cur_noti:
            tele.send(mes = f"ALERT!!!! you have new {int(val) - const.cur_noti} notification(s).")
        const.cur_noti = int(val)