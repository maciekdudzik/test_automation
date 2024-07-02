*** Settings ***
Resource    resources.robot

*** Variables ***
${ARTICLE_ID}    1234
${ARTICLE_TITLE}    Test Article

*** Test Cases ***
Check Article List Unchanged
    GET ${BASE_URL}/articles
    ${first_list}=    Set Variable    ${response.json()}
    Sleep    2s
    GET ${BASE_URL}/articles
    ${second_list}=    Set Variable    ${response.json()}
    Length Should Be Equal    ${first_list}    ${second_list}

Check Adding And Removing Article
    GET ${BASE_URL}/articles
    Article Should Not Be Present    ${response.json()}    ${ARTICLE_TITLE}
    POST ${BASE_URL}/articles    json=${json}
    Should Be Equal As Strings    ${response.status_code}    201
    GET ${BASE_URL}/articles
    Article Should Be Present    ${response.json()}    ${ARTICLE_TITLE}
    DELETE ${BASE_URL}/articles/${ARTICLE_ID}
    Should Be Equal As Strings    ${response.status_code}    204
    GET ${BASE_URL}/articles
    Article Should Not Be Present    ${response.json()}    ${ARTICLE_TITLE}

Check Removing Nonexistent Article
    DELETE ${BASE_URL}/articles/nonexistent
    Should Be Equal As Strings    ${response.status_code}    404

Check Adding Article Without Title
    POST ${BASE_URL}/articles    json={"id": "5678", "title": ""}
    Should Be Equal As Strings    ${response.status_code}    400
    Dictionary Should Contain Value    ${response.json()}    "Title cannot be empty"

*** Keywords ***
Article Should Be Present
    [Arguments]    ${articles}    ${title}
    ${titles}=    Evaluate    [article['title'] for article in ${articles}]
    Should Contain    ${titles}    ${title}

Article Should Not Be Present
    [Arguments]    ${articles}    ${title}
    ${titles}=    Evaluate    [article['title'] for article in ${articles}]
    Should Not Contain    ${titles}    ${title}
