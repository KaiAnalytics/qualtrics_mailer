from io import StringIO
from unittest import TestCase

import requests

from tests import test_config
from qualtrics_account import QualtricsAccount
from qualtrics_mailing_list import QualtricsMailingList


class QualtricsAccountTests(TestCase):
    def test_set_api_token_from_file(self):
        # set a pointer to a file so that exactly one line will be read to get
        # an API token
        test_token = "This is a test token! :)"
        test_fp = StringIO(test_token)

        # initiate a QualtricsAccount object
        test_account = QualtricsAccount()
        test_account.set_api_token_from_file(test_fp)
        self.assertEqual(test_token, test_account.api_token)


class QualtricsMailingListTests(TestCase):
    def test_mailing_list_init(self):
        # initiate a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initiate a QualtricsMailingList object
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
        self.assertEqual(request_response.status_code, 200)

    def test_import_contact_list_from_csv_file(self):
        # initiate a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initiate a QualtricsMailingList object
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
        contact_list_results = request_response.json()["result"]["elements"]
        self.assertEqual(len(contact_list_results), len(test_contact_list) - 1)

    def test_contact_list_property(self):
        # initiate a QualtricsAccount object
        test_api_token = test_config.API_TOKEN
        test_data_center = test_config.DATA_CENTER
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # initiate a QualtricsMailingList object
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

        # verify contact list has been imported and is accessible from property
        self.assertEqual(len(test_mailing_list.contact_list),
                         len(test_contact_list) - 1)
