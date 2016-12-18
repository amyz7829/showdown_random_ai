from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

def login(driver, playerName, password):
    driver.get("http://play.pokemonshowdown.com")

    try:
        chooseNameButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
        chooseNameButton.click()
    except:
        print("failed to find chooseName button")
        driver.quit()
        return

    try:
        userName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        userName.send_keys(playerName)
        chooseName = driver.find_element_by_xpath("//P[@class='buttonbar']//STRONG[text() = 'Choose name']")
        chooseName.click()
    except:
        print("failed to find username entry")
        driver.quit()
        return

    try:
        passwordInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        passwordInput.clear()
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.RETURN)

    except:
        print("failed to find password button")
        driver.quit()
        return

    if(driver.find_element_by_xpath("(//SPAN[@class='username'])[1]").get_property("data-name") is playerName):
        print("successfully logged in")


# Takes webdriver and the player name as arguments. Presumes you are already logged in
def challengePlayer(driver, playerName):
    findUserButton = driver.find_element_by_name("finduser")
    findUserButton.click()

    try:
        findUserText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "data"))
        )
    except:
        print("unable to enter in playername")
        driver.quit()
        return

    findUserText.send_keys(playerName)
    findUserText.send_keys(Keys.RETURN)

    try:
        challengeUserButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "challenge"))
        )
    except:
        print("unable to find challenge button")
        driver.quit()
        return

    challengeUserButton.click()

    try:
        startRandomBattleButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "makeChallenge"))
        )
    except:
        print("unable to find start random battle button")
        driver.quit()
        return

    startRandomBattleButton.click()

# Presumes you are in a battle
def listPokemon(driver):
    pokemon_list = driver.get_elements_by_name("chooseSwitch")
    for pokemon in pokemon_list:
        print(pokemon.text())

def elementExistsByCSS(driver, css):
    try:
        driver.find_element_by_css_selector(css)
    except:
        return False

    return True

def elementExistsByXpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        return False
    return True

def elementExistsByName(driver, name):
    try:
        driver.find_element_by_name(name)
    except:
        return False
    return True

def elementExistsById(driver, id):
    try:
        driver.find_element_by_id(id)
    except:
        return False
    return True

