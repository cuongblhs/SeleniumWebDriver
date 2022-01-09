from selenium import webdriver
from openpyxl import load_workbook
import time

if __name__ == '__main__':
    # mở trình duyệt chrome
    driver = webdriver.Chrome()

    # đọc file testcase
    testcase_login = load_workbook("testcase/add_dich_vu.xlsx")
    sheet = testcase_login['Sheet1']
    data = list(sheet.values)
    data.pop(0)

    testcase_pass = 0
    testcase_fail = 0
    for row in data:
        check_pass = True
        # truy cập vào website
        driver.get("http://localhost/quanlyphongtro/admin/views/listservices/")
        time.sleep(1)

        # kiểm tra nếu bị chuyển về trang đăng nhập thì tức là cần phải đăng nhập
        if driver.current_url == "http://localhost/quanlyphongtro/admin/views/login/":
            # lấy input username
            input_username = driver.find_element_by_name("username")
            # lấy input password
            input_password = driver.find_element_by_name("password")
            # lấy button đăng nhập
            button_login = driver.find_element_by_css_selector("button.start_login")
            input_username.send_keys("admin")
            input_password.send_keys("12345")
            button_login.click()
            time.sleep(1)
            # vào lại trang quản lý dịch vụ sau khi đăng nhập
            driver.get("http://localhost/quanlyphongtro/admin/views/listservices/")

        # lấy nút thêm dịch vụ
        button_add = driver.find_element_by_css_selector("button.themmoi")
        button_add.click()
        time.sleep(1)
        # lấy input thông tin dịch vụ
        input_name = driver.find_element_by_id("tendichvu")
        input_price = driver.find_element_by_id("dongia")
        input_donvi = driver.find_element_by_id("donvi")
        input_desc = driver.find_element_by_id("mota")

        # nhập các testcase
        if row[1]:
            input_name.send_keys(row[1])
        else:
            input_name.send_keys("")
        if row[2]:
            input_price.send_keys(row[2])
        else:
            input_price.send_keys("")
        if row[3]:
            input_donvi.send_keys(row[3])
        else:
            input_donvi.send_keys("")
        if row[4]:
            input_desc.send_keys(row[4])
        else:
            input_desc.send_keys("")

        # lấy nút lưu dịch vụ
        button_save = driver.find_element_by_css_selector("button#luudv")
        button_save.click()
        time.sleep(1)

        # lấy message thông báo
        message = driver.find_element_by_css_selector(".thongbaoloi")
        if message.text == "":
            try:
                message = driver.find_element_by_css_selector(".saidinhdang2")
            except:
                message = driver.find_element_by_css_selector(".thongbao:last-child")
        message = message.text
        if str(message) == str(row[5]):
            testcase_pass += 1
        else:
            testcase_fail += 1
            check_pass = False
        print("#testcase %s: %s" % (row[0], "pass" if check_pass else "fail"))
        time.sleep(1)
    driver.close()
    print("=========================")
    print("Total: %s" % len(data))
    print("#Pass: %s" % testcase_pass)
    print("#Fail: %s" % testcase_fail)