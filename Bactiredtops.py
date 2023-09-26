from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

def main():
    edge_driver_path = r'C:\Users\s176444\Downloads\edgedriver_win32\msedgedriver.exe'
    
    driver = webdriver.Edge(executable_path=edge_driver_path)
    driver.get("https://forms.office.com/pages/responsepage.aspx?id=xHuKPzfjpUeg_A1RLA4F8dP8_fMEmf1GnO1IU2HCna5UNEJHU0JVRzFSMVpNV0pOT0tFQVpHUFVQNi4u")
    
    wait = WebDriverWait(driver, 5)

    fill_date(driver, wait)
    fill_code_collected_by(driver, wait)
    click_submit(driver, wait)

    driver.quit()

    print("Success: Entire task completed!")

def fill_date(driver, wait):
    date_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/input')))
    current_date_str = datetime.now().strftime("%m/%d/%Y")
    date_input.clear()
    date_input.send_keys(current_date_str)

def fill_code_collected_by(driver, wait):
    code_collected_by_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input')))
    code_collected_by_input.clear()
    code_collected_by_input.send_keys("ERCOLLECT")

def click_submit(driver, wait):
    onsubmit_end = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[3]/div/button')))
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", onsubmit_end)
    time.sleep(2)
    
    # Attempt clicking using ActionChains
    try:
        actions = ActionChains(driver)
        actions.move_to_element(onsubmit_end).click().perform()
        time.sleep(5)  # Holding for 10 seconds
        print("Success: Button clicked successfully!")
    except Exception as e:
        print(f"Error: Failed to click the button. Reason: {str(e)}")
        # Fallback to JavaScript click if ActionChains fail
        driver.execute_script("arguments[0].click();", onsubmit_end)

if __name__ == '__main__':
    main()
