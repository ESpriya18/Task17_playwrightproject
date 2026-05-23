import pytest
from drivers.browser_manager import BrowserManager


@pytest.fixture(scope="function")
def setup_browser(request):

    bm = BrowserManager()

    context = bm.get_context()

    page = context.new_page()

    yield page


    if request.node.rep_call.failed:
        page.screenshot(
            path=f"screenshots/{request.node.name}.png"
        )

    bm.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)