"""Creates a mailing-list class for interfacing with Qualtrics API v3

This module creates a class for encapsulating a Qualtrics Mailing List based
upon a Qualtrics Account object, Qualtrics Library/Group id, and settings for
mailing-list name and category name

"""

import json

import pandas as pd
import requests
from .qualtrics_account import QualtricsAccount


class QualtricsMailingList(object):
    """Mailing-list Class for interfacing with Qualtrics API v3"""
    def __init__(
            self,
            account: QualtricsAccount,
            library_id: str,
            mailing_list_name: str,
            category_name: str
    ):
        """Initializes a Qualtrics mailing-list object

        Args:
            account: a QualtricsAccount object
            library_id: a Qualtrics Library/Group id, which acts similarly to a
                "working directory"; see https://api.qualtrics.com/docs/
                finding-qualtrics-ids
            mailing_list_name: the name for the mailing list being created
            category_name: the category name for the mailing list being created,
                which acts similarly to a "tag" for the mailing list
        """
        self.account = account
        self.library_id = library_id
        self.mailing_list_name = mailing_list_name
        self.category_name = category_name

        # make Qualtrics API v3 call to create mailing list
        request_response = requests.request(
            "POST",
            f"https://{self.account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/",
            data=(
                f'{{"libraryId": "{library_id}",'
                f'"name": "{mailing_list_name}",'
                f'"category": "{category_name}" }}'
            ),
            headers={
                "content-type": "application/json",
                "x-api-token": self.account.api_token,
            },
        )

        # extract mailing list id from HTTP response
        self.id = request_response.json()["result"]["id"]

    def import_contact_list_from_csv_file(self, fp) -> None:
        """Imports a contact list from a csv file using a Qualtrics v3 API call.

        Args:
            fp: pointer to csv file or file-like object having a non-empty
                subset of the following column headers in the next line to be
                read and corresponding data in all following lines:
                - id
                - firstName
                - lastName
                - email
                - language
                - unsubscribed
                - externalReference
                see https://api.qualtrics.com/docs/create-contacts-import

        """

        # convert csv file contents to JSON records format
        contact_list = json.loads(pd.read_csv(fp).to_json(orient='records'))

        # make Qualtrics API v3 call to upload contact list
        request_response = requests.request(
            "POST",
            f"https://{self.account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{self.id}/contactimports",
            json={"contacts": contact_list},
            headers={
                "content-type": "application/json",
                "x-api-token": self.account.api_token,
            },
        )

        # check upload progress until complete
        progress_id = request_response.json()["result"]["id"]
        request_check_progress = 0
        while request_check_progress < 100:
            request_response = requests.request(
                "GET",
                f"https://{self.account.data_center}.qualtrics.com"
                f"/API/v3/mailinglists/{self.id}/contactimports/{progress_id}",
                headers={
                    "x-api-token": self.account.api_token,
                },
            )
            request_check_progress = request_response.json()["result"][
                "percentComplete"]

    @property
    def contact_list(self) -> dict:
        """Returns mailing list's contact list without caching"""
        request_response = requests.request(
            "GET",
            f"https://{self.account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{self.id}/contacts",
            headers={
                "x-api-token": self.account.api_token,
            },
        )
        return request_response.json()["result"]["elements"]
