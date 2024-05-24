from playwright.sync_api import Page
from models.base_page import BasePage
import requests

class HomePage(BasePage):
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_route = "/home"
        self.api_url = "http://localhost:8000/api/v1/cpt/jobs?pretty=true"
        self.xpath_table_tbody = '//div[@class="main-page-container "]/child::table/child::tbody'
        self.xpath_page_no_of_jobs = '//button[@id="pagination-bottom-toggle"]/child::span/child::b[2]'
        self.xpath_page_no_of_pages = '//div[@id="pagination-bottom-pagination"]/child::nav//following::span[2]'
    