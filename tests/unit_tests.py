"""Create functional tests for project using unittest module

This module depends on the file test/test_config.py to define the following
module-level constants, which are used in live Qualtrics API v3 calls to create
test mailing lists and survey distributions:

- API_TOKEN, a Qualtrics API v3 token; see https://www.qualtrics.com/support/
    integrations/api-integration/overview/#GeneratingAnAPIToken
- DATA_CENTER, a Qualtrics account data center specific to the account
    associated with the API token; see https://api.qualtrics.com/docs/root-url
- LIBRARY_ID, a Qualtrics Library/Group id specific to the account associated
    with the API token; see https://api.qualtrics.com/docs/finding-qualtrics-ids
- MAILING_LIST_NAME, the name for the test mailing list being created
- CATEGORY_NAME_FOR_UNIT_TESTS, the category name for the test mailing list
    being created
- MESSAGE_ID, a Qualtrics message id specific to the account associated with
    the API token; see https://api.qualtrics.com/docs/finding-qualtrics-ids
- SURVEY_ID, a Qualtrics survey id specific to the account associated with
    the API token; see https://api.qualtrics.com/docs/finding-qualtrics-ids
- SEND_DATE, the send datetime for the test survey distribution being created in
    ISO 8601 format; see https://api.qualtrics.com/docs/dates-and-times
- FROM_NAME, the from name for the test survey distribution being created
- REPLY_EMAIL, the reply-to email address for the test survey distribution being
    created
- SUBJECT, the email subject for the test survey distribution being created

"""

from io import StringIO
from unittest import TestCase

import requests

from tests import test_config
from qualtrics_account import QualtricsAccount
from qualtrics_mailing_list import QualtricsMailingList
from qualtrics_distribution import QualtricsDistribution


class QualtricsAccountTests(TestCase):
    def test_set_api_token_from_file(self):
        # set a pointer to a file so that exactly one line will be read to get
        # an API token
        test_token = "This is a test token! :)"
        test_fp = StringIO(test_token)

        # initialize a QualtricsAccount object
        test_account = QualtricsAccount()
        test_account.set_api_token_from_file(test_fp)
        self.assertEqual(test_token, test_account.api_token)


class QualtricsMailingListTests(TestCase):
    def test_mailing_list_init(self):
        # initialize a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initialize a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            category_name=test_category_name,
        )
        test_mailing_list_id = test_mailing_list.id

        # verify mailing list with created id exists
        request_response = requests.request(
            "GET",
            f"https://{test_account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{test_mailing_list_id}",
            headers={
                "x-api-token": test_account.api_token
            },
        )

        # verify mailing list exists with specified id by checking HTTP response
        self.assertEqual(request_response.status_code, 200)

    def test_import_contact_list_from_csv_file(self):
        # initialize a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initialize a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            category_name=test_category_name,
        )

        # import test contact file
        test_contact_list = [
            "firstName,lastName,email",
            "first,user1,first@user.test.please.ignore",
            "second,user2,second@user2.test.please.ignore",
        ]
        test_fp = StringIO("\n".join(test_contact_list))
        test_mailing_list.import_contact_list_from_csv_file(test_fp)

        # verify contact list has been imported
        request_response = requests.request(
            "GET",
            f"https://{test_account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{test_mailing_list.id}/contacts",
            headers={
                "x-api-token": test_account.api_token,
            },
        )

        # verify mailing list has specified length by checking HTTP response
        contact_list_results = request_response.json()["result"]["elements"]
        self.assertEqual(len(contact_list_results), len(test_contact_list) - 1)

    def test_contact_list_property(self):
        # initialize a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initialize a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            category_name=test_category_name,
        )

        # import test contact file
        test_contact_list = [
            "firstName,lastName,email",
            "first,user1,first@user.test.please.ignore",
            "second,user2,second@user2.test.please.ignore",
        ]
        test_fp = StringIO("\n".join(test_contact_list))
        test_mailing_list.import_contact_list_from_csv_file(test_fp)

        # verify contact list of specified list exists and is accessible using
        # the contact_list property
        self.assertEqual(len(test_mailing_list.contact_list),
                         len(test_contact_list) - 1)


class QualtricsDistributionTest(TestCase):
    def test_distribution_init(self):
        # initialize a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initialize a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            category_name=test_category_name,
        )

        # initialize a QualtricsDistribution object
        test_message_id = test_config.MESSAGE_ID
        test_survey_id = test_config.SURVEY_ID
        test_send_date = test_config.SEND_DATE
        test_from_name = test_config.FROM_NAME
        test_reply_email = test_config.REPLY_EMAIL
        test_subject = test_config.SUBJECT
        test_distribution = QualtricsDistribution(
            test_mailing_list,
            test_message_id,
            test_survey_id,
            test_send_date,
            test_from_name,
            test_reply_email,
            test_subject,
        )
        test_distribution_id = test_distribution.id
        print(test_distribution.id)

        # verify distribution exists
        request_response = requests.request(
            "GET",
            f"https://{test_account.data_center}.qualtrics.com/API/v3/"
            f"distributions/{test_distribution_id}?surveyId={test_survey_id}",
            headers={
                "x-api-token": test_account.api_token
            },
        )

        # verify distribution exists with specified id by checking HTTP response
        self.assertEqual(request_response.status_code, 200)

    def test_distribution_details_property(self):
        # initialize a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initialize a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            category_name=test_category_name,
        )

        # initialize a QualtricsDistribution object
        test_message_id = test_config.MESSAGE_ID
        test_survey_id = test_config.SURVEY_ID
        test_send_date = test_config.SEND_DATE
        test_from_name = test_config.FROM_NAME
        test_reply_email = test_config.REPLY_EMAIL
        test_subject = test_config.SUBJECT
        test_distribution = QualtricsDistribution(
            test_mailing_list,
            test_message_id,
            test_survey_id,
            test_send_date,
            test_from_name,
            test_reply_email,
            test_subject,
        )

        # verify distribution list was successfully created and had properly
        # formatted id accessible from details property
        self.assertRegex(test_distribution.details["result"]["id"], 'EMD_\w+')
