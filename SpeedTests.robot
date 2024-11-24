*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
RegTest
    ${speed}=   get selenium speed
    log to console  ${speed}
    open browser    http://demowebshop.tricentis.com/register   chrome
    maximize browser window
    #sleep 3
    set selenium speed  3 seconds

    select radio button     Gender      M

    input text  name:FirstName  Vijay
    input text  name:LastName   Khalate
    input text  name:Email  vijaykhalate05@gmail.com
    input text  name:Password   davidjohn
    input text  name:ConfirmPassword    davidjohn

    ${speed}=   get selenium speed
    log to console  ${speed}