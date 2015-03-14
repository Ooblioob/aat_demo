Feature: Test thecatapi homepage
  As a cat enthusiast
  I want to see a home page with a random cat picture
  So that I can enjoy it, share it or up/down vote it

Scenario: Test the title
  Given I am on thecatapi's homepage
  When I click the "love it" button
  Then a new cat image should be loaded into the page
