import selenium
Path = "/usr/local/bin/chromedriver"
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()
# browser.get('http://youtube.com/')

# Goto covid check google form
driver = webdriver.Chrome(Path)
driver.get('http://go.lbl.gov/s')

#locate employee ID field and enter to field

search = driver.find_element_by_class_name('quantumWizTextinputPaperinputInput')
search.send_keys("065128")
search.send_keys(Keys.RETURN)

#Locate CheckBox and
#checkbox = driver.find_element_by_name("i12")
checkbox = driver.find_element_by_class_name('quantumWizTogglePapercheckboxInnerBox')
checkbox.click()


# Click on submit

submit = driver.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')

submit.click()
#appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel
#print (driver.title)

#driver.close()


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
