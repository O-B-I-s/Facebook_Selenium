import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.facebook.com/')
time.sleep(2)

input('Press enter to continue')

element = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Menu"][role="button"]')
element.click()
time.sleep(2)

group_page = WebDriverWait(driver, 1800).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Connect with people who share your interests."]')))
group_page.click()
# Increase timeout and add delay
time.sleep(2)

# Wait for the "See all" element to be clickable directly
see_all_groups = driver.find_element(By.XPATH, '//a[@href="/groups/joins/?nav_source=tab"]')

#     WebDriverWait(driver, 60).until(
#     EC.element_to_be_clickable((By.XPATH, '//a[contains(@aria-label, "See all")]'))
# ))

# Click the element directly
see_all_groups.click()
time.sleep(3)
messages = [
    "Hello, nice to be here! Hope I'm welcomed.",
    "Hi everyone! Glad to join this group, looking forward to connecting with you all.",
    "Hey! Excited to be here, hope to have some great conversations!",
    "Hi there! Just joined, happy to be part of this community.",
    "Hello everyone! Looking forward to learning and growing with you all.",
    "Hi folks! Just joined, hope to make some great connections here.",
    "Hey everyone! New here, excited to see what this group is all about!",
    "Hello! Happy to join the group, hope I'm welcomed!",
    "Hey guys! Just landed here, looking forward to some great interactions!",
    "Hi everyone! Just joined, hoping to have some meaningful discussions here.",
    "Hello! Excited to be here and connect with you all.",
    "Hey there! New to the group, can’t wait to get to know you all.",
    "Hi everyone! Looking forward to sharing and learning with you all.",
    "Hello! Just joined the group, hope to have some fun discussions!",
    "Hey all! Glad to be here, hoping to contribute and learn from everyone.",
    "Hi everyone! Excited to join the group, let's make this fun!",
    "Hello! Happy to be part of this community, looking forward to engaging with you all.",
    "Hey folks! Just joined, can't wait to meet you all and get involved.",
    "Hi everyone! New member here, hope to have some interesting conversations!",
    "Hello! Happy to be here, looking forward to some great connections!"
]

number_of_posts = range(0,1)
loop = 0
group_cards = driver.find_elements(By.XPATH, '//div[@class="x6s0dn4 x78zum5 x1vqgdyp x1qughib xw7yly9 xvfhwrs"]//a')
group_links = [link.get_attribute('href') for link in group_cards]
for link_url in group_links:
    print(f"Opening group: {link_url}")
    driver.get(link_url)

    time.sleep(3)
    for _ in number_of_posts:

        #link.click()
        #input('Press enter to continue')

        try:
            write_placeholder = driver.find_element(By.XPATH, "//span[contains(text(),'Write something...')]")
            # Click on the element
            ActionChains(driver).move_to_element(write_placeholder).click().perform()
            print("Clicked on 'Write something...' successfully!")
            time.sleep(3)
            try:
                input_box = driver.find_element(By.XPATH, '//div[@aria-label="Write something..." and @role="textbox"]')
                # Send keys to the input box
                input_box.send_keys(messages[loop])
                time.sleep(3)
                try:
                    post_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Post" and @role="button"]'))
                    )
                    post_button.click()
                    print("Post button clicked successfully!")
                except Exception as e:
                    print(f"Failed to click the post button: {e}")

            except Exception as e:
                print(f"Private group input box not found: {e}")
            try:
                post_box = driver.find_element(By.CSS_SELECTOR,
                                               'div[aria-label="Create a public post…"][contenteditable="true"]')
                post_box.send_keys(messages[loop])
                time.sleep(3)
                try:
                    post_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Post" and @role="button"]'))
                    )
                    post_button.click()
                    print("Post button clicked successfully!")
                except Exception as e:
                    print(f"Failed to click the post button: {e}")

            except Exception as e :
                print(f"Public group post box not found: {e}")
            # input_box = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            #     (By.XPATH, '//div[@aria-label="Write something..." and @role="textbox"]')))

            # post_box = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            #     (By.CSS_SELECTOR, 'div[aria-label="Create a public post…"][contenteditable="true"]')))

            loop += 1
            time.sleep(3)
        except Exception as e:
            print(f"Error interacting with group: {e}")
            continue  # Proceed to the next group if an error occurs


input('Press enter to close browser')
driver.quit()


# class Program:
#     def __init__(self):

