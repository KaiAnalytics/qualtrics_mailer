"""Creates a class for interfacing with Qualtrics API v3

This module creates a class for distributing a survey to a mailing list
"""


import requests

from qualtrics_mailing_list import QualtricsMailingList


class QualtricsDistribution(object):
    """Class for interfacing with Qualtics API v3"""
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
        """Initializes a distribution object

        Args:
            mailing_list: Inherits objects from the QualtricsMailingList class
            message_id: Contains information about the body of the email message that is sent to survey recipients.
                Typically, the message is saved in the user's library.
            survey_id: Identifies the survey
            send_date: The date and time the survey will be sent (in ISO 8601 format).
                An example sendDate is 2017-08-07T21:45:00Z.
                Note that this date and time could be in the future if the email distribution is scheduled to send after a delay.
            from_name: The name of the sender. Typically the account owner's name, for instance, John Doe.
            reply_email: The email address of the sender of the email, for example, john@example.com.
                This is the address that will receive a message should the recipient of the email choose reply.
            subject: The email's subject line.
            from_email: The email address of the sender. The default is noreply@qemailserver.com.
                Note that additional setup may be required with Qualtrics and your IT team to use emails with custom domains.
        """
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
        """Returns the distribution using a Qualtrics API v3 call"""
        request_response = requests.request(
            "GET",
            f"https://{self.mailing_list.account.data_center}.qualtrics.com"
            f"/API/v3/distributions/{self.id}?surveyId={self.survey_id}",
            headers={
                "x-api-token": self.mailing_list.account.api_token
            },
        )
        return request_response.json()