from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from password_encryption import password, username
import time

# Set the path to the ChromeDriver executable
chromedriver_path = "/Users/mohamedabuomar/Downloads/chromedriver_mac_arm64/chromedriver.exe"
print(username)

# Create a Service object with the path to the ChromeDriver
service = Service(chromedriver_path)
def get_text_content():
# Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service)

    # Open the Koodo Mobile login page
    driver.get("https://identity.koodomobile.com/as/authorization.oauth2?client_id=214aa452-c949-4895-9a9f-5e8b18d9a9a1&response_type=code&scope=profileinfohighdetail%20customerinfo%20securitymgmt%20paymentmanagement%20ordermgmt%20invoicedocuments%20cmscustomerbillmanagement%20customerbillmanagement%20invoiceinfo%20devicemanagement%20phonenumbermgmt%20accountinfo%20accountmanagement%20loyaltyandrewards%20priceplaninfo%20accountactivity%20paymentprocessing%20profilemanagement%20usagepreferencemanagement%20usagemeter%20wlspaymentmgmt%20usagemanagement%20usagedetails%20usageblockmanagement%20serviceeligibility%20servicemanagement%20onetimepasscode%20hellocustomer%20billpreferencemanagement%20identityinfofulldetail%20serviceassociation%20callcontrolmanagement%20wlsserviceagreement%20wlsserviceandfeature%20wlspriceplan%20userprofileselfreg%20userprofileselflink%20paymentManagement%20clientIdentityOneTimePasscode%20paymentMethods%20billmgmt&redirect_uri=https%3A%2F%2Fproxy.digital.koodomobile.com%2Foauth2%2Fcallback")

    # Find the username and password input fields
    username_field = driver.find_element(By.ID, "idtoken1")
    password_field= driver.find_element(By.ID, "idtoken2")

    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div[4]/button')
    login_button.click()


    # Wait for the button to be clickable and click it, going to the self serve section
    try:
        self_serve_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="li-self-serve-4423"]/a')))
        self_serve_button.click()
    except:
        print("Button not found or not clickable")

    # Wait for the button to be clickable and click it, going to the self serve drop down section
    try:
        self_serve_dropdown_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/div/header/span[2]/div/div[2]/div/div[1]/div/div/div[2]/button/span/strong')))
        self_serve_dropdown_button.click()
    except:
        print("selfserve drop down Button not found or not clickable")

    # Wait for the button to be clickable and click it, going to the usage section

    try:
        usage_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/div/header/span[2]/div/div[2]/div/div[1]/div/div/div[2]/div/ul/li[3]/div/a/div')))
        usage_button.click()
    except:
        print("usage Button not found or not clickable")

    # Wait for the button to be clickable and click it, going to the specific number
    try:
        number_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content-9054623030"]')))
        number_button.click()
    except:
        print("Number Button not found or not clickable")


    element = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[4]/div/div/span[2]')))
    days_content = element.text
    print(days_content)


    # Wait for the button to be clickable and click it, going to data details

    try:
        details_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[3]/a')))
        details_button.click()
    except:
        print("Number Button not found or not clickable")




    element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/table/tfoot/tr/td[3]')))
    text_content = element.text
    print(text_content)
    # input("Press Enter to close the browser...")
    driver.quit()
    return text_content, days_content

# get_text_content()




# Wait for user interaction before closing the browser

# Close the browser

