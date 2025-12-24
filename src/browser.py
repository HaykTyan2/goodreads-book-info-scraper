from playwright.sync_api import sync_playwright

_playwright = None
_browser = None
_context = None

def start_browser(headless=False, user_agent=None):
    global _playwright, _browser, _context
    _playwright = sync_playwright().start()
    _browser = _playwright.chromium.launch(headless=headless)
    _context = _browser.new_context(
        user_agent=user_agent or 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    return _browser

def stop_browser():
    global _playwright, _browser, _context
    if _context:
        _context.close()
    if _browser:
        _browser.close()
    if _playwright:
        _playwright.stop()

def get_page(url, wait_until="domcontentloaded"):
    page = _context.new_page()
    page.goto(url, wait_until=wait_until)
    return page
