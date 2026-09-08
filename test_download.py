from playwright.sync_api import Page


def test_file_download(page: Page):

    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        page.locator("a").first.click()

    download = download_info.value

    print(download.suggested_filename())

    assert download.suggested_filename() != ""