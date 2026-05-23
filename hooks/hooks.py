import os
import platform
from py.xml import html
import pytest



def pytest_configure(config):

    config.metadata["Project"] = "Playwright Automation"

    config.metadata["Tester"] = "Priya"

    config.metadata["Browser"] = "Chromium (Playwright)"

    config.metadata["OS"] = (
        platform.system() + " " + platform.release()
    )


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):

    report.title = "ZenClass Automation Test Report"


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(
        prefix,
        summary,
        postfix
):

    prefix.extend([
        html.p("Automation executed by Priya")
    ])


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):

    cells.insert(1, html.th("Status"))


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):

    if report.passed:

        cells.insert(1, html.td("PASS"))

    elif report.failed:

        cells.insert(1, html.td("FAIL"))

    else:

        cells.insert(1, html.td("WARNING"))


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_html(report, data):

    if report.failed:

        test_name = report.nodeid.split("::")[-1]

        screenshot_path = (
            f"screenshots/{test_name}.png"
        )

        if os.path.exists(screenshot_path):

            data.append(
                html.a(
                    "Screenshot",
                    href=screenshot_path
                )
            )