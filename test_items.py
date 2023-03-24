import time
from selenium.webdriver.common.by import By

'''
Комментарий для проверяющего:
    1) Код написан для PyCharm строки обращения к driver возможно нужно будет заменить, 
    как и к user_language
    2) Выбор языка по умолчанию: None
'''

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_check_basket(browser):
    browser.get(link)
    time.sleep(30)
    input1 = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    text_basket = input1.text
    print(f"'Это текст на кнопке:' {text_basket}")
    assert "Añadir al carrito" == text_basket, 'Внимание, текст на кнопке на es'

