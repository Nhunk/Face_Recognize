# 📌 Recognition for Automated Attendance Management

Hệ thống chấm công tự động bằng gương mặt.  
Dự án kết hợp **nhận diện khuôn mặt với Transformer + FAISS** để tăng tốc độ và độ chính xác, đồng thời sử dụng **MySQL-MariaDB** để lưu trữ dữ liệu nhân viên và ngày công.  
Người dùng có thể **đăng nhập qua web ASP.NET** để xem bảng chấm công.

---

## 🚀 Tính năng chính
- ✅ Nhận diện khuôn mặt nhân viên bằng mô hình **Transformer + FAISS**  
- ✅ Quản lý nhân viên và thông tin chấm công qua **SQL Server**  
- ✅ Hệ thống web **ASP.NET** để đăng nhập và xem ngày công  
- ✅ Tự động tính số ngày công dựa trên giờ vào/ra  
- ✅ Cấu trúc hướng đối tượng, dễ mở rộng  

---

## 📂 Cấu trúc thư mục (dự kiến)
```bash
project/
│── model/              # Transformer + FAISS model
│── database/           # SQL scripts, schema
│── web/                # ASP.NET WebForms/ASP.NET MVC
│── src/                # Mã nguồn Python nhận diện
│── docs/               # Tài liệu thiết kế, mô tả
│── README.md
⚙️ Công nghệ sử dụng
Ngôn ngữ: Python 3.10, C# (ASP.NET WebForms)

Database: SQL Server

Machine Learning: Transformer, FAISS (Facebook AI Similarity Search)

Web: ASP.NET (đăng nhập & xem ngày công)

🖥️ Demo (tùy chọn)
Ảnh chụp màn hình giao diện web

Hình minh họa nhận diện khuôn mặt

📖 Hướng dẫn sử dụng (tổng quan)
Nhân viên đăng ký khuôn mặt → hệ thống lưu vector embedding vào FAISS + SQL Server

Khi điểm danh, camera quét → mô hình so khớp khuôn mặt → ghi nhận thời gian vào/ra

Quản trị viên/nhân viên đăng nhập web ASP.NET → xem ngày công

🔗 Repository
GitHub: Recognition-for-Automated-Attendance-Management