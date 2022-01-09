from selenium import webdriver
import time

if __name__ == '__main__':
    # mở trình duyệt chrome
    driver = webdriver.Chrome(port=9515)
    # truy cập vào website
    driver.get("http:localhost/bhdt?role=admin")

    # lấy input username
    input_username = driver.find_element_by_name("username")
    # lấy input password
    input_password = driver.find_element_by_name("password")
    # lấy button đăng nhập
    button_login = driver.find_element_by_css_selector(".login-btn button")

    # nhập các testcase
    # time.sleep(1)
    # input_username.send_keys("admin")
    # time.sleep(1)
    # input_password.send_keys("123456")
    # time.sleep(1)
    # button_login.click()

    print(input_password.get_attribute("required"))

    # lấy đối tượng popup
    # alert = driver.switch_to.alert
    # time.sleep(1)
    # print(alert.text)
    # alert.accept()

