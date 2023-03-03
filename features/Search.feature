Feature: Search Functionality

  Background: Asian Paint Navigation
    Given Chrome is opened and user is able to Navigate to Asian Paint Page
    Then Notification is shown user clicks NotNow Button

  Scenario: Search text Box is visible to the User.
    When User enters Asian Paint page it shows search textbox
    Then user enters text on search textbox "paints"

  Scenario: User is able to see Popular Searches in Search Bar
    When  User clicks on Search textbox in Asian Paints Page
    Then It shows Popular Searches
    And User Clicks on "Wallpapers"
    Then It navigates to Wallpapers Page

  Scenario Outline: User enters Valid Search data
    Given User clicks on Search textbox
    When Enters the <ValidData>
    And Clicks on Search icon
    Then It shows Valid search result page

    Examples:
      | ValidData   |
      | Red         |
      | Rooms       |

  Scenario Outline: User enters Invalid Search data
    Given User clicks on Search textbox
    When Enters the <InvalidData>
    And Clicks on Search icon
    Then It shows Invalid search result

    Examples:
      | InvalidData |
      | guyrftyidyt |
      | hgfdfdstys  |

  Scenario: Related search result after entering valid phrase
    Given User clicks on Search textbox
    When User enters valid phrase "Wall"
    Then Result for "Wall" are shown
    And It includes "5 Wall Colours For Home With A Calming Influence"
    Then User navigates to the search page


  Scenario: Related search result after entering Invalid phrase
    Given User clicks on Search textbox
    When User enters invalid phrase "xyz"
    Then It Shows "NO MATCHES FOUND!"
