from playwright.sync_api import Page, expect


def test_checkbox_radio(page: Page):

    # Open practice page
    page.goto("https://www.w3schools.com/html/html_forms.asp")

    # Find checkbox
    checkbox = page.locator('input[type="checkbox"]').first

    # Check the checkbox
    checkbox.check()

    # Verify checkbox is checked
    expect(checkbox).to_be_checked()