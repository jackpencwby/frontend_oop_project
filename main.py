search_hotel_endpoint = "http://127.0.0.1:8000/search/hotel"
search_reservation_endpoint = "http://127.0.0.1:8000/search/reservation"
login_endpoint = "http://127.0.0.1:8000/auth/login"
get_personal_information_endpoint = "http://127.0.0.1:8000/account/profile"
get_my_travelling_endpoint = "http://127.0.0.1:8000/account/MyReservation"

from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import date
import requests

# สร้างหน้าต่างหลัก
root = ttk.Window(themename="superhero")
root.title("เเอปจองโรงเเรม")
root.geometry("1280x720")

# สร้าง Frame แต่ละหน้า
frame_home = ttk.Frame(root)
frame_register = ttk.Frame(root)
frame_login = ttk.Frame(root)
frame_search_hotel = ttk.Frame(root)
frame_search_reservation = ttk.Frame(root)
frame_hotel = ttk.Frame(root)
frame_reservation = ttk.Frame(root)
frame_account = ttk.Frame(root)
frame_personal_information = ttk.Frame(root)
frame_my_travelling = ttk.Frame(root)
frame_my_favorite_hotel = ttk.Frame(root)

def show_page(page, current_frame=frame_home):
    current_frame.pack_forget()

    if page == "home_page":
        frame_home.pack()
    elif page == "register_page":
        frame_register.pack()
    elif page == "login_page":
        frame_login.pack()
    elif page == "search_hotel_page":
        frame_search_hotel.pack()
    elif page == "search_reservation_page":
        frame_search_reservation.pack()
    elif page == "hotel":
        frame_hotel.pack()
    elif page == "reservation":
        frame_reservation.pack()
    elif page == "account":
        frame_account.pack()
    elif page == "personal_information":
        frame_personal_information.pack()

