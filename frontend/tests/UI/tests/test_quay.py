from playwright.sync_api import sync_playwright, expect, Page
from models.quay_page import QuayPage
import os
import pytest

@pytest.fixture
def tconfig():
    """
    This is configuration fixture which gets enviroment variables and passes to test
    """
    return {
        "base_url": os.environ['BASE_URL'],
        "api_url": os.path.join(os.environ['API_URL'],"ocp")
    }

def test_quay_page(tconfig, page: Page):
    quay_page = QuayPage(page)
    quay_page.api_url = tconfig['api_url']
    quay_page.base_route = tconfig['base_url']
    quay_page.navigate(tconfig['base_url']) 
    expect(quay_page.get_element_by_text("CPT Dashboard")).to_be_visible()
