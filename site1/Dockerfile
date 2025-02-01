# Dựa trên hình ảnh Python 3.10
FROM python:3

# Thiết lập môi trường để không đệm đầu ra
ENV PYTHONUNBUFFERED=1

# Thiết lập thư mục làm việc
WORKDIR /code

# Sao chép file requirements.txt vào thư mục làm việc
COPY requirements.txt .

# Cài đặt các thư viện được liệt kê trong requirements.txt
RUN pip install -r requirements.txt

# Sao chép tất cả các file và thư mục còn lại vào thư mục làm việc
COPY . .

# Tiếp xúc cổng 8000 để ứng dụng có thể truy cập từ bên ngoài
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]