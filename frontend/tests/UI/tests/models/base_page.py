from playwright.sync_api import Page
from typing import Dict, List
import requests

class BasePage:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_route = None
        self.api_url = None
        self.xpath_table_tbody = None
        self.xpath_page_no_of_jobs = None
        self.xpath_page_no_of_pages = None

    def navigate(self, route:str="/") -> None:
        self.page.goto(route)
    
    def get_element_by_text(self, text:str="CPT Dashboard") -> Page.locator:
        return self.page.get_by_text(text)
    
    def wait_until_table_is_visible(self, var_xpath:str) -> None:
        self.page.wait_for_selector(var_xpath)

    def calculate_no_of_pages(self, total_no_of_jobs:int, records_per_page:int=25) -> int:
        """
        calculate total no of page using total no of jobs  
        """
        tmp_page_no = total_no_of_jobs/records_per_page
        if not tmp_page_no.is_integer():
            calculated_no_of_pages = str(tmp_page_no).split(".")[0]    
            calculated_no_of_pages = int(calculated_no_of_pages)+1
        else:
            calculated_no_of_pages = tmp_page_no
        
        return calculated_no_of_pages
    
    def get_pagination_and_page_counts(self) -> Dict:
        """
        return 
            - jobs count from api & page
            - calculated no of pages & pages count from page 
        """
        self.navigate(route=self.base_route)
        self.wait_until_table_is_visible(self.xpath_table_tbody)
        api_data = self.get_all_jobs(self.api_url)
        
        # no of jobs from Pagination section
        page_no_of_jobs = int(self.page.wait_for_selector(
            self.xpath_page_no_of_jobs
            ).text_content())
        
        # no of pages from Pagination section
        page_no_of_pages = self.page.wait_for_selector(
            self.xpath_page_no_of_pages
            ).text_content()
        
        # remove some extra string and get text
        page_no_of_pages = int(page_no_of_pages.split()[1])
        
        return {
            "api_no_of_jobs": len(api_data['results']),
            "page_no_of_jobs": page_no_of_jobs,
            "page_no_of_pages": page_no_of_pages,
            "calculated_no_of_pages": self.calculate_no_of_pages(page_no_of_jobs, 25)
        }

    def get_all_jobs(self, api_url:str) -> Dict:
        '''
        This function will return all jobs details
        res : {
            startDate: "2024-05-11"
            endDate: "2024-05-16"
            results:[
                {}...{}
            ]
        }
        '''
        return requests.get(api_url).json()
    
    def search(self, text:str):
        pass