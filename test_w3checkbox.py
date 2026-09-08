from playwright.sync_api import Page


def test_checkbox_radio(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator('input[type="checkbox"]').first

    checkbox.check()

    assert checkbox.is_checked()