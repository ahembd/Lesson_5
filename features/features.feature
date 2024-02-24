# Created by alberthembd at 2/23/24
Feature: Target login

  Scenario: Target login
    Given the user has a valid user name and password and the user has navigated to the Target web page
    When he clicks the Sign in button and then clicks username
    Then the process will log him in.