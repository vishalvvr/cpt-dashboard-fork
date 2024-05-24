from playwright.sync_api import Page
from models.base_page import BasePage
import requests

class QuayPage(BasePage):

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_route = "/quay"
    