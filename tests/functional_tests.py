'''
Rough Design

    1. hard coded config file with things like API urls

    2. Files that only contain user parameters, like API token

    3.  a) Survey Object <- data center, survey ID
        b) Mailing List Object <- data center, library id (group id), mailing list name, category name (folder name) *optional*
        c) Message Object <- message id, survey object, mailing list object
        d) Importable Contact list
        e) Survey distribution object
'''




# BOBBY'S EXPERIENCE

'''

Users would like to better understand their customer sentiments on an on-going basis. They therefore would like to
regularly conduct satisfaction surveys (e.g. NPS) using Qualtrics. They would like to avoid the manual process of 
preparing a contact (e.g. mailing) list, importing it into Qualtrics and then scheduling a survey to be distributed
on a routine basis (daily/weekly/quarterly).

'''

# Bobby setups their User id token in the Qualtrics Admin page by following the instructions here:
# https://api.qualtrics.com/docs/finding-qualtrics-ids

# Bobby is going to create a Qualtrics Account object by specifying a data center and API token.

# Bobby goes to the Qualtrics.com Admin page to identify the Qualtrics ID associated with their library/group they want to work in

# Bobby creates a new mailing list by specifying the Qualtrics Account object, mailing list name, category name *optional*
# The mailing list object then makes an API call to get its mailing list id

# Bobbby then imports their contact list into the mailing list object
    # The mailing list object needs to be a JSON object or a JSON file
    # The import process will need to convert the data format accordingly
    # It will also confirm import process completed before proceeding
    # Qualtrics documentation:
    #       https://api.qualtrics.com/docs/create-contacts-import
    #       https://api.qualtrics.com/docs/get-contacts-import

# Bobby then distributes the survey to the contact list by specifying the: mailing list object, email settings (to/from/subject), and ISO time to send the survey
    # Qualtrics documentation:
    #       https://api.qualtrics.com/docs/create-survey-distribution
    #       Default survey expiration is 60days (we can add a feature to change this as backlog)

