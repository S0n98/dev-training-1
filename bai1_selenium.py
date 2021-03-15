from selenium import webdriver

username = 'admin'
password = '123456aA'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://45.79.43.178/source_carts/wordpress/wp-login.php')

user_input = driver.find_element_by_id('user_login')
user_input.send_keys(username)

password_input = driver.find_element_by_id('user_pass')
password_input.send_keys(password)

login_button = driver.find_element_by_id('wp-submit')
login_button.click()

element = driver.find_elements_by_class_name('display-name')
print(element[0].get_attribute('innerHTML'))