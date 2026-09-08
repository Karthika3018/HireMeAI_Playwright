from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://hiremeai.website/login")

    page.get_by_placeholder("you@email.com").fill("keerthiananth006@gmail.com")
    page.locator('input[name="password"]').fill("Immigration@30")

    page.get_by_role("button", name="Log in →").click()

    expect(page.get_by_role("button", name="Log out")).to_be_visible()

    page.get_by_role("button", name="Log out").click()

    expect(page).to_have_url("https://hiremeai.website/login")