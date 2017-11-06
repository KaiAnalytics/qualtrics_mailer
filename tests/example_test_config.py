"""Exports attributes for running module functional and unit tests

To use this file,
(1) fill in all items in square brackets below, using values corresponding to
    your Qualtrics account
(2) rename to test_config.py

Instructions for generating an API Token can be found at
https://www.qualtrics.com/support/integrations/api-integration/overview/

Instructions for finding Qualtrics objects ids can be found at
https://api.qualtrics.com/docs/finding-qualtrics-ids

Attributes:
    API_TOKEN (str): a Qualtrics API v3 token; see https://www.qualtrics.com/
        support/integrations/api-integration/overview/#GeneratingAnAPIToken
    DATA_CENTER (str): a Qualtrics account data center specific to the account;
        see https://api.qualtrics.com/docs/root-url
    LIBRARY_ID (str): a Qualtrics Library/Group id specific to the account; see
        https://api.qualtrics.com/docs/finding-qualtrics-ids
    MAILING_LIST_NAME (str): the name for the test mailing list being created
    CATEGORY_NAME_FOR_FUNCTIONAL_TESTS (str): the category name for the test
        mailing list being created
    MESSAGE_ID (str): a Qualtrics message id specific to the account; see
        https://api.qualtrics.com/docs/finding-qualtrics-ids
    SURVEY_ID (str): a Qualtrics survey id specific to the account; see
        https://api.qualtrics.com/docs/finding-qualtrics-ids
    SEND_DATE (str): the send datetime for the test survey distribution being
        created in ISO 8601 format; see https://api.qualtrics.com/docs/
        dates-and-times
    FROM_NAME (str): the from name for the test survey distribution being
        created
    REPLY_EMAIL (str): the reply-to email address for the test survey
        distribution being created
    SUBJECT (str): the email subject for the test survey distribution being
        created

"""

from datetime import datetime


API_TOKEN = '[your account API token]'
DATA_CENTER = '[your account data center name]'


LIBRARY_ID = '[valid library id for your account]'
MAILING_LIST_NAME = datetime.now().strftime('%Y%m%d-%H%M%S')
CATEGORY_NAME_FOR_UNIT_TESTS = "Unit Testing Folder"
CATEGORY_NAME_FOR_FUNCTIONAL_TESTS = "Functional Testing Folder"

MESSAGE_ID = '[valid message id for your account]'
SURVEY_ID = '[valid survey id for your account]'
SEND_DATE = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
FROM_NAME = 'Test From Name'
REPLY_EMAIL = 'Test.Email@Email.com'
SUBJECT = 'Test Survey'
