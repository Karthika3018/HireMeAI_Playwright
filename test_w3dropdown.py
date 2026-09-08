from playwright.sync_api import Page, expect


def test_dropdown(page: Page):

    # Open practice page
    page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

    # Access the iframe
    frame = page.frame_locator("#iframeResult")

    # Select an option from dropdown
    frame.locator("select").select_option("saab")

    # Verify selected option
    expect(frame.locator("select")).to_have_value("saab")