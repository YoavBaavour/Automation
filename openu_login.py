from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException

user_name = ''
password = ''
user_id = ''
url = 'https://sso.apps.openu.ac.il/login?T_PLACE=https://sheilta.apps.openu.ac.il/pls/dmyopt2/sheilta.main'
# add 'detach' option to avoid web page closing at the end of the program
driver = webdriver.Firefox(firefox_options=Options().add_experimental_option("detach", True))
driver.get(url)

# get user name field
try:
    user_name_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'p_user')))
except NoSuchElementException:
    print('username field not found')
    driver.quit()
except TimeoutException:
    print('Timed out.')
    driver.quit()

# user_name_field field found
user_name_field.click()
user_name_field.send_keys(user_name)

# get password field
try:
    password_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'p_sisma')))
except NoSuchElementException:
    print('password field not found')
    driver.quit()
except TimeoutException:
    print('Timed out.')
    driver.quit()

# password_field found
password_field.click()
password_field.send_keys(password)

# get id number field
try:
    id_num_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'p_mis_student')))
except NoSuchElementException:
    print('ID field not found')
    driver.quit()
except TimeoutException:
    print('Timed out.')
    driver.quit()

# id_num_field found
id_num_field.click()
id_num_field.send_keys(user_id)

#get login button
try:
    login = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[1]/form/fieldset/input[1]')))
except NoSuchElementException:
    print('login button not found')
    driver.quit()
except TimeoutException:
    print('Timed out.')
    driver.quit()

# login button found
login.click()
