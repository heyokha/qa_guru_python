import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_size():
    browser.config.window_width = 1280
    browser.config.window_height = 960
    yield
    browser.quit()


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('anothername').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу anothername ничего не найдено.'))