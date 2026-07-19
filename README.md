# 🚀 Enterprise Face Recognition & MLOps System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

Hệ thống điểm danh thông minh tự động hoàn toàn dựa trên công nghệ Nhận diện Khuôn mặt, được phát triển theo tiêu chuẩn sản xuất (production-ready) với kiến trúc Microservices và 파ipeline MLOps toàn diện.

Dự án ứng dụng các công nghệ tiên tiến nhất trong Computer Vision như **Vision Transformer (Dinov2)**, **YOLOv8** và hệ thống truy vấn vector **FAISS**.

---

## ✨ Tính năng nổi bật (Key Features)

### 1. Computer Vision & Deep Learning
- **Phát hiện khuôn mặt (Face Detection):** Tích hợp **YOLOv8** (`Ultralytics`) để phát hiện và cắt khuôn mặt với tốc độ xử lý thời gian thực, khắc phục các hạn chế về góc nghiêng và điều kiện ánh sáng.
- **Trích xuất đặc trưng (Feature Extraction):** Sử dụng **Vision Transformer (Dinov2)** từ HuggingFace để chuyển đổi hình ảnh khuôn mặt thành vector đặc trưng (embeddings) với độ chính xác cực cao.
- **Tìm kiếm tương đồng (Similarity Search):** Triển khai **FAISS** (Facebook AI Similarity Search) để so khớp vector, cho phép nhận diện hàng ngàn nhân viên chỉ trong vài mili-giây.

### 2. MLOps & System Architecture
- **Microservices API:** Đóng gói toàn bộ logic suy luận (inference) thành các endpoint RESTful tốc độ cao bằng **FastAPI**.
- **Containerization:** Triển khai linh hoạt với **Docker** và **Docker Compose**, đảm bảo tính nhất quán từ môi trường phát triển (Local) đến máy chủ đám mây (AWS EC2/ECS).
- **Experiment Tracking:** Sử dụng **MLflow** để theo dõi chặt chẽ vòng đời mô hình, log lại các siêu tham số (hyperparameters), metrics (Accuracy, F1 Score) và quản lý model artifacts (FAISS Index).

### 3. Data Pipeline & Analytics
- **Auto-Annotation:** Pipeline tiền xử lý tự động sử dụng YOLO để trích xuất ảnh khuôn mặt từ video thô, tối ưu hóa quá trình xây dựng tập dữ liệu huấn luyện.
- **Time-Series Analysis:** Module phân tích dữ liệu chuỗi thời gian (điểm danh) bằng **Pandas**, giúp phát hiện xu hướng đi trễ/về sớm và dự báo số lượng nhân sự có mặt (Forecasting).

---

## 🛠 Công nghệ sử dụng (Tech Stack)

| Lĩnh vực | Công nghệ |
| :--- | :--- |
| **Computer Vision** | `PyTorch`, `Transformers (Dinov2)`, `Ultralytics (YOLOv8)`, `OpenCV` |
| **Machine Learning** | `FAISS`, `Scikit-learn`, `Pandas`, `Albumentations` |
| **MLOps & Backend** | `FastAPI`, `Docker`, `Docker Compose`, `MLflow` |
| **Database & UI** | `MySQL / MariaDB`, `Tkinter` |

---

## 🚀 Hướng dẫn Cài đặt & Khởi chạy (Quick Start)

Nhờ kiến trúc Dockerized, việc khởi chạy toàn bộ hệ thống trở nên cực kỳ đơn giản mà không cần cấu hình rườm rà.

### Yêu cầu:
- [Docker](https://docs.docker.com/get-docker/) và [Docker Compose](https://docs.docker.com/compose/install/) đã được cài đặt.

### Khởi chạy hệ thống:
1. Clone repository về máy.
2. Mở terminal tại thư mục gốc của dự án.
3. Chạy lệnh sau để build và khởi động hệ thống:
```bash
docker-compose up -d --build
```

### Các Dịch vụ sau khi khởi chạy:
- **FastAPI (Swagger UI):** Truy cập `http://localhost:8000/docs` để test trực tiếp các API nhận diện.
- **MLflow Dashboard:** Truy cập `http://localhost:5000` để xem các báo cáo huấn luyện và metrics.

---

## 📂 Cấu trúc Thư mục Hệ thống

```bash
project/
├── api/                   # FastAPI Server (Endpoints: /detect, /recognize)
├── model/                 # Core AI Models (Dinov2, YOLO) & MLflow Tracking
├── data_pipeline/         # Scripts Auto-annotation và Data processing
├── database/              # SQL scripts cho dữ liệu nhân sự (MySQL)
├── web/                   # (Tùy chọn) Giao diện quản lý Web
├── Dockerfile             # Cấu hình container cho FastAPI API
├── docker-compose.yml     # Khởi chạy hệ thống Microservices
└── requirements.txt       # Dependencies
```

---

## 👨‍💻 Tác giả & Ứng dụng thực tế

Dự án này được xây dựng không chỉ như một phần mềm Quản lý điểm danh, mà còn là một minh chứng (Proof of Concept) cho khả năng:
- Áp dụng các bài báo khoa học (Vision Transformers) vào thực tế sản xuất.
- Kỹ năng triển khai mô hình học máy (Deploy / MLOps).
- Khả năng tích hợp liên phòng ban (Phần cứng Camera -> AI Model -> Database/Backend).
