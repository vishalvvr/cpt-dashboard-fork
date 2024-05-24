from playwright.sync_api import sync_playwright, expect, Page
from models.ocp_page import OcpPage
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
    
def test_ocp_page(tconfig, page: Page):
    """
    test homepage is visible 
    """
    ocp_page = OcpPage(page)
    ocp_page.api_url = tconfig['api_url']
    ocp_page.base_route = tconfig['base_url']
    ocp_page.navigate(tconfig['base_url'])
    expect(ocp_page.get_element_by_text("CPT Dashboard")).to_be_visible()
