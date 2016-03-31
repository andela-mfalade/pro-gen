class Response():
    def __call__(self, status_code=None, req_url=None, flag=None):
        return self.composeResponse(status_code=status_code, req_url=req_url, flag=flag)

    def composeResponse(self, status_code=None, req_url=None, flag=None):
        status_msgs = {
            400: {'message': 'You are doing this wrong. You need to specify the count.'},
            404: {'message': 'Nothing exists on this endpoint.'},
            413: {'message': 'Request Limit Exceeded. 50 or less count allowed per request.'},
            200: {'message': 'Welcome to the Progen API.'},
            'bootstrap-successful': {'message': 'Files Successfully Bootstraped.'},
            'bootstrap-failed': {'message': 'Failed To Bootstrap Files.'},
        }
        tip = {'tip': 'You can request up to 50 profiles per request.'}
        usage = {
            'usage': {
                'sample1': 'http://senongo.pythonanywhere.com/api/v1/profile',
                'sample2': 'http://senongo.pythonanywhere.com/api/v1/profiles?count=<number of desired profile>'
            }
        }
        default_message = {
            'status_code': status_code,
            'links': {'self': req_url},
        }
        custom_error = {'success': False}
        custom_success = {'success': True}

        if not flag:
            if status_code == 200:
                default_message.update(usage)
            if status_code in (200, 201):
                default_message.update(custom_success)
                default_message.update(tip)
            elif status_code in (400, 404, 413):
                default_message.update(usage)
                default_message.update(custom_error)
            default_message.update(status_msgs.get(status_code, {}))
        else:
            default_message.update(status_msgs.get(flag, {}))
        return default_message
