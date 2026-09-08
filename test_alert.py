from playwright.sync_api import Page, expect


def test_alert(page: Page):

    # Open practice page
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
   

    # Handle browser alert
    page.on("dialog", lambda dialog: dialog.accept())
    

    # Click the alert button
    page.get_by_role("button", name="Click for JS Alert").click()
    

    # Verify result
    expect(page.locator("#result")).to_have_text(
        "You successfully clicked an alert"
    )
   