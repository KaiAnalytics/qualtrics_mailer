class QualtricsAccount():

    def __init__(self):
        self.api_token = None

    def set_api_token_from_file(self,fp):
        self.api_token = fp.readline()