from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)





#Base url http://shop.demoqa.com/

driver.get("https://shop.demoqa.com/my-account/")

# Login in to a pre created account
username_name = driver.find_element_by_id("username")
username_name.clear()
username_name.send_keys("Logan")

password_name = driver.find_element_by_id("password")
password_name.clear()
password_name.send_keys("Warsong69")

login = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button").click()

driver.get("https://shop.demoqa.com/wishlist/")

# Choose any item and select it.
driver.find_element_by_xpath("//*[contains(text(),'Black Cross Back Maxi Dress')]").click()

# Choose a color option (Color) and a size option (Size)
driver.find_element_by_xpath("//select[@name='attribute_pa_color']/option[@value='black']").click()
driver.find_element_by_xpath("//select[@name='attribute_pa_size']/option[@value='medium']").click()

# Click add to cart
driver.find_element_by_xpath("//*[contains(text(),'Add to cart')]").click()


# A success message should pop up
message_alert = driver.find_element_by_xpath("//div[@class='woocommerce-message']")


# Going to the cart  via view cart button
driver.find_element_by_xpath("//a[contains(text(),'View cart')]").click()

# Choosing a dress that has been saved to the wishlist.
cart_count = driver.find_element_by_xpath("//span[@class='cart-count']")
cart_total = driver.find_element_by_xpath("//span[@class='woocommerce-Price-currencySymbol']")


# Clicking the checkout button to move forward.
driver.find_element_by_xpath("//*[contains(text(),'Proceed to checkout')]").click()

time.sleep(2)
# Filling out the required fields and checking terms and conditions.
first_name = driver.find_element_by_id("billing_first_name")
first_name.clear()
first_name.send_keys("Logan")

last_name = driver.find_element_by_id("billing_last_name")
last_name.clear()
last_name.send_keys("Gustafson")

driver.find_element_by_xpath("//select[@name='billing_country']/option[@value='GR']").click()


address = driver.find_element_by_id("billing_address_1")
address.clear()
address.send_keys("454 E 1370 N")

code_postale = driver.find_element_by_id("billing_postcode")
code_postale.clear()
code_postale.send_keys("84074")

city = driver.find_element_by_id("billing_city")
city.clear()
city.send_keys("tooele")

phone = driver.find_element_by_id("billing_phone")
phone.clear()
phone.send_keys("4352288883")

email = driver.find_element_by_id("billing_email")
email.clear()
email.send_keys("fake11@email.com")

# I HAVE READ AND AGREE TO THE WEBSITETERMS AND CONDITIONS
time.sleep(2)
terms = driver.find_element_by_id("terms")
terms.click()

# Clicking the «PLACE ORDER» button
driver.find_element_by_id("place_order").click()

# a succsess messsage should show up.
thankyou = driver.find_element_by_xpath("//*[@class='woocommerce-thankyou-order-received']")
assert thankyou.text == 'Thank you. Your order has been received.'


time.sleep(3)
driver.close()