def on_click_search_hotel_button():
    payload = {
        "country": country.get(),
        "province": province.get()
    }
    response = requests.post(search_hotel_endpoint, json=payload)
    if response.ok:
        data = response.json()
        ttk.Label(frame_hotel, text="ผลการค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(pady=30)
        row = 1
        for index_hotel in range(len(data)):
            ttk.Label(frame_hotel, text=""+str(data[index_hotel]["hotel_name"]), font=("Helvetica", 18), bootstyle="light").grid(row=row, column=0, ipady=20, sticky='w')
            ttk.Button(frame_hotel, text="เลือก", bootstyle="danger").grid(row=row, column=0, sticky='e')
            row += 1
        ttk.Button(frame_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("search_hotel_page", frame_hotel)).grid(row=6, column=0, pady=300, columnspan=2)
        show_page("hotel", frame_search_hotel)

def on_click_search_reservation_button():
    day, month, year = check_in_date.entry.get().split("/")
    date_list = [day, month, year]
    date = "-".join(date_list)
    payload = {
        "firstname": firstname.get(),
        "lastname": lastname.get(),
        "booking_no": booking_no.get(),
        "check_in_date": date
    }
    response = requests.post(search_reservation_endpoint, json=payload)
    if response.ok:
        data = response.json()
        ttk.Label(frame_reservation, text="ผลการค้นหาการจอง", font=("Helvetica", 36), bootstyle="light").grid(pady=30)
        ttk.Label(frame_reservation, text="ชื่อจริง : "+ str(data["firstname"]), font=("Helvetica", 18), bootstyle="danger").grid(row=1, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="นามสกุล : "+ str(data["lastname"]), font=("Helvetica", 18), bootstyle="danger").grid(row=2, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="หมายเลขการจอง : "+ str(data["booking_no"]), font=("Helvetica", 18), bootstyle="danger").grid(row=3, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="โรงเเรม : "+ str(data["hotel"]["hotel_name"]), font=("Helvetica", 18), bootstyle="danger").grid(row=4, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="ประเภทห้อง : "+ str(data["room_type"]), font=("Helvetica", 18), bootstyle="danger").grid(row=5, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="จำนวนห้อง : "+ str(data["room_quantity"]), font=("Helvetica", 18), bootstyle="danger").grid(row=6, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="วันที่เช็คอิน : "+ str(data["check_in_date"]), font=("Helvetica", 18), bootstyle="danger").grid(row=7, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="วันที่เช็คเอาท์ : "+ str(data["check_out_date"]), font=("Helvetica", 18), bootstyle="danger").grid(row=8, column=0, padx=10, ipady=10)
        ttk.Label(frame_reservation, text="สถานะ : "+ str(data["status"]), font=("Helvetica", 18), bootstyle="danger").grid(row=9, column=0,padx=10, ipady=10)
        ttk.Button(frame_reservation, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("search_reservation_page", frame_reservation)).grid(row=10, column=0, pady=50, columnspan=2)
        show_page("reservation", frame_search_reservation)
    
def on_click_login_button():
    payload = {
        "email": email.get(),
        "password": password.get(),
    }
    response = requests.post(login_endpoint, json=payload)
    if response.ok:
        show_page("account", frame_login)

def on_click_personal_information_button():
    response = requests.get(get_personal_information_endpoint)
    if response.ok:
        data = response.json()
        ttk.Label(frame_personal_information, text="ข้อมูลส่วนตัว", font=("Helvetica", 36), bootstyle="light").grid(pady=30)
        ttk.Label(frame_personal_information, text="ชื่อจริง : "+ str(data["firstname"]), font=("Helvetica", 18), bootstyle="danger").grid(row=1, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="นามสกุล : "+ str(data["lastname"]), font=("Helvetica", 18), bootstyle="danger").grid(row=2, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="ประเทศ : "+ str(data["country"]), font=("Helvetica", 18), bootstyle="danger").grid(row=3, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="จังหวัด: "+ str(data["province"]), font=("Helvetica", 18), bootstyle="danger").grid(row=4, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="รหัสไปรษณีย์ : "+ str(data["zip_code"]), font=("Helvetica", 18), bootstyle="danger").grid(row=5, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="วันเกิด: "+ str(data["birthday"]), font=("Helvetica", 18), bootstyle="danger").grid(row=6, column=0, padx=10, ipady=10)
        ttk.Label(frame_personal_information, text="เบอร์โทรศัพท์ : "+ str(data["phone_number"]), font=("Helvetica", 18), bootstyle="danger").grid(row=7, column=0, padx=10, ipady=10)
        ttk.Button(frame_personal_information, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("account", frame_personal_information)).grid(row=8, column=0, pady=200, columnspan=2)
        show_page("personal_information", frame_account)

def on_click_my_travelling_button():
    response = requests.get(get_my_travelling_endpoint)
    if response.ok:
        data = response.json()
        pass
        
def on_click_my_favorite_hotel_button():
    pass

province = StringVar()
country = StringVar()
firstname = StringVar()
lastname = StringVar()
booking_no = StringVar()
email = StringVar()
password = StringVar()

# เนื้อหาในหน้า homepage
ttk.Label(frame_home, text="เเอปจองโรงเเรม", font=("Helvetica", 36), bootstyle="light").pack(pady=30)
ttk.Button(frame_home, text="สมัครสมาชิก", command=lambda: show_page("register_page"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="เข้าสู่ระบบ", command=lambda: show_page("login_page"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel_page"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาการจอง", command=lambda: show_page("search_reservation_page"), bootstyle="danger").pack(pady=30)

# เนื้อหาในหน้า register
ttk.Label(frame_register, text="สมัครสมาชิก", font=("Helvetica", 36), bootstyle="light").pack(pady=30)

# เนื้อหาในหน้า login
ttk.Label(frame_login, text="เข้าสู่ระบบ", font=("Helvetica", 36), bootstyle="light").grid(ipady=30, columnspan=2)
ttk.Label(frame_login, text="อีเมล :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=30)
ttk.Entry(frame_login, textvariable=email, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_login, text="รหัสผ่าน :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_login, textvariable=password, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_login, text="เข้าสู่ระบบ", bootstyle="danger", command=on_click_login_button).grid(row=3, column=0, pady=30, columnspan=2)
ttk.Button(frame_login, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home_page", frame_login)).grid(row=8, column=0, pady=300, columnspan=2)

# เนื้อหาในหน้า search_hotel
ttk.Label(frame_search_hotel, text="ค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(row=0, column=0, ipady=30, columnspan=2)
ttk.Label(frame_search_hotel, text="ประเทศ :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=30)
ttk.Entry(frame_search_hotel, textvariable=country, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_search_hotel, text="จังหวัด :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_search_hotel, textvariable=province, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_search_hotel, text="ค้นหาโรงเเรม", bootstyle="danger", command=on_click_search_hotel_button).grid(row=3, column=0, pady=30, columnspan=2)
ttk.Button(frame_search_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home_page", frame_search_hotel)).grid(row=8, column=0, pady=300, columnspan=2)

# เนื้อหาในหน้า search_reservation
ttk.Label(frame_search_reservation, text="ค้นหาการจอง", font=("Helvetica", 36), bootstyle="light").grid(row=0, column=0, ipady=30, columnspan=2)
ttk.Label(frame_search_reservation, text="ชื่อจริง :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation, textvariable=firstname, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_search_reservation, text="นามสกุล :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation,  textvariable=lastname, width=20).grid(row=2, column=1, padx=10)
ttk.Label(frame_search_reservation, text="หมายเลขการจอง :", font=("Helvetica", 18), bootstyle="light").grid(row=3, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation, textvariable=booking_no, width=20).grid(row=3, column=1, padx=10)
ttk.Label(frame_search_reservation, text="วันที่เช็คอิน :", font=("Helvetica", 18), bootstyle="light").grid(row=4, column=0, padx=10, ipady=15)
check_in_date = ttk.DateEntry(frame_search_reservation, bootstyle="danger", startdate=date.today())
check_in_date.grid(row=4, column=1, padx=10)
ttk.Button(frame_search_reservation, text="ค้นหาการจอง", bootstyle="danger", command=on_click_search_reservation_button).grid(row=5, column=0, pady=30, columnspan=2)
ttk.Button(frame_search_reservation, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home_page", frame_search_reservation)).grid(row=6, column=0, pady=200, columnspan=2)

# เนื้อหาในหน้า account
ttk.Button(frame_account, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel_page", frame_account), bootstyle="danger").pack(pady=30)
ttk.Button(frame_account, text="ค้นหาการจอง", command=lambda: show_page("search_reservation_page", frame_account), bootstyle="danger").pack(pady=30)
ttk.Button(frame_account, text="ข้อมูลส่วนตัว", command=on_click_personal_information_button, bootstyle="danger").pack(pady=30)
# ttk.Button(frame_account, text="การเดินทางของฉัน", command=lambda: show_page(), bootstyle="danger").pack(pady=30)
# ttk.Button(frame_account, text="โรงเเรมที่ฉันชื่นชอบ", command=lambda: show_page(), bootstyle="danger").pack(pady=30)

# เนื้อหาในหน้าข้อมูลส่วนตัว

# เนื้อหาในหน้า account

# เนื้อหาในหน้า account





# แสดงหน้าแรกในตอนเริ่มต้น
current_frame = frame_home
current_frame.pack()

# เริ่มลูปหลัก
root.mainloop()
