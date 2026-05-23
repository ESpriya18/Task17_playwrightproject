from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)

    def get_context(self):
        return self.browser.new_context()
        return context.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()
