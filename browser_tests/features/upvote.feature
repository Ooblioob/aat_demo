Feature: Test thecatapi upvote system
  As a cat enthusiast
  I want to be able to upvote a picture I like
  So that the website will continue to show cute cats

Scenario: Test display new picture functionality
  Given I am on thecatapi's homepage
  When I click "love it"
  Then a new cat image should be loaded into the page

