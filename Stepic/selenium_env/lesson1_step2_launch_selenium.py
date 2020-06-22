import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидет открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливет паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска
# элементов обсудим позже
# ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# текст ответа в найденном поле
textarea.send_keys("get()")
time.sleep(5)

# найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# команда закрытия окна браузера
driver.quit()







