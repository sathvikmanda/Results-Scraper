import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


csv_file = "roll.csv"
url = "https://gradesresults.griet.in/results.php?result=GR22:2024-25:A:320:REGULAR:AUGUST"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        hallticket = row[0].strip()
        if not hallticket:
            continue
        print(f"Fetching results for: {hallticket}")

        driver.get(url)
        time.sleep(1)
        input_box = wait.until(EC.element_to_be_clickable((By.NAME, "rollno")))
        input_box.clear()
        input_box.send_keys(hallticket)
        input_box.send_keys(Keys.RETURN)

    time.sleep(60)  

driver.quit()
