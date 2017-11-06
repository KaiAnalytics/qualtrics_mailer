"""Creates a class for interfacing with Qualtrics API v3

This module creates a class for encapsulating API token and data center.
This module also creates a method for loading an API token from a file.

"""


class QualtricsAccount(object):
    """Class for interfacing with Qualtics API v3"""

    def __init__(
            self,
            api_token: str = None,
            data_center: str = None
    ):
        """Initializes QualtricsAccount objects based upon API Token and Date Center

        Args:
            api_token: Qualtrics Account API v3 token
            data_center: Qualtrics center root url;
                see https://api.qualtrics.com/docs/root-url
        """
        self.api_token = api_token
        self.data_center = data_center

    def set_api_token_from_file(self, fp) -> None:
        """Loads API token from file

        Args:
            fp: pointer to file or file-like object that is ready to read from
                and contains a Qualtrics API v3 token as the next full-line to be read
        """
        self.api_token = fp.readline()
