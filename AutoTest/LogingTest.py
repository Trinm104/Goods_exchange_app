import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        """Thiết lập: Khởi động trình duyệt"""
        self.driver = webdriver.Chrome()  # Đảm bảo rằng ChromeDriver đã được cài đặt

    def tearDown(self):
        """Kết thúc: Đóng trình duyệt"""
        self.driver.quit()

    def test_unit_login(self):
        """Kiểm tra đăng nhập"""
        driver = self.driver

        # Truy cập vào trang quản trị Django
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        print("Đang mở trình duyệt...")

        # Điền tên đăng nhập
        inputUserName = driver.find_element(By.NAME, "username")
        inputUserName.send_keys("admin")

        # Điền mật khẩu
        password = driver.find_element(By.NAME, "password")
        password.send_keys("832005")

        # Gửi thông tin đăng nhập
        password.send_keys(Keys.RETURN)
        print("Đang gửi thông tin đăng nhập...")

        # Chờ trang tải (nên thay bằng WebDriverWait để chuyên nghiệp hơn)
        time.sleep(5)

        # Kiểm tra tiêu đề trang
        actual_title = driver.title
        expected_title = "Site administration | Django site admin"
        print(f"Tiêu đề trang: {actual_title}")
        self.assertEqual(actual_title, expected_title, "Tiêu đề trang không khớp!")

        print("Kiểm tra đăng nhập hoàn tất.")


if __name__ == "__main__":
    unittest.main()
