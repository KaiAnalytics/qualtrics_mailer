"""Creates an account class for interfacing with Qualtrics API v3

This module creates a class for encapsulating a Qualtrics Account based upon API
token and data center, including a method for reading an API token from a file.

"""


class QualtricsAccount(object):
    """Account Class for interfacing with Qualtrics API v3"""

    def __init__(
            self,
            api_token: str = None,
            data_center: str = None
    ):
        """Initializes QualtricsAccount object using API Token and Date Center

        Args:
            api_token: a Qualtrics API v3 token; see https://www.qualtrics.com/
                support/integrations/api-integration/overview/
            data_center: a Qualtrics account data center specific to the account
                associated with the API token; see https://api.qualtrics.com/
                docs/root-url

        """
        self.api_token = api_token
        self.data_center = data_center

    def set_api_token_from_file(self, fp) -> None:
        """Loads Qualtrics API v3 token from file

        Args:
            fp: pointer to file or file-like object that is ready to read from
                and contains a Qualtrics API v3 token as the next line to read

        """
        self.api_token = fp.readline()
