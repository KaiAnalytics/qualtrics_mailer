"""Creates a survey-distribution class for interfacing with Qualtrics API v3

This module creates a class for encapsulating a Qualtrics Survey Distribution
based upon a Qualtrics Mailing List object, Qualtrics Message id, Qualtrics
Survey id, and email settings for send date, from name, reply-to email address,
subject, and from email address, which defaults to "noreply@qemailserver.com"

"""


import requests

from .qualtrics_mailing_list import QualtricsMailingList


class QualtricsDistribution(object):
    """Survey-Distribution Class for interfacing with Qualtrics API v3"""
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
        """Initializes a Qualtrics survey-distribution object

        Args:
            mailing_list: a QualtricsMailingList object with initialized
                Qualtrics Account sub-object
            message_id: a Qualtrics message id; see https://api.qualtrics.com/
                docs/finding-qualtrics-ids
            survey_id: a Qualtrics survey id; see https://api.qualtrics.com/
                docs/finding-qualtrics-ids
            send_date: the send datetime for the survey distribution being
                created in ISO 8601 format; see https://api.qualtrics.com/
                docs/dates-and-times
            from_name: the from name for the survey distribution being created
            reply_email: the reply-to email address for the survey distribution
                being created
            subject: the email subject for the survey distribution being created
            from_email: the from name for the survey distribution being created,
                defaulting to the Qualtrics-supplied noreply@qemailserver.com;
                see https://www.qualtrics.com/support/survey-platform/
                distributions-module/email-distribution/emails/
                using-a-custom-from-address/

        """
        self.mailing_list = mailing_list
        self.message_id = message_id
        self.survey_id = survey_id
        self.send_date = send_date
        self.from_name = from_name
        self.reply_email = reply_email
        self.subject = subject
        self.from_email = from_email

        # make Qualtrics API v3 call to create survey distribution
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

        # extract distribution id from HTTP response
        self.id = request_response.json()["result"]["id"]

    @property
    def details(self) -> dict:
        """Returns survey-distribution details without caching"""
        request_response = requests.request(
            "GET",
            f"https://{self.mailing_list.account.data_center}.qualtrics.com"
            f"/API/v3/distributions/{self.id}?surveyId={self.survey_id}",
            headers={
                "x-api-token": self.mailing_list.account.api_token
            },
        )
        return request_response.json()['result']
