"""Creates a class for interfacing with Qualtrics API v3

This module creates a class that has methods for creating a mailing list and
    for exporting a JSON object into a Qualtrics mailing list from a csv file
"""


import json

import pandas as pd
import requests

from qualtrics_account import QualtricsAccount


class QualtricsMailingList(object):
    """Class for interfacing with Qualtics API v3"""
    def __init__(
            self,
            account: QualtricsAccount,
            library_id: str,
            mailing_list_name: str,
            category_name: str
    ):
        """Initializes a mailing list object

        Arges:
            account: Consists of attributes inherited from the Qualtrics Account class
            library_id: It indicates the ID of the library (aka.Qualtrics "working directory")
                where  mailing lists is saved
            mailing_list_name: The name for a mailing list
            category_name: Tag/Group in which to create the new mailing list
        """
        self.account = account
        self.library_id = library_id
        self.mailing_list_name = mailing_list_name
        self.category_name = category_name

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
        self.id = request_response.json()["result"]["id"]

    def import_contact_list_from_csv_file(self, fp):
        """Imports a contact list from csv file into a mailing list using a Qualtrics v3 API call.
        This import method converts the csv file into a JSON object.
        This import method will confirm the process completed before proceeding

        Args:
            fp: pointer to the csv object that is ready to read from

        Qualtrics documentation:
            https://api.qualtrics.com/docs/create-contacts-import
            https://api.qualtrics.com/docs/get-contacts-import
        """
        contact_list = json.loads(pd.read_csv(fp).to_json(orient='records'))

        # noinspection SpellCheckingInspection
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
        progress_id = request_response.json()["result"]["id"]

        request_check_progress = 0
        while request_check_progress < 100:
            # noinspection SpellCheckingInspection
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
        """Returns the mailing list's contact list using a Qualtrics API v3 call"""
        request_response = requests.request(
            "GET",
            f"https://{self.account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{self.id}/contacts",
            headers={
                "x-api-token": self.account.api_token,
            },
        )
        return request_response.json()["result"]["elements"]
