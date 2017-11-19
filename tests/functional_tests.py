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
- CATEGORY_NAME_FOR_FUNCTIONAL_TESTS, the category name for the test mailing
    list being created
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

from pprint import pprint
from unittest import TestCase

from qualtrics_mailer import QualtricsAccount, QualtricsDistribution, QualtricsMailingList
from tests import test_config


class ScheduleDistributionTests(TestCase):
    def test_schedule_distribution_with_csv_import(self):
        # BOBBY'S EXPERIENCE

        # Bobby follows the instructions at
        # https://www.qualtrics.com/support/integrations/api-integration
        # /overview/#GeneratingAnAPIToken to generate an API Token

        # Bobby then follows the instructions at
        # https://api.qualtrics.com/docs/root-url to get their data center name

        # Bobby then creates a Qualtrics account object by specifying a data
        # center name and API token
        test_data_center = test_config.DATA_CENTER
        test_api_token = test_config.API_TOKEN
        test_account = QualtricsAccount(test_api_token, test_data_center)

        # Bobby then follows the instructions at
        # https://api.qualtrics.com/docs/finding-qualtrics-ids to find the
        # library/group they want to work in

        # Bobby then creates a new mailing list object by specifying a Qualtrics
        # Account object, library id, mailing list name, and category name
        test_library_id = test_config.LIBRARY_ID
        test_mailing_list_name = test_config.MAILING_LIST_NAME
        test_category_name = test_config.CATEGORY_NAME_FOR_FUNCTIONAL_TESTS
        test_mailing_list = QualtricsMailingList(
            test_account,
            test_library_id,
            test_mailing_list_name,
            test_category_name
        )

        # The mailing list object makes an API call to get its mailing list id
        self.assertRegex(test_mailing_list.id, 'ML_\w+')

        # Bobby then imports their contact list into the mailing list object
        # by passing a file pointer to a CSV file having columns
        # - firstName
        # - lastName
        # - email
        with open('tests/test_contact_list.csv') as fp:
            test_mailing_list.import_contact_list_from_csv_file(fp)

        # Bobby then prints out the contents of the contact list to make sure
        # it was created as expected
        pprint(test_mailing_list.contact_list)

        # Bobby then follows the instructions at
        # https://api.qualtrics.com/docs/finding-qualtrics-ids to determine the
        # id for a survey they would like to distribute

        # Bobby then follows the instructions at
        # https://api.qualtrics.com/docs/finding-qualtrics-ids to determine the
        # id for a message they would like to use to distribute the survey

        # Bobby then creates a distribution object by specifying a mailing list
        # object, a message id, survey id, and email settings for send datetime
        # is ISO 8601 format, from name, reply email address, and subject
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

        # Bobby then prints out the contents of the distribution to make sure it
        # was created as expected
        pprint(test_distribution.details)

        # Bobby can then log into Qualtrics.com and verify the survey project
        # was created as specified using
