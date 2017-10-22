from io import StringIO
from unittest import TestCase

from qualtrics_account import QualtricsAccount

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