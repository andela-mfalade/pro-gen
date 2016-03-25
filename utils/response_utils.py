class Response():
    TIP = {'tip': 'You can request up to 50 profiles per request.'}
    USAGE = {
        'usage': {
            'sample1': 'http://progen.pythonanywhere.com/api/v1/profile',
            'sample2': 'http://progen.pythonanywhere.com/api/v1/profiles?count=<number of desired profile>'
        }
    }
    WELCOME_TEXT = {'g_text': 'Welcome to the Progen API.'}

    def __call__(self, status_code=None, descr=None):
        if status_code == 200:
            return self.composeSuccessMessage(descr)
        else:
            return self.composeErrorMessage(status_code, descr)

    def composeErrorMessage(self, status_code=None, descr=None):
        pass

    def composeSuccessMessage(self, descr=None):
        welcome_message = {'message': 'Welcome to the Progen API.'}
        welcome_message.update(self.USAGE)
        welcome_message.update(self.TIP)
        return welcome_message
