*** Settings ***
Library         SeleniumLibrary

*** Test Cases ***
Valid Registration
    [Documentation]     As a UI user I can: 1. Register through web portal
    Open Index Page
    Open Register Page
    Register User    username=PetriK    password=0000    firstname=Petri    lastname=Kukka    phone=0000    

Valid User Info
    [Documentation]     As a UI user I can: 2. Review my own user information from the main view
    Open Index Page
    Open Login Page
    Enter Credentials    username=PetriK    password=0000   
    Element Text Should Be  id=username   PetriK
    Element Text Should Be  id=firstname    Petri
    Element Text Should Be  id=lastname     Kukka
    Element Text Should Be  id=phone    0000

*** Keywords ***
Open Login Page
    Click Link      Log In
    Title Should Be    Log In - Demo App

Open Index Page
    Open Browser    http://10.80.126.57:8080/
    Title Should Be    index page - Demo App

Open Register Page
    Click Link      Register
    Title Should Be    Register - Demo App

Register User
    [Arguments]    ${username}    ${password}    ${firstname}    ${lastname}    ${phone}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Input Text    id=firstname    ${firstname}
    Input Text    id=lastname    ${lastname}
    Input Text    id=phone    ${phone}
    Click Button    Register
    # Log In page is opened
    Title Should Be    Log In - Demo App
    
Enter Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    Log In
    Title Should Be    User Information - Demo App
