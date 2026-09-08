from playwright.sync_api import Page, expect


def test_new_tab(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")
   

    # Wait for a new tab to open
    with page.expect_popup() as popup_info:

        # Click the link that opens a new tab
        page.get_by_text("Click Here").click()
  

    # Get the new tab
    new_page = popup_info.value
  

    # Verify the new tab URL
    expect(new_page).to_have_url(
        "https://the-internet.herokuapp.com/windows/new"
    )


    # Verify text in the new tab
    expect(new_page.locator("h3")).to_have_text("New Window")
  