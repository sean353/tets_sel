from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# פתיחת דפדפן (למשל Chrome)
driver = webdriver.Chrome()

# פתיחת עמוד הלוגין של פייסבוק
driver.get("https://www.facebook.com/?locale=he_IL")

# חיפוש שדה שם המשתמש והזנת מידע
username_field = driver.find_element(By.ID, "email")
for char in "your_username":  # החלף עם שם המשתמש שלך
    username_field.send_keys(char)
    time.sleep(0.01)  # השהייה בין התווים

# חיפוש שדה הסיסמה והזנת מידע
password_field = driver.find_element(By.ID, "pass")
for char in "your_password":  # החלף עם הסיסמה שלך
    password_field.send_keys(char)
    time.sleep(0.01)   # השהייה בין התווים

# לחיצה על כפתור הלוגין
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# השהייה ארוכה כדי לשמור על החלון פתוח
time.sleep(60)  # תוכל לשנות את הזמן לפי הצורך

# אם אתה רוצה להפסיק את הסקריפט ידנית, תוכל להוסיף:
input("Press Enter to exit...")  # מחכה ללחיצה על Enter

# סגירת הדפדפן
driver.quit()  # זה יקרה רק לאחר הלחיצה על Enter
