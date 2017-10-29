from datetime import datetime
from io import StringIO
from unittest import TestCase

import requests

import test_config
from qualtrics_account import QualtricsAccount
from qualtrics_mailing_list import QualtricsMailingList


class APITokenManagementTests(TestCase):

    def test_set_api_token_from_file(self):
        # set a test file pointer to a file that exactly one line will be read
        # from to get an API token
        test_token = "This is a test token! :)"
        test_fp = StringIO(test_token)

        # initiate a QualtricsAccount object which can be passed to a
        # QualtricsSurvey or QualtricsDistribution object when they're created
        test_account = QualtricsAccount()
        test_account.set_api_token_from_file(test_fp)
        self.assertEqual(test_token,test_account.api_token)


class CreateMailingListObject(TestCase):

    def test_mailing_list_init(self):
        # data center, libraryid, mailinglistname, categoryname * optional *
        # Qualtrics Account object initialization includes setting data center, libraryID

        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = datetime.now().strftime('%Y%m%d-%H%M%S')
        test_category_name = "Test Folder" #
        test_mailing_list = QualtricsMailingList(test_account, test_library_id, test_mailing_list_name, category_name = test_category_name)
        test_mailing_list_id = test_mailing_list.id

        request_response = requests.request(
            "GET",
            f"https://{test_account.data_center}.qualtrics.com/API/v3/mailinglists/{test_mailing_list_id}",
            headers = {"content-type": "application/json", "x-api-token": test_account.api_token},
        )
        print(request_response.text)
        self.assertEqual(request_response.status_code,200)

