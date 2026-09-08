from playwright.sync_api import Page, expect


def test_confirm_accept(page: Page):

    # Open JavaScript alerts page
    page.goto("https://the-internet.herokuapp.com/javascript_alerts") 
   
    # Handle confirm dialog and click OK
    page.on("dialog", lambda dialog: dialog.accept()) 
    

    # Click the confirm button
    page.get_by_role("button", name="Click for JS Confirm").click()
 

    # Verify OK was selected
    expect(page.locator("#result")).to_have_text(
        "You clicked: Ok"
    )
   