import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang đăng nhập Admin Django
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

# Nhập tên người dùng
inputUserName = driver.find_element(By.NAME, value="username")
inputUserName.send_keys("admin")
time.sleep(1.5)

# Nhập mật khẩu
password = driver.find_element(By.NAME, value="password")
password.send_keys("832005")
time.sleep(1.5)

# Nhấn Enter để đăng nhập
password.send_keys(Keys.RETURN)
time.sleep(5)  # Đợi trang admin load xong

# Chuyển hướng đến giao diện chính của web
driver.get("http://127.0.0.1:8000/courses/")
time.sleep(5)  # Đợi trang web chính load xong

driver.get("http://127.0.0.1:8000/edit-course/?course_id=1")
time.sleep(5)  # Đợi trang web chính load xong
# Tìm và nhấn vào nút "GỬI" bằng ID
send_button = driver.find_element(By.ID, "sendButton")
send_button.click()

# Đợi xử lý hoàn tất
time.sleep(5)


# Đóng trình duyệt
driver.quit()
