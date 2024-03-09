search_hotel_endpoint = "http://127.0.0.1:8000/search/hotel"
search_reservation_endpoint = "http://127.0.0.1:8000/search/reservation"
login_endpoint = "http://127.0.0.1:8000/auth/login"
logout_endpoint = "http://127.0.0.1:8000/auth/logout"
register_endpoint = "http://127.0.0.1:8000/auth/register"
get_personal_information_endpoint = "http://127.0.0.1:8000/account/profile"
get_my_travelling_endpoint = "http://127.0.0.1:8000/account/MyReservations"
get_my_favorite_hotel_end_point = "http://127.0.0.1:8000/account/MyFavoriteHotel"

from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import date
import requests

# สร้างหน้าต่างหลัก
root = ttk.Window(themename="cyborg")
root.title("เเอปจองโรงเเรม")
root.geometry("1280x720")

#สร้าง Notebook
style = ttk.Style()
style.configure("TNotebook.Tab", font=('Helvetica', 16))
my_travelling_notebook = ttk.Notebook(root, bootstyle="cyborg", width=1280, height=720)

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
frame_my_favorite_hotel = ttk.Frame(root)
arriving_tab = ttk.Frame(my_travelling_notebook)
cancelled_tab = ttk.Frame(my_travelling_notebook)

# ฟังก์ชันสำหรับการเปลี่ยนหน้าไปมา
def show_page(page, current_frame=frame_home):
    current_frame.pack_forget()

    if page == "home":
        frame_home.pack()
    elif page == "register":
        frame_register.pack()
    elif page == "login":
        frame_login.pack()
    elif page == "search_hotel":
        frame_search_hotel.pack()
    elif page == "search_reservation":
        frame_search_reservation.pack()
    elif page == "hotel":
        frame_hotel.pack()
    elif page == "reservation":
        frame_reservation.pack()
    elif page == "account":
        frame_account.pack()
    elif page == "personal_information":
        frame_personal_information.pack()
    elif page == "my_travelling":
        my_travelling_notebook.pack()
        my_travelling_notebook.add(arriving_tab, text="กำลังจะมาถึง")
        my_travelling_notebook.add(cancelled_tab, text="ยกเลิกเเล้ว")
    elif page == "my_favorite_hotel":
        frame_my_favorite_hotel.pack()

