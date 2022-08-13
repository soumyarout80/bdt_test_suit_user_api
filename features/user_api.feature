@UserAPI
Feature: Create a user using  RESTful API
    As a user
    I want to use user API for user CRUD operations
    So that I can create, retrieve, update, and delete users using HTTP requests.

    Background:
        Given user API endpoint
        And a customer's first name
        And a customer's last name
        And a customer's gender

    @CreateUserPositive
    Scenario Outline: 001 Create a user with a valid email and password
        When I enter user email id <email>
            And I enter the user phone number <phone>
            And I enter password <password> for the user
            And I send a POST request to the user API
        Then I should not see the error message
            And I should get a status code of "<status>"
            And I should be able to request GET for the newly created user
            And the response value of "email" should equal <email>
        Examples:
            |email                      |phone      |password    |status |
            | "soumya.rout@gmail.com"   |1234567899 |"abc12345"  | 200   |

    @CreateUserNegative01
    Scenario Outline: 002 Create a user with an invalid email and password
        When I enter user email id <email>
            And I enter the user phone number <phone>
            And I enter password <password> for the user
            And I send a POST request to the user API
            And I should get a status code of "<status>"
        Examples:
           |email                  |phone      |password   |status |
           |"soumya.rout$gmail.com"|1234567899 |"abc12345" | 406   |
