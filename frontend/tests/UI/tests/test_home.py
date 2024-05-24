import os
import pytest
from playwright.sync_api import sync_playwright, expect, Page
import requests
from models.home_page import HomePage

  
@pytest.fixture
def tconfig():
    """
    This is configuration fixture which gets enviroment variables and passes to test
    """
    return {
        "base_url": os.environ['BASE_URL'],
        "api_url": os.environ['API_URL']
    }

def test_homepage(tconfig, page: Page):
    '''
    Test if homepage is visible
    '''
    home_page = HomePage(page)
    home_page.api_url = tconfig['api_url']
    home_page.base_route = tconfig['base_url']
    home_page.navigate(tconfig['base_url'])    
    expect(home_page.get_element_by_text("CPT Dashboard")).to_be_visible()

def test_pagination_count(tconfig, page: Page):
    '''
    Test if pagination count displayed is equal to what api is returning 
    '''
    home_page = HomePage(page)
    home_page.api_url = tconfig['api_url']
    home_page.base_route = tconfig['base_url']
    data = home_page.get_pagination_and_page_counts()        
    # assert total no of jobs
    assert data["api_no_of_jobs"] == data["page_no_of_jobs"]
    # assert total no of pages    
    assert data["page_no_of_pages"] == data["calculated_no_of_pages"]

def test_pagination_navigation(tconfig, page: Page):
    '''
    Test if pagination count displayed is equal to what api is returning
    '''
    home_page = HomePage(page)
    home_page.api_url = tconfig['api_url']
    home_page.base_route = tconfig['base_url']
    pass