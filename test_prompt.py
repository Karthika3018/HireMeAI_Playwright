from playwright.sync_api import Page, expect


def test_prompt(page: Page):

    # Open JavaScript alerts page
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # Handle prompt dialog and enter text
    page.on("dialog", lambda dialog: dialog.accept("Karthika"))

    # Click the prompt button
    page.get_by_role("button", name="Click for JS Prompt").click()

    # Verify entered text
    expect(page.locator("#result")).to_have_text(
        "You entered: Karthika"
    )