import json

import pandas as pd
import requests

from qualtrics_account import QualtricsAccount


class QualtricsMailingList(object):
    def __init__(
            self,
            account: QualtricsAccount,
            library_id: str,
            mailing_list_name: str,
            category_name: str
    ):
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
        # The contact list object needs to be a JSON object or a JSON file
        # The import process will need to convert the data format accordingly
        # It will also confirm import process completed before proceeding
        #
        # Qualtrics documentation:
        #   https://api.qualtrics.com/docs/create-contacts-import
        #   https://api.qualtrics.com/docs/get-contacts-import
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
        request_response = requests.request(
            "GET",
            f"https://{self.account.data_center}.qualtrics.com"
            f"/API/v3/mailinglists/{self.id}/contacts",
            headers={
                "x-api-token": self.account.api_token,
            },
        )
        return request_response.json()["result"]["elements"]
