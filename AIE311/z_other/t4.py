import csv
import os
from collections import Counter
import customtkinter as ctk
from tkinter import messagebox
idx= 290
# ฟังก์ชั่นในการหาค่า Mode
def find_mode(data):
    if not data:
        return None
    count = Counter(data)
    mode_data = count.most_common(1)
    return mode_data[0][0]

# ฟังก์ชั่นในการตรวจสอบขนาดของไฟล์และจำนวนแถวในไฟล์
def check_csv_file(filename):
    if not os.path.exists(filename):
        return 0
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        row_count = sum(1 for _ in reader)
        return row_count

# ฟังก์ชั่นในการเขียนข้อมูลลงไฟล์ CSV
def write_to_csv(filename, rows):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# ฟังก์ชั่นในการเพิ่ม Header ใหม่ในไฟล์ CSV เดิม
def add_new_column(filename):
    # อ่านข้อมูลทั้งหมดในไฟล์เดิม
    with open(filename, mode='r', newline='') as read_file:
        reader = csv.reader(read_file)
        rows = list(reader)
    
    # เพิ่มคอลัมน์ว่างในแต่ละแถว
    new_rows = [row + [""] for row in rows]

    # เพิ่ม Header ใหม่
    new_rows.append(["Time-Start", "Time-End", "RSSI"])
    # เขียนข้อมูลกลับไปที่ไฟล์เดิม
    with open(filename, mode='w', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(new_rows)
        

    messagebox.showinfo("Success", f"เพิ่มคอลัมน์ใหม่ในไฟล์ {filename} เรียบร้อยแล้ว!")

# ฟังก์ชั่นในการประมวลผลข้อมูลที่ใส่เข้ามา
def process_input(input_text):
    rssi_list = []
    time_list = []
    start_time = None

    # แยกข้อมูลเวลาและค่า RSSI ออกจากข้อมูลที่รับเข้ามา
    try:
        input_lines = input_text.splitlines()
        for user_input in input_lines:
            parts = user_input.split(" -> ")
            time_part = parts[0]
            rssi_value = int(parts[1].split(",")[1])

            # เก็บค่าที่รับมาใน list
            if start_time is None:
                start_time = time_part

            rssi_list.append(rssi_value)
            time_list.append(time_part)

    except (IndexError, ValueError):
        messagebox.showerror("Error", "ข้อมูลไม่ถูกต้อง กรุณาใส่ข้อมูลในรูปแบบ: 13:48:30.873 -> R24080016,-71")
        return

    # คำนวณ Mode ของค่า RSSI ที่เก็บได้
    mode_rssi = find_mode(rssi_list)

    if mode_rssi is None:
        messagebox.showwarning("Warning", "ไม่มีข้อมูลเพียงพอในการคำนวณ Mode กรุณาใส่ข้อมูล RSSI ที่ถูกต้อง.")
        return

    # นำเครื่องหมาย '-' ออกจาก RSSI ก่อนเขียนลงไฟล์
    mode_rssi = abs(mode_rssi)

    # หาเวลาที่น้อยที่สุดในชุดข้อมูลสำหรับ Time-End (ไม่รวมแถวแรก)
    if len(time_list) > 1:
        time_end = min(time_list[1:])
    else:
        time_end = time_list[0]

    # เขียนข้อมูลลงไฟล์ CSV
    write_to_csv(filename, [[start_time, time_end, mode_rssi]])

    messagebox.showinfo("Success", f"ข้อมูลถูกเขียนลงไฟล์ {filename} แล้ว")

# ฟังก์ชั่นสำหรับปุ่ม Submit
def submit_action():
    input_text = input_textbox.get("1.0", "end").strip()
    if input_text:
        process_input(input_text)
        input_textbox.delete("1.0", "end")  # ล้างข้อมูลในช่อง input
    else:
        messagebox.showwarning("Warning", "กรุณาใส่ข้อมูลในช่องรับข้อมูล")

# ฟังก์ชั่นสำหรับปุ่ม New Column
def new_column_action():
    add_new_column(filename)

# ชื่อไฟล์ CSV ที่จะบันทึกข้อมูล
filename = "R24020016 - R24020016.csv"
# ตรวจสอบจำนวนแถวในไฟล์
row_count = check_csv_file(filename)


# ถ้าไฟล์ไม่มีข้อมูล ให้สร้างไฟล์ใหม่และเขียน Header
if row_count == 0:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time-Start", "Time-End", "RSSI"])

# สร้าง GUI ด้วย customtkinter
ctk.set_appearance_mode("dark")  # โหมดสีเข้ม
ctk.set_default_color_theme("dark-blue")  # ธีมสี

app = ctk.CTk()  # สร้างหน้าต่างหลัก
app.title("CSV Data Logger")  # กำหนดชื่อหน้าต่าง
app.geometry("600x400")  # กำหนดขนาดหน้าต่าง

# สร้างช่องใส่ข้อมูลขนาดใหญ่
input_textbox = ctk.CTkTextbox(app, width=500, height=200, font=("Arial", 14))
input_textbox.pack(pady=20)

# สร้างปุ่ม Submit
submit_button = ctk.CTkButton(app, text="Submit", command=submit_action)
submit_button.pack(pady=10)

# สร้างปุ่ม New Column
new_column_button = ctk.CTkButton(app, text="New Column", command=new_column_action)
new_column_button.pack(pady=10)

app.mainloop()
