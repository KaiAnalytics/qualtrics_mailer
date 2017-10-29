class QualtricsAccount():

    def __init__(self,api_token=None,data_center=None):
        self.api_token = api_token
        self.data_center = data_center

    def set_api_token_from_file(self,fp):
        self.api_token = fp.readline()