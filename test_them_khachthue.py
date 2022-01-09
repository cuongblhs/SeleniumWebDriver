from selenium import webdriver
from openpyxl import load_workbook
import time

if __name__ == '__main__':
    # mở trình duyệt chrome
    driver = webdriver.Chrome()

    # đọc file testcase
    testcase_login = load_workbook("testcase/add_khach_thue.xlsx")
    sheet = testcase_login['Sheet1']
    data = list(sheet.values)
    data.pop(0)

    testcase_pass = 0
    testcase_fail = 0
    for row in data:
        check_pass = True
        # truy cập vào website
        driver.get("http://localhost/quanlyphongtro/admin/views/renters/")
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
            # vào lại trang quản lý người trọ sau khi đăng nhập
            driver.get("http://localhost/quanlyphongtro/admin/views/renters/")

        # lấy nút thêm dịch vụ
        button_add = driver.find_element_by_css_selector("button.themmoi")
        button_add.click()
        time.sleep(1)
        # lấy input thêm khách thuê
        input_name = driver.find_element_by_id("tenkhachthue")
        input_phone = driver.find_element_by_id("sodienthoai")
        input_cmt = driver.find_element_by_id("socmnd")
        input_email = driver.find_element_by_id("email")
        input_noicap = driver.find_element_by_id("noicap")
        input_hokhau = driver.find_element_by_id("hokhau")
        input_ngaysinh = driver.find_element_by_id("ngaysinh")
        input_ngaycap = driver.find_element_by_id("ngaycap")
        input_noicongtac = driver.find_element_by_id("noicongtac")
        input_mota = driver.find_element_by_id("mota")
        input_anhdaidien = driver.find_element_by_id("anh0")
        input_mattruoc = driver.find_element_by_id("anh1")
        input_matsau = driver.find_element_by_id("anh2")
        input_bome = driver.find_element_by_id("bome")
        input_lienhe = driver.find_element_by_id("sdtlienhe")
        input_tamtru = driver.find_element_by_css_selector(".right_nhapthongtin input[type='checkbox']")

        # nhập các testcase
        if row[1]:
            input_name.send_keys(row[1])
        else:
            input_name.send_keys("")
        if row[2]:
            input_phone.send_keys(row[2])
        else:
            input_phone.send_keys("")
        if row[3]:
            input_cmt.send_keys(row[3])
        else:
            input_cmt.send_keys("")
        if row[4]:
            input_email.send_keys(row[4])
        else:
            input_email.send_keys("")
        if row[5]:
            input_noicap.send_keys(row[5])
        else:
            input_noicap.send_keys("")
        if row[6]:
            input_hokhau.send_keys(row[6])
        else:
            input_hokhau.send_keys("")

        if row[7] == "Nam":
            driver.find_element_by_css_selector("input[name='gioitinh'][value='Nam']").click()
        else:
            driver.find_element_by_css_selector("input[name='gioitinh'][value='Nữ']").click()
        if row[8] == "Sinh viên":
            driver.find_element_by_css_selector("input[name='nghenghiep'][value='Sinh viên']").click()
        else:
            driver.find_element_by_css_selector("input[name='ngheghiep'][value='Người đi làm']").click()

        if str(row[9]) == "1":
            if not input_tamtru.get_attribute("checked"):
                input_tamtru.click()
        else:
            if input_tamtru.get_attribute("checked"):
                input_tamtru.click()

        if row[10]:
            input_ngaysinh.click()
            time.sleep(1)
            driver.find_element_by_css_selector("a.ui-state-highlight").click()
        else:
            input_ngaysinh.send_keys("")
        if row[11]:
            input_ngaycap.click()
            time.sleep(1)
            driver.find_element_by_css_selector("a.ui-state-highlight").click()
        else:
            input_ngaycap.send_keys("")
        if row[12]:
            input_noicongtac.send_keys(row[12])
        else:
            input_noicongtac.send_keys("")
        if row[13]:
            input_mota.send_keys(row[13])
        else:
            input_mota.send_keys("")
        if row[14]:
            input_anhdaidien.send_keys(row[14])
        if row[15]:
            input_mattruoc.send_keys(row[15])
        if row[16]:
            input_matsau.send_keys(row[16])
        if row[17]:
            input_bome.send_keys(row[17])
        else:
            input_bome.send_keys("")
        if row[18]:
            input_lienhe.send_keys(row[18])
        else:
            input_lienhe.send_keys("")

        # lấy nút lưu
        button_save = driver.find_element_by_css_selector("button#luukt")
        button_save.click()
        time.sleep(1)

        # lấy message thông báo
        message = driver.find_element_by_css_selector(".thongbaoloi")
        if message.text == "":
            try:
                message = driver.find_element_by_css_selector(".saidinhdang > p")
            except:
                message = driver.find_element_by_css_selector(".thongbao:last-child")
        message = message.text
        if str(message) == str(row[19]):
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