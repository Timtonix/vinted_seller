import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Vinted:
    def __init__(self, mail: str, password: str):
        self.mail = mail
        self.password = password

        self.driver = webdriver.Chrome()
        self.driver.get("https://vinted.fr")
        assert "Vinted" in self.driver.title

    def accept_cookie(self, answer: bool):
        if answer:
            element = self.driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
            element.click()
        else:
            element = self.driver.find_element(By.XPATH, "//button[@id='onetrust-reject-all-handler']")
            element.click()

    def connect(self):
        # 1.Click on S'inscrire | Se connecter
        element = self.driver.find_element(By.XPATH, "//a[@data-testid='header--login-button']")
        element.click()
        # 2.Switch to the connection page
        element = self.driver.find_element(By.XPATH, "//span[@data-testid='auth-select-type--register-switch']")
        element.click()
        # 3.Open the login form iframe
        element = self.driver.find_element(By.XPATH, "//span[@data-testid='auth-select-type--login-email']")
        element.click()
        # 4.Insert the email
        email_input = self.driver.find_element(By.ID, "username")
        email_input.send_keys(self.mail)
        # 5.Insert the password
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(self.password)
        # 6.Submit and get connected to Vinted !
        password_input.submit()
        time.sleep(20)



f = open("data.json")
credentials = json.loads(f.read())
vinted = Vinted(credentials["email"], credentials["password"])
f.close()
vinted.accept_cookie(False)
vinted.connect()