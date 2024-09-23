from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# פתיחת דפדפן (למשל Chrome)
driver = webdriver.Chrome()

# פתיחת עמוד הלוגין של Flask (החלף לכתובת שלך אם שונה)
driver.get("http://127.0.0.1:5000/login")

# חיפוש שדה שם המשתמש והזנת מידע
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("admin")  # שם המשתמש הנכון

# חיפוש שדה הסיסמה והזנת מידע
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("1234")  # סיסמה נכונה

# לחיצה על כפתור הלוגין
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# השהייה של מספר שניות לראות את התוצאה
time.sleep(5)

# סגירת הדפדפן
driver.quit()
