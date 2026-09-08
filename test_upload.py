from playwright.sync_api import Page, expect


def test_file_upload(page: Page):

    # Open upload practice page
    page.goto("https://the-internet.herokuapp.com/upload")

    # Upload a file
    page.locator("#file-upload").set_input_files("test.txt")

    # Click Upload
    page.locator("#file-submit").click()

    # Verify uploaded file name
    expect(page.locator("#uploaded-files")).to_have_text("test.txt")
  