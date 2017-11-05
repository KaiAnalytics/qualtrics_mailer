import requests

from qualtrics_mailing_list import QualtricsMailingList


class QualtricsDistribution(object):
    def __init__(
        self,
        mailing_list: QualtricsMailingList,
        message_id: str,
        survey_id: str,
        send_date: str,
        from_name: str,
        reply_email: str,
        subject: str,
        *,
        from_email: str = "noreply@qemailserver.com",
    ):
        self.mailing_list = mailing_list
        self.message_id = message_id
        self.survey_id = survey_id
        self.send_date = send_date
        self.from_name = from_name
        self.reply_email = reply_email
        self.subject = subject
        self.from_email = from_email

        # verify distribution exists
        request_response = requests.request(
            "POST",
            f"https://{self.mailing_list.account.data_center}.qualtrics.com"
            f"/API/v3/distributions/",
            headers={
                "x-api-token": self.mailing_list.account.api_token,
                "Content-Type": "application/json",
            },
            json={
                "surveyLink": {
                    "surveyId": self.survey_id,
                },
                "header": {
                    "fromEmail": self.from_email,
                    "fromName": self.from_name,
                    "replyToEmail": self.reply_email,
                    "subject": self.subject,
                },
                "message": {
                    "libraryId": self.mailing_list.library_id,
                    "messageId": self.message_id,
                },
                "recipients": {
                    "mailingListId": self.mailing_list.id,
                },
                "sendDate": self.send_date,
            }
        )
        self.id = request_response.json()["result"]["id"]

    @property
    def details(self) -> dict:
        request_response = requests.request(
            "GET",
            f"https://{self.mailing_list.account.data_center}.qualtrics.com"
            f"/API/v3/distributions/{self.id}?surveyId={self.survey_id}",
            headers={
                "x-api-token": self.mailing_list.account.api_token
            },
        )
        return request_response.json()