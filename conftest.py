import pytest
import os

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": os.getenv("CI", "false") == "true",
        "args": [
            "--window-position=260,-990",
            "--window-size=1400,900"
            # "--start-maximized"
        ]
    }