
Feature: Search Using DDF
  Background: Asian Paint Navigation
    Given Chrome is opened and user is able to Navigate to Asian Paint Page
    Then Notification is shown user clicks NotNow Button

  Scenario:User enters Valid Search data
    Given User clicks on Search textbox
    When  User enters <Valid> data using excel
    And Clicks on Search icon
    Then It shows Valid search result page 1

  Scenario:User enters Valid Search data
    Given User clicks on Search textbox
    When  User enters <Valid> data 2 using excel
    And Clicks on Search icon
    Then It shows Valid search result page 2