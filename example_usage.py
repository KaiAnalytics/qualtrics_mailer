from datetime import datetime
from pprint import pprint

from qualtrics_mailer import (
    QualtricsAccount,
    QualtricsDistribution,
    QualtricsMailingList
)


# set data center and API token
api_token = '[your account API token]'
data_center = '[your account data center name]'

# initialize Qualtrics Account object
account = QualtricsAccount(api_token, data_center)

# set library id, mailing list, and category name
library_id = '[valid library id for your account]'
mailing_list_name = 'Example Usage List Name'
category_name = 'Example Usage Category Name'

# initialize Qualtrics Mailing List object
mailing_list = QualtricsMailingList(
    account,
    library_id,
    mailing_list_name,
    category_name
)

# import example contact list from test folder
with open('example_mailing_list.csv') as fp:
    mailing_list.import_contact_list_from_csv_file(fp)

# print mailing list's contact list to confirm proper import
pprint(mailing_list.contact_list)

# set message id, survey id, and email settings
message_id = '[valid message id for your account]'
survey_id = '[valid survey id for your account]'
send_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
from_name = 'Example Usage From Name'
reply_email = 'Example.Usage@From.Name'
subject = 'Example Usage Subject'
distribution = QualtricsDistribution(
    mailing_list,
    message_id,
    survey_id,
    send_date,
    from_name,
    reply_email,
    subject,
)

# print survey-distribution details to confirm proper creation
pprint(distribution.details)
