from playwright.sync_api import Page, expect

def test_wikipedia_search(page: Page):
    page.goto("https://www.wikipedia.org/")

    page.locator("#searchInput").fill("Playwright")

    page.locator("#searchInput").press("Enter")
    #page.get_by_role("button", name="Search").click()

    expect(page).to_have_url(
        "https://en.wikipedia.org/wiki/Playwright"
    )