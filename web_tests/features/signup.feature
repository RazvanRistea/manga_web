Feature: Register new users tests
  Tests for registering new users functionality


  Scenario Outline: Register new user with different countries
    Given There is the following country we want to test with <countryCode>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    Then the user should exist in the backend.

    Examples:
    | countryCode |
    | Japan       |
    | France      |
    | Thailand    |

  Scenario Outline: Register new user with accepting Terms and Conditions and Personal Data Handling
    Given There is the following sign-up agreement combination we want to test with <agreements>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    Then the user should exist in the backend.

    Examples:
    | agreements      |
    | agreeAll offers |
    | agreeAll        |

  Scenario Outline: Register new user without accepting Terms and Conditions and Personal Data Handling
    Given There is the following sign-up agreement combination we want to test with <agreements>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    Then The continue button will be greyed out due to not accepting the correct agreements.

    Examples:
    | agreements           |
    | offers               |

  Scenario: Register new user with missing or invalid information
    Given User is not logged in.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form with invalid data.
    And I fill in the second registration form with invalid data.
    Then the user should exist in the backend.

