from behave import *
import time
from hamcrest import *
from features.pages.SearchPageClass import SearchPageClass
from datafiles import ExcelUtils
from features.utility.ConfigClass import ConfigClass

@when("User enters {Valid} data using excel")
def step_impl(context ,Valid):
    ExcelUtils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    Valid = ExcelUtils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 1)
    SearchPage = SearchPageClass(context.driver)
    SearchPage.enter_data(Valid)
    context.driver.implicitly_wait(10)

@then("It shows Valid search result page 1")
def step_impl(context):
    expectedURL = "https://www.asianpaints.com/search-results.html?q=colors"
    pageURL = context.driver.current_url

    try:
        if (expectedURL == pageURL):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Failed")
            assert False
        context.driver.implicitly_wait(10)
    finally:
        print("Page title is " + pageURL)
        context.driver.implicitly_wait(10)
@when("User enters {Valid} data 2 using excel")
def step_impl(context, Valid):
    ExcelUtils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    Valid = ExcelUtils.read_data(ConfigClass.datafilepath, "Sheet1", 3, 1)
    SearchPage = SearchPageClass(context.driver)
    SearchPage.enter_data(Valid)
    context.driver.implicitly_wait(10)


@then("It shows Valid search result page 2")
def step_impl(context):
    expectedURL = "https://www.asianpaints.com/search-results.html?q=asian"
    pageURL = context.driver.current_url
    try:
        if (expectedURL == pageURL):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 3, 2, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 3, 2, "Failed")
            assert False
        context.driver.implicitly_wait(10)
    finally:
        print("Page title is " + pageURL)
        context.driver.implicitly_wait(10)
