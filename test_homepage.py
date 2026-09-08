from playwright.sync_api import Page, expect

def test_login_navigation(page: Page):
    page.goto("https://hiremeai.website/")

    page.get_by_role("link", name="Login").click()

    expect(page).to_have_url("https://hiremeai.website/login")