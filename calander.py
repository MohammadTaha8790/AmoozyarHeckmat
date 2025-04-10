from datetime import datetime

def formatted_date():
    # دریافت تاریخ کنونی
    now = datetime.now()

    # قالب‌بندی تاریخ
    formatted = now.strftime("%A, %d %B %Y | %H:%M:%S")
    return formatted

# چاپ تاریخ
print("📅 تاریخ و زمان فعلی:")
print(formatted_date())