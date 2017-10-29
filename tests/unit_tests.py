from io import StringIO
from unittest import TestCase

import requests

from tests import test_config
from qualtrics_account import QualtricsAccount
from qualtrics_mailing_list import QualtricsMailingList


class APITokenManagementTests(TestCase):

    def test_set_api_token_from_file(self):
        # set a pointer to a file so that exactly one line will be read to get
        # an API token
        test_token = "This is a test token! :)"
        test_fp = StringIO(test_token)

        # initiate a QualtricsAccount object
        test_account = QualtricsAccount()
        test_account.set_api_token_from_file(test_fp)
        self.assertEqual(test_token,test_account.api_token)


class CreateMailingListObject(TestCase):

    def test_mailing_list_init(self):
        # initiate a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initiate a QualtricsMailingList object
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_UNIT_TESTS
        test_mailing_list = QualtricsMailingList(test_account, test_library_id, test_mailing_list_name, category_name = test_category_name)
        test_mailing_list_id = test_mailing_list.id

        # verify mailing list with created id exists
        request_response = requests.request(
            "GET",
            f"https://{test_account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{test_mailing_list_id}",
            headers = {
                "content-type": "application/json",
                "x-api-token": test_account.api_token
            },
        )
        self.assertEqual(request_response.status_code,200)
