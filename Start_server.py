from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import undetected_chromedriver as uc


def Start_command():
    # Bot Bypass
    chromedriver_autoinstaller.install()
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.set_window_size(1012, 1012)

    driver.get('https://aternos.org/go/')

    # Username input
    elem = driver.find_element(by=By.ID, value='user')
    elem.send_keys('AstroKuro')
    driver.implicitly_wait(3)

    # Password Input
    elem = driver.find_element(by=By.ID, value='password')
    elem.send_keys('1tomimot1')
    driver.implicitly_wait(2.5)
    driver.find_element(by=By.ID, value='login').click()
    driver.implicitly_wait(300)
    print('logged')

    # Turning on
    driver.find_element(by=By.CLASS_NAME, value='css-ygmynb').click()
    print('it works 1')
    driver.implicitly_wait(2)
    driver.find_element(by=By.CLASS_NAME, value='qc-cmp2-buttons-desktop').click()
    driver.implicitly_wait(20)
    print('it works 2')
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.server-body"))).click()
    driver.implicitly_wait(20)
    print('it works 3')
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "start"))).click()
    driver.implicitly_wait(2)
    print('it works 4')

    driver.quit()
