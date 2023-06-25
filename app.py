import asyncio
from playwright.async_api import *

id = 'your ID'
pw = 'your PW'

async def post(page: Page):
    user_input = input("트위터에 남기고 싶은 글을 써주세요: ")
    await page.fill('.public-DraftStyleDefault-ltr', user_input)
    await page.get_by_test_id("tweetButtonInline").click()


async def open_and_login(page: Page):
    await page.goto("http://twitter.com")
    await page.get_by_test_id("login").click()
    await page.locator('text=휴대폰 번호, 이메일 주소 또는 사용자 아이디').fill(id)
    await page.locator('text=다음').click()
    await page.get_by_text("비밀번호", exact=True).fill(pw)
    await page.locator('text=로그인하기').click()


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await open_and_login(page)
        await post(page)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
