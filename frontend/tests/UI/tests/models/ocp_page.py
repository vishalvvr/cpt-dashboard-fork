from playwright.sync_api import Page
from models.base_page import BasePage
import requests

class OcpPage(BasePage):
    
    def __init__(self, page: Page) -> None:
        self.page = page