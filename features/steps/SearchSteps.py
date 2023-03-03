from behave import *
import time
from hamcrest import *

from features.pages.SearchPageClass import SearchPageClass

@given("Chrome is opened and user is able to Navigate to Asian Paint Page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@then("Notification is shown user clicks NotNow Button")
def step_impl(context):
    context.driver.implicitly_wait(10)
    Notification_Message = SearchPageClass(context.driver)
    Notification_Message.notification()


@when("User enters Asian Paint page it shows search textbox")
def step_impl(context):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.search_textbox()


@then('user enters text on search textbox "{text}"' )
def step_impl(context,text):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.enter_data(text)


@when("User clicks on Search textbox in Asian Paints Page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.click_search_textbox()


@then("It shows Popular Searches")
def step_impl(context):
    context.driver.implicitly_wait(10)
    print("Total no of Searches")
    landingPage = SearchPageClass(context.driver)
    landingPage.popular_search_element()



@step('User Clicks on "Wallpapers"')
def step_impl(context):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.wallpaper_page_()

@then("It navigates to Wallpapers Page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Range of Wall Coverings & Interior Wallpaper for Walls - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@given("User clicks on Search textbox")
def step_impl(context):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.click_search_textbox()

@when(u'Enters the {data}')
def step_impl(context, data):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.enter_data(data)

@step("Clicks on Search icon")
def step_impl(context):
    context.driver.implicitly_wait(10)
    ResultPage = SearchPageClass(context.driver)
    ResultPage.click_search_textbox()


@then("It shows Valid search result page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    Invalid_text = SearchPageClass(context.driver)
    expectedText = "ALL SEARCH RESULTS"
    actualText = Invalid_text.show_all_searches()
    print("The Text is -------->" + actualText)
    assert_that(expectedText, equal_to(actualText))


@then("It shows Invalid search result")
def step_impl(context):
    context.driver.implicitly_wait(10)
    Invalid_text = SearchPageClass(context.driver)
    expectedText ="Sorry, there seem to be no results matching your search."
    actualText = Invalid_text.show_messge()
    print("The Text is -------->" + actualText)
    assert_that(expectedText, equal_to(actualText))


@when('User enters valid phrase "{valid}"')
def step_impl(context, valid):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.enter_data(valid)


@then('Result for "Wall" are shown')
def step_impl(context):
    context.driver.implicitly_wait(10)
    landingPage = SearchPageClass(context.driver)
    landingPage.auto_search_element()


@step('It includes "{auto}"')
def step_impl(context ,auto):
    context.driver.implicitly_wait(10)
    SearchPage = SearchPageClass(context.driver)
    SearchPage.click_auto_search(auto)

@then("User navigates to the search page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedURL = "https://www.asianpaints.com/blogs/5-wall-colours-for-home-with-a-calming-influence.html"
    actualURL = context.driver.current_url
    print("Page title is " + actualURL)
    assert_that(expectedURL, equal_to(actualURL))



@when('User enters invalid phrase "{invalid}"')
def step_impl(context, invalid):
    time.sleep(5)
    landingPage = SearchPageClass(context.driver)
    landingPage.enter_data(invalid)


@then('It Shows "NO MATCHES FOUND!"')
def step_impl(context):
    time.sleep(5)
    Invalid_text = SearchPageClass(context.driver)
    expectedText = "NO MATCHES FOUND!"
    actualText = Invalid_text.invalid_search()
    print("The Text is -------->" +actualText)
    assert_that(expectedText, equal_to(actualText))


