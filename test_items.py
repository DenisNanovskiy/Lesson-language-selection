# import time


def test_contains_an_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    flag = False
    try:
        button_submit = browser.find_element_by_css_selector('button.btn-add-to-basket')
        flag = True
    except:
        assert flag is True, "No Such Element"
    # time.sleep(30)
