Feature: Feature name

Scenario: Succes login with correct credentials
    Given I am on the homepage
    When I cick sign in
    And I fill my credentials
    Then I can't login with wrong credentials