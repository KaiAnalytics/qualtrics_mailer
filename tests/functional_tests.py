'''
Rough Design

    1. hard coded config file with things like API urls

    2. Files that only contain user parameters, like API token

    3.  a) Survey Object <- data center, survey ID
        b) Mailing List Object <- data center, library id (group id), mailing list name, category name (folder name) *optional*
        c) Message Object <- message id, survey object, mailing list object
        d) Contact list

'''




# BOBBY'S EXPERIENCE

'''

'''

# Bobby setups their User id token in the Qualtrics Admin page by following the instructions here:
# https://api.qualtrics.com/docs/finding-qualtrics-ids

# Bobby calls a helper function to input their Qualtrics API token into a 'token.ini' file
# input()

# Bobby creates a mailing list object by specifying the: data center, library id, mailing list name, category name *optional*
# The mailing list object then makes an API call to get its mailing list id


