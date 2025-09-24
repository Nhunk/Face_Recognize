# Recognition for Automated Attendance Management

Hệ thống chấm công tự động bằng gương mặt.  
Dự án kết hợp **nhận diện khuôn mặt với Transformer + FAISS** để tăng tốc độ và độ chính xác, đồng thời sử dụng **MySQL-MariaDB** để lưu trữ dữ liệu nhân viên và ngày công.  
Người dùng có thể **đăng nhập qua web ASP.NET** để xem bảng chấm công.

---

## Tính năng chính
- Nhận diện khuôn mặt nhân viên bằng mô hình **Transformer + FAISS**  
- Quản lý nhân viên và thông tin chấm công qua **SQL Server**  
- Hệ thống web **ASP.NET** để đăng nhập và xem ngày công  
- Tự động tính số ngày công dựa trên giờ vào/ra  
- Cấu trúc hướng đối tượng, dễ mở rộng  

---

### Cấu trúc thư mục (dự kiến)
```bash
project/
│── model/              # Transformer + FAISS model
│── database/           # SQL scripts, schema
│── web/                # ASP.NET WebForms/ASP.NET MVC
│── src/                # Mã nguồn Python nhận diện
│── docs/               # Tài liệu thiết kế, mô tả
│── README.md
```

### Công nghệ sử dụng
- Ngôn ngữ: Python 3.10, C# (ASP.NET WebForms)
- Database: SQL Server
- Machine Learning: Transformer, FAISS (Facebook AI Similarity Search)
- Web: ASP.NET (đăng nhập & xem ngày công)


### Hướng dẫn sử dụng (tổng quan)
Nhân viên đăng ký khuôn mặt → hệ thống lưu vector embedding vào FAISS + SQL Server
Khi điểm danh, camera quét → mô hình so khớp khuôn mặt → ghi nhận thời gian vào/ra
Quản trị viên/nhân viên đăng nhập web ASP.NET → xem ngày công

#### 1. Cài đặt cơ sở dữ liệu MySQL/MariaDB

Cài đặt MySQL hoặc MariaDB trên máy.

Tạo database tên nckh:

CREATE DATABASE nckh;


Import file SQL trong thư mục database/ để tạo bảng và dữ liệu mẫu:

mysql -u root -p nckh < database/schema.sql

#### 2. Cấu hình chuỗi kết nối (ASP.NET)

Trong file Web.config hoặc App.config thêm:

<connectionStrings>
  <add name="ConnectionString"
       connectionString="server=localhost;user id=root;password=1234;database=nckh;SslMode=none;AllowPublicKeyRetrieval=true;"
       providerName="MySql.Data.MySqlClient"/>
</connectionStrings>


🔑 Thay user id và password theo tài khoản MySQL của bạn.

#### 3. Cài đặt môi trường Python (AI Model)

##### Tạo môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```


##### Cài dependencies:
```bash
pip install -r src/requirements.txt
```

#### 4. Train và chạy mô hình nhận diện

Chạy script để huấn luyện hoặc nạp model sẵn:
```bash
python src/train_model.py
```


Khởi chạy module nhận diện:
```bash

python src/face_recognition.py
```

#### 5. Chạy ứng dụng Web ASP.NET

Mở web/ trong Visual Studio.

Kiểm tra lại connectionStrings.

Nhấn Run (IIS Express) để khởi chạy website.

Truy cập http://localhost:5000 để đăng nhập và xem ngày công.




**Repository**

GitHub: Recognition-for-Automated-Attendance-Management
