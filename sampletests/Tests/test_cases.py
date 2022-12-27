# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sampletests.utilities.baseclass import BaseClass
from sampletests.PageObjects.source import SRC
from sampletests.PageObjects.destination import Dest
from sampletests.PageObjects.journeydate import Jrndate
from sampletests.PageObjects.search import Search


class TestBusticketBooking(BaseClass):

    def test_source_select(self):
        log = self.getLogger()
        origin = SRC(self.d)
        origin.sourcesel().send_keys('pul')
        l = origin.searchsource()
        for city in l:
            if city.text == 'Pulivendula':
                city.send_keys(Keys.ENTER)
        log.info('Sorce city Selected')

    def test_destination_select(self):
        log = self.getLogger()
        endlocation = Dest(self.d)
        endlocation.destsel().send_keys('hyd')
        l1 = endlocation.searchend()
        for end in l1:
            if end.text == 'Hyderabad':
                end.send_keys(Keys.ENTER)
        log.info('Destination city Selected')

    def test_journey_date(self):
        journey_date = Jrndate(self.d)
        journey_date.godate().click()
        journey_date.seldate().click()

    def test_submit_search(self):
        searchbtn = Search(self.d)
        searchbtn.searchbtn().click()
