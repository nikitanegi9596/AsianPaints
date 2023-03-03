from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

class SearchPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element locators
        self.Search = "q"

        self.SearchClick = "//*[@class='textInputWrap search-widget']"

        self.Popularelements = "//div[@class='header-auto-suggest__default--list track_autosuggestion']/ul/li/a"

        self.Autosearch ="//div[@class='header-auto-suggest__results--search-list track_search_autosuggestion']/ul/li/a"

        self.Result = "header-auto-suggest__no-results"

        self.Message = "div[class='no-results-content__text-block text']>h2"

        self.SearchResult = "div[class ='result-content__header-wrap']>h2"

        self.Searchicon ="//button[@class='js-header-search-handle']"

        self.Frame = "(//iframe)[7]"

        self.button = "//*[@value='Not Now']"


    def search_textbox(self):
        SearchTextBox = self.driver.find_element(By.NAME, self.Search)
        SearchTextBox.is_displayed()

    def enter_data(self ,en):
        EnterText = self.driver.find_element(By.NAME, self.Search)
        EnterText.send_keys(en)

    def click_search_textbox(self):
        ClickSearch = self.driver.find_element(By.NAME, self.Search)
        ClickSearch.send_keys(Keys.ENTER)

    def popular_search_element(self):
        elements = self.driver.find_elements(By.XPATH,self.Popularelements)
        print(len(elements))
        for i in elements:
            print(i.text)

    def wallpaper_page_(self):
        elements = self.driver.find_elements(By.XPATH,self.Popularelements)
        for i in elements:
            if i.text == 'Wallpapers':
                i.send_keys(Keys.ENTER)
                break


    def auto_search_element(self):
        elements = self.driver.find_elements(By.XPATH, self.Autosearch)
        print(len(elements))
        for i in elements:
            print(i.text)


    def click_auto_search(self, ref):
        elements = self.driver.find_elements(By.XPATH, self.Autosearch)
        for i in elements:
            if (i.text == ref):
                i.send_keys(Keys.ENTER)
                break

    def click_search_icon(self):
        SearchIcon= self.driver.find_elements(By.XPATH,self.Searchicon)
        SearchIcon.send_keys(Keys.ENTER)

    def show_all_searches(self):
        Text = self.driver.find_element(By.CSS_SELECTOR, self.SearchResult).text
        return Text

    def show_messge(self):
        searchText = self.driver.find_element(By.CSS_SELECTOR, self.Message).text
        return searchText

    def invalid_search(self):
        Match = self.driver.find_element(By.CLASS_NAME, self.Result).text
        return Match

    def notification(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("(//iframe)[7]"))
        AllowButton = self.driver.find_element(By.XPATH, self.button)
        AllowButton.send_keys(Keys.ENTER)


