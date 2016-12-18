from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Methods
import requests

driver = webdriver.Firefox()
Methods.login(driver, "AureyTest", "password")
Methods.challengePlayer(driver, "Aurey")
Methods.listPokemon(driver)