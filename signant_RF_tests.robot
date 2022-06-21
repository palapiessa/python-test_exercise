*** Settings ***
Library         SeleniumLibrary

*** Test Cases ***
# Valid Registration
#     [Documentation]     As a UI user I can: 1. Register through web portal
    

Valid Login
    [Documentation]     As a UI user I can: 2. Review my own user information from the main view
    Open Login Page
    Enter User Name
    Enter Password
    Submit Credentials
    Element Text Should Be  id=username   web-user
    Element Text Should Be  id=firstname    Jouko
    Element Text Should Be  id=lastname     Talo
    Element Text Should Be  id=phone    04012345

*** Keywords ***
Open Login Page
    Open Browser    http://10.80.126.57:8080/login
    Title Should Be    Log In - Demo App

Enter User Name
    Input Text    id=username      web-user

Enter Password
    Input Text    id=password  rasti

Submit Credentials
    Click Button    Log In
    Title Should Be    User Information - Demo App
