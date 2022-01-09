from selenium import webdriver
from openpyxl import load_workbook
import time

if __name__ == '__main__':
    # mở trình duyệt chrome
    driver = webdriver.Chrome()

    # đọc file testcase
    testcase_login = load_workbook("testcase/login_phong_tro.xlsx")
    sheet = testcase_login['Sheet1']
    data = list(sheet.values)
    data.pop(0)

    testcase_pass = 0
    testcase_fail = 0
    for row in data:
        check_pass = True
        # truy cập vào website
        driver.get("http://localhost/quanlyphongtro/admin/views/login")

        # lấy input username
        input_username = driver.find_element_by_name("username")
        # lấy input password
        input_password = driver.find_element_by_name("password")
        # lấy button đăng nhập
        button_login = driver.find_element_by_css_selector("button.start_login")

        # nhập các testcase
        time.sleep(1)
        if row[1]:
            input_username.send_keys(row[1])
        else:
            input_username.send_keys("")
        time.sleep(1)
        if row[2]:
            input_password.send_keys(row[2])
        else:
            input_password.send_keys("")
        time.sleep(1)
        button_login.click()
        time.sleep(1)
        # lấy message sau khi nhấn nút đăng nhập
        try:
            message = driver.find_element_by_css_selector(".login > form > p")
            if not message == None:
                message = message.text
                if str(message) == str(row[3]):
                    testcase_pass += 1
                else:
                    testcase_fail += 1
                    check_pass = False
            else:
                testcase_fail += 1
                check_pass = False
        except:
            pass

        # kiêm tra đăng nhập thành công
        if driver.current_url == "http://localhost/quanlyphongtro/admin/views/overview/":
            testcase_pass += 1
            # nếu đăng nhập thành công thì sẽ tiếp tục quay lại trang đăng nhập để test các testcase khác
            driver.get("http://localhost/quanlyphongtro/admin/views/login")
            time.sleep(1)
        print("#testcase %s: %s" % (row[0], "pass" if check_pass else "fail"))
        time.sleep(1)
    driver.close()
    print("=========================")
    print("Total: %s" % len(data))
    print("#Pass: %s" % testcase_pass)
    print("#Fail: %s" % testcase_fail)
