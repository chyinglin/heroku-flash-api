*** Settings ***
Documentation     Example using the space separated format.
Library           OperatingSystem

*** Variables ***
${MESSAGE}        MESSAGE

*** Test Cases ***
Test
    [Documentation]    Example test.
    Log    ${MESSAGE}
    Log    ${OUTPUT DIR}
    Log    ${LOG FILE}
