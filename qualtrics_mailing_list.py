import requests

from qualtrics_account import QualtricsAccount

class QualtricsMailingList():

    def __init__(self, account : QualtricsAccount, library_id, mailing_list_name, category_name):
        request_response = requests.request(
            "POST",
            f"https://{account.data_center}.qualtrics.com/API/v3/mailinglists/",
            # data=f'{"libraryId":{library_id},"name":{mailing_list_name},"category":{category_name}}',
            data='{ "libraryId":"%s", "name":"%s","category":"%s" }' % (library_id, mailing_list_name, category_name),
            headers={"content-type": "application/json", "x-api-token": account.api_token},
        )
        print(request_response.text)
        self.id = request_response.json()["result"]["id"]