def on_click_search_hotel_button():
    payload = {
        "country": country.get(),  
        "province": province.get()
    }
    response = requests.post(search_hotel_endpoint, json=payload)
    if response.ok:
        data = response.json()
        print(data)
        ttk.Label(frame_hotel, text="ผลการค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(pady=30)
        row = 1
        for index_hotel in range(len(data)):
            ttk.Label(frame_hotel, text=""+str(data[index_hotel]["hotel_name"]), font=("Helvetica", 18), bootstyle="light").grid(row=row, column=0, ipady=20, sticky='w')
            ttk.Button(frame_hotel, text="เลือก", bootstyle="danger").grid(row=row, column=0, sticky='e')
            row += 1
        ttk.Button(frame_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("search_hotel", frame_hotel)).grid(row=6, column=0, pady=300, columnspan=2)
        show_page("hotel", frame_search_hotel)

def on_click_search_reservation_button():
    day, month, year = check_in_date.entry.get().split("/")
    Date = date(int(year), int(month), int(day)).strftime("%d-%m-%Y")
    payload = {
        "firstname": firstname.get(),
        "lastname": lastname.get(),
        "booking_no": booking_no.get(),
        "check_in_date": Date
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
        ttk.Button(frame_reservation, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("search_reservation", frame_reservation)).grid(row=10, column=0, pady=50, columnspan=2)
        show_page("reservation", frame_search_reservation)
    
def on_click_login_button():
    payload = {
        "email": email.get(),
        "password": password.get(),
    }
    response = requests.post(login_endpoint, json=payload)
    if response.ok:
        ttk.Button(frame_account, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel", frame_account), bootstyle="danger").pack(pady=30)
        ttk.Button(frame_account, text="ค้นหาการจอง", command=lambda: show_page("search_reservation", frame_account), bootstyle="danger").pack(pady=30)
        ttk.Button(frame_account, text="ข้อมูลส่วนตัว", command=on_click_personal_information_button, bootstyle="danger").pack(pady=30)
        ttk.Button(frame_account, text="การเดินทางของฉัน", command=on_click_my_travelling_button, bootstyle="danger").pack(pady=30)
        ttk.Button(frame_account, text="โรงเเรมที่ฉันชื่นชอบ", command=on_click_my_favorite_hotel_button, bootstyle="danger").pack(pady=30)
        ttk.Button(frame_account, text="ออกจากระบบ", command=on_click_logout_button, bootstyle="secondary").pack(pady=60)
        show_page("account", frame_login)

def on_click_logout_button():
    response = requests.put(logout_endpoint)
    if response.ok:
        show_page("login", frame_account)

def on_click_register_button():
    day, month, year = birthday.entry.get().split("/")
    birthday_date = date(int(year), int(month), int(day)).strftime("%d-%m-%Y")
    payload = {
        "firstname": firstname.get(),
        "lastname": lastname.get(),
        "country": country.get(),
        "province": province.get(),
        "country": country.get(),
        "zip_code": zip_code.get(),
        "birthday": birthday_date,
        "phone_number": phone_number.get(),
        "email": email.get(),
        "password": password.get(),
        "confirm_password": confirm_password.get()
    }

    response = requests.post(register_endpoint, json=payload)
    if response.ok:
        show_page("login", frame_register)

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
        print(data)
        arriving = data["arriving"]
        cancelled = data["cancelled"]
        for index_reservation in range(len(arriving)):
            ttk.Label(arriving_tab, text="ชื่อจริง : "+ str(arriving[index_reservation]["firstname"]), font=("Helvetica", 14), bootstyle="danger").grid(row=0, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="นามสกุล : "+ str(arriving[index_reservation]["lastname"]), font=("Helvetica", 14), bootstyle="danger").grid(row=1, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="หมายเลขการจอง : "+ str(arriving[index_reservation]["booking_no"]), font=("Helvetica", 14), bootstyle="danger").grid(row=2, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="โรงเเรม : "+ str(arriving[index_reservation]["hotel"]["hotel_name"]), font=("Helvetica", 14), bootstyle="danger").grid(row=3, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="ประเภทห้อง : "+ str(arriving[index_reservation]["room_type"]), font=("Helvetica", 14), bootstyle="danger").grid(row=4, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="จำนวนห้อง : "+ str(arriving[index_reservation]["room_quantity"]), font=("Helvetica", 14), bootstyle="danger").grid(row=5, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="วันที่เช็คอิน : "+ str(arriving[index_reservation]["check_in_date"]), font=("Helvetica", 14), bootstyle="danger").grid(row=6, column=0, padx=20, ipady=10)
            ttk.Label(arriving_tab, text="วันที่เช็คเอาท์ : "+ str(arriving[index_reservation]["check_out_date"]), font=("Helvetica", 14), bootstyle="danger").grid(row=7, column=0, padx=20, ipady=10)
            ttk.Button(arriving_tab, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("account", my_travelling_notebook)).grid(row=8, column=0, pady=100)
        for index_reservation in range(len(cancelled)):
            ttk.Label(cancelled_tab, text="ชื่อจริง : "+ str(cancelled[index_reservation]["firstname"]), font=("Helvetica", 14), bootstyle="danger").grid(row=0, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="นามสกุล : "+ str(cancelled[index_reservation]["lastname"]), font=("Helvetica", 14), bootstyle="danger").grid(row=1, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="หมายเลขการจอง : "+ str(cancelled[index_reservation]["booking_no"]), font=("Helvetica", 14), bootstyle="danger").grid(row=2, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="โรงเเรม : "+ str(cancelled[index_reservation]["hotel"]["hotel_name"]), font=("Helvetica", 14), bootstyle="danger").grid(row=3, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="ประเภทห้อง : "+ str(cancelled[index_reservation]["room_type"]), font=("Helvetica", 14), bootstyle="danger").grid(row=4, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="จำนวนห้อง : "+ str(cancelled[index_reservation]["room_quantity"]), font=("Helvetica", 14), bootstyle="danger").grid(row=5, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="วันที่เช็คอิน : "+ str(cancelled[index_reservation]["check_in_date"]), font=("Helvetica", 14), bootstyle="danger").grid(row=6, column=0, padx=20, ipady=10)
            ttk.Label(cancelled_tab, text="วันที่เช็คเอาท์ : "+ str(cancelled[index_reservation]["check_out_date"]), font=("Helvetica", 14), bootstyle="danger").grid(row=7, column=0, padx=20, ipady=10)
            ttk.Button(cancelled_tab, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("account", my_travelling_notebook)).grid(row=8, column=0, pady=100)
        show_page("my_travelling", frame_account)
        
def on_click_my_favorite_hotel_button():
    response = requests.get(get_my_favorite_hotel_end_point)
    if response.ok:
        data = response.json()
        ttk.Label(frame_my_favorite_hotel, text="โรงเเรมที่ฉันชื่นชอบ", font=("Helvetica", 36), bootstyle="light").grid(pady=30)
        if isinstance(data, dict):
            ttk.Label(frame_my_favorite_hotel, text="ไม่มีโรงเเรมที่คุณชื่นชอบ", font=("Helvetica", 18), bootstyle="danger").grid(row=1, column=0, padx=20, ipady=10)
        else:
            for index_my_favorite_hotel in range(len(data)):
                ttk.Label(frame_my_favorite_hotel, text="ชื่อจริง : "+ str(data[index_my_favorite_hotel]["hotel_name"]), font=("Helvetica", 18), bootstyle="danger").grid(row=1, column=0, padx=20, ipady=10)
        ttk.Button(frame_my_favorite_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("account", frame_my_favorite_hotel)).grid(row=8, column=0, pady=100)   
        show_page("my_favorite_hotel", frame_account)
        
province = StringVar()
country = StringVar()
firstname = StringVar()
lastname = StringVar()
booking_no = StringVar()
email = StringVar()     
password = StringVar()
confirm_password = StringVar()
zip_code = StringVar()
phone_number = StringVar()


# เนื้อหาในหน้า homepage
ttk.Label(frame_home, text="เเอปจองโรงเเรม", font=("Helvetica", 36), bootstyle="light").pack(pady=30)
ttk.Button(frame_home, text="สมัครสมาชิก", command=lambda: show_page("register"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="เข้าสู่ระบบ", command=lambda: show_page("login"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาการจอง", command=lambda: show_page("search_reservation"), bootstyle="danger").pack(pady=30)

# เนื้อหาในหน้า register
def set_input_register():
    firstname.set("customer")
    lastname.set("3")
    country.set("Thailand")
    province.set("Bangkok")
    zip_code.set("10520")
    phone_number.set("0929677181")
    email.set("customer3@gmail.com")
    password.set("customer3")
    confirm_password.set("customer3")

ttk.Label(frame_register, text="สมัครสมาชิก", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_register, text="ชื่อจริง:", font=("Helvetica", 15), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=firstname, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_register, text="นามสกุล:", font=("Helvetica", 15), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=lastname, width=20).grid(row=2, column=1, padx=10)
ttk.Label(frame_register, text="ประเทศ:", font=("Helvetica", 15), bootstyle="light").grid(row=3, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=country, width=20).grid(row=3, column=1, padx=10)
ttk.Label(frame_register, text="จังหวัด :", font=("Helvetica", 15), bootstyle="light").grid(row=4, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=province, width=20).grid(row=4, column=1, padx=10)
ttk.Label(frame_register, text="รหัสไปรษณีย์ :", font=("Helvetica", 15), bootstyle="light").grid(row=5, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=zip_code, width=20).grid(row=5, column=1, padx=10)
ttk.Label(frame_register, text="วันเกิด:", font=("Helvetica", 15), bootstyle="light").grid(row=6, column=0, padx=10, ipady=10)
birthday = ttk.DateEntry(frame_register, bootstyle="danger", startdate=date.today())
birthday.grid(row=6, column=1, padx=10)
ttk.Label(frame_register, text="เบอร์โทรศัพท์ :", font=("Helvetica", 15), bootstyle="light").grid(row=7, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=phone_number, width=20).grid(row=7, column=1, padx=10)
ttk.Label(frame_register, text="อีเมล:", font=("Helvetica", 15), bootstyle="light").grid(row=8, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=email, width=20).grid(row=8, column=1, padx=10)
ttk.Label(frame_register, text="รหัสผ่าน:", font=("Helvetica", 15), bootstyle="light").grid(row=9, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=password, width=20).grid(row=9, column=1, padx=10)
ttk.Label(frame_register, text="ยืนยันรหัสผ่าน:", font=("Helvetica", 15), bootstyle="light").grid(row=10, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=confirm_password, width=20).grid(row=10, column=1, padx=10)
ttk.Button(frame_register, text="สมัครสมาชิก", bootstyle="danger", command=on_click_register_button).grid(row=11, column=0, pady=20, columnspan=2)
ttk.Button(frame_register, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_register)).grid(row=12, pady=20, columnspan=2)
set_input_register()

# เนื้อหาในหน้า login
ttk.Label(frame_login, text="เข้าสู่ระบบ", font=("Helvetica", 36), bootstyle="light").grid(ipady=30, columnspan=2)
ttk.Label(frame_login, text="อีเมล :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=30)
ttk.Entry(frame_login, textvariable=email, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_login, text="รหัสผ่าน :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_login, textvariable=password, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_login, text="เข้าสู่ระบบ", bootstyle="danger", command=on_click_login_button).grid(row=3, column=0, pady=30, columnspan=2)
ttk.Button(frame_login, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_login)).grid(row=8, column=0, pady=300, columnspan=2)

# เนื้อหาในหน้า search_hotel
ttk.Label(frame_search_hotel, text="ค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(row=0, column=0, ipady=30, columnspan=2)
ttk.Label(frame_search_hotel, text="ประเทศ :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=30)
ttk.Entry(frame_search_hotel, textvariable=country, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_search_hotel, text="จังหวัด :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_search_hotel, textvariable=province, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_search_hotel, text="ค้นหาโรงเเรม", bootstyle="danger", command=on_click_search_hotel_button).grid(row=3, column=0, pady=30, columnspan=2)
ttk.Button(frame_search_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_search_hotel)).grid(row=8, column=0, pady=300, columnspan=2)

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
ttk.Button(frame_search_reservation, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_search_reservation)).grid(row=6, column=0, pady=200, columnspan=2)

# เนื้อหาในหน้าข้อมูลส่วนตัว


# แสดงหน้าแรกในตอนเริ่มต้น
current_frame = frame_home
current_frame.pack()

# เริ่มลูปหลัก
root.mainloop()
