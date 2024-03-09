from datetime import date

date1 = "14-3-2548"
day, month, year = date1.split("-")
date1_new = date(int(year), int(month), int(day)).strftime("%d-%m-%Y")
print(date1_new)