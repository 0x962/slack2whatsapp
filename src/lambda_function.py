class Job():
    twilio_account_sid = None
    twilio_auth_token = None

    def run(self, event, context):
        print "Event: " + str(event)
        print "Context: " + str(context)
        self.send_message(event)
        return {
            "event": event
        }

    def get_client(self):
        import os
        from twilio.rest import Client

        self.twilio_account_sid = os.environ.get('twilio_account_sid')
        self.twilio_auth_token = os.environ.get('twilio_auth_token')
        self.whatsapp_from = os.environ.get('whatsapp_from')
        self.whatsapp_to = os.environ.get('whatsapp_to')

        if None in [self.twilio_account_sid, self.twilio_auth_token]:
            raise StandardError("No twilio keys")

        print "Creating twilio client with " + str(self.twilio_account_sid) + " " + str(self.twilio_auth_token)
        return Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_message(self, event):
        client = self.get_client()
        event = event['body']
        event = {x[0] : x[1] for x in [x.split("=") for x in event[1:].split("&") ]}

        user_name = event.get("user_name", "unknown")
        text = event.get("text", "unknown").replace("+", " ")
        timestamp = event.get("timestamp", "unknown")
        wp_body = "*"+ user_name.title() + "* says: \n\n```" + text.rstrip() + "```\n"

        message = client.messages.create(
            body=wp_body,
            from_=self.whatsapp_from,
            to=self.whatsapp_to
        )
        return message.sid

def lambda_handler(event, context):
    job = Job()
    return job.run(event, context)

if __name__ == '__main__':
    body = {u'body': u'token=rM2dmZ4oYXhobRS6iYjf8TZU&team_id=TAWH8L82K&team_domain=aesopwebtechnologies&service_id=528322072898&channel_id=CAVG1R658&channel_name=ci&timestamp=1547994101.000900&user_id=UAVFV17C2&user_name=naved&text=Test+Twilio.', u'resource': u'/slack2twilio', u'requestContext': {u'requestTime': u'20/Jan/2019:14:21:42 +0000', u'protocol': u'HTTP/1.1', u'domainName': u'uk4u39dey8.execute-api.ap-south-1.amazonaws.com', u'resourceId': u'7x0x4s', u'apiId': u'uk4u39dey8', u'resourcePath': u'/slack2twilio', u'httpMethod': u'POST', u'domainPrefix': u'uk4u39dey8', u'requestId': u'b576db4e-1cbe-11e9-b078-79c43c1357e9', u'extendedRequestId': u'TzmOhGs0BcwFmrQ=', u'path': u'/default/slack2twilio', u'stage': u'default', u'requestTimeEpoch': 1547994102534, u'identity': {u'userArn': None, u'cognitoAuthenticationType': None, u'accessKey': None, u'caller': None, u'userAgent': u'Slackbot 1.0 (+https://api.slack.com/robots)', u'user': None, u'cognitoIdentityPoolId': None, u'cognitoIdentityId': None, u'cognitoAuthenticationProvider': None, u'sourceIp': u'54.157.187.181', u'accountId': None}, u'accountId': u'271507579140'}, u'queryStringParameters': None, u'multiValueHeaders': {u'Accept-Encoding': [u'gzip,deflate'], u'X-Forwarded-Port': [u'443'], u'X-Forwarded-For': [u'54.157.187.181'], u'Accept': [u'*/*'], u'User-Agent': [u'Slackbot 1.0 (+https://api.slack.com/robots)'], u'X-Amzn-Trace-Id': [u'Root=1-5c4483f6-1eb92a4590109ab4819211d9'], u'Host': [u'uk4u39dey8.execute-api.ap-south-1.amazonaws.com'], u'X-Forwarded-Proto': [u'https'], u'Content-Type': [u'application/x-www-form-urlencoded']}, u'multiValueQueryStringParameters': None, u'pathParameters': None, u'headers': {u'Accept-Encoding': u'gzip,deflate', u'X-Forwarded-Port': u'443', u'X-Forwarded-For': u'54.157.187.181', u'Accept': u'*/*', u'User-Agent': u'Slackbot 1.0 (+https://api.slack.com/robots)', u'X-Amzn-Trace-Id': u'Root=1-5c4483f6-1eb92a4590109ab4819211d9', u'Host': u'uk4u39dey8.execute-api.ap-south-1.amazonaws.com', u'X-Forwarded-Proto': u'https', u'Content-Type': u'application/x-www-form-urlencoded'}, u'isBase64Encoded': False, u'stageVariables': None, u'path': u'/slack2twilio', u'httpMethod': u'POST'}
    lambda_handler(body, {})

    