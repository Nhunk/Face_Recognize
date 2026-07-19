import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class AttendanceAnalyzer:
    def __init__(self, csv_path=None):
        """
        Khởi tạo module phân tích dữ liệu chuỗi thời gian (time-series) cho việc điểm danh.
        Trong thực tế, bạn sẽ load từ Database (MySQL). Ở đây dùng Pandas DataFrame/CSV làm ví dụ.
        """
        if csv_path:
            self.df = pd.read_csv(csv_path)
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        else:
            self.df = self._generate_dummy_data()

    def _generate_dummy_data(self):
        """Tạo dữ liệu điểm danh giả lập (Time-Series) trong 30 ngày."""
        print("[INFO] Generating dummy time-series attendance data...")
        dates = pd.date_range(start="2026-06-01", periods=30, freq='D')
        employees = ['Nguyen Van A', 'Tran Thi B', 'Le Van C', 'Pham Thi D']
        
        data = []
        for date in dates:
            # Skip weekends
            if date.weekday() >= 5:
                continue
                
            for emp in employees:
                # 90% chance to attend
                if np.random.rand() < 0.9:
                    # Random arrival time between 7:30 and 8:30 AM
                    arrival_time = date + timedelta(hours=7, minutes=30) + timedelta(minutes=np.random.randint(0, 60))
                    data.append({
                        'employee_name': emp,
                        'timestamp': arrival_time,
                        'status': 'Present'
                    })
        
        return pd.DataFrame(data)

    def analyze_arrival_patterns(self):
        """
        Phân tích xu hướng giờ đến (Arrival Time Trends) - Time Series Analysis cơ bản.
        """
        print("\n--- Phân tích Xu hướng Giờ Điểm danh ---")
        df = self.df.copy()
        
        # Extract Hour and Minute
        df['hour_minute'] = df['timestamp'].dt.hour + df['timestamp'].dt.minute / 60.0
        
        # Calculate mean arrival time
        mean_arrival = df['hour_minute'].mean()
        hours = int(mean_arrival)
        minutes = int((mean_arrival - hours) * 60)
        print(f"Giờ đến trung bình của toàn công ty: {hours:02d}:{minutes:02d}")
        
        # Identify late arrivals (Assuming 08:00 is on-time)
        df['is_late'] = df['hour_minute'] > 8.0
        late_count = df['is_late'].sum()
        print(f"Tổng số lượt đi trễ: {late_count} / {len(df)} ({late_count/len(df)*100:.2f}%)")

    def forecast_attendance(self):
        """
        Dự báo số lượng người đi làm dựa trên trung bình trượt (Moving Average) - Kỹ thuật Time Series.
        """
        print("\n--- Dự báo Số lượng Nhân sự (Time-Series Forecasting) ---")
        df = self.df.copy()
        
        # Đếm số người có mặt theo ngày
        daily_counts = df.groupby(df['timestamp'].dt.date).size().reset_index(name='count')
        
        # Tính Moving Average 3 ngày
        daily_counts['MA_3'] = daily_counts['count'].rolling(window=3).mean()
        
        print("Dữ liệu 5 ngày gần nhất:")
        print(daily_counts.tail(5))
        
        last_ma = daily_counts['MA_3'].iloc[-1]
        print(f"-> Dựa trên MA(3), dự báo số nhân sự đi làm ngày mai là: ~{int(last_ma)} người.")

if __name__ == "__main__":
    analyzer = AttendanceAnalyzer()
    analyzer.analyze_arrival_patterns()
    analyzer.forecast_attendance()
