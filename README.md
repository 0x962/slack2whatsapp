# slack2whatsapp

A simple, barebones python script to forward messages from your Slack channels to your Whatsapp. Designed to forward notifications from build servers, uptime monitors, task managers and more to your whatsapp. 

Integrating with Slack allows you to add a large number of notification channels, since most third party services will allow integrating with slack. 

- Jenkins -> Slack -> Whatsapp.
- Prometheus -> Slack -> Whatsapp. 
- Asana -> Slack - Whatsapp. 

Designed to work with AWS Lambda. 

# Deployment 

- You must have a slack organisation. 
- Create a Twilio account, and a whatsapp sandbox account.

1. Start a new AWS Lambda application. 
2. Add an API trigger. 
3. Edit Layer 0, and upload the zip in this directory. 
4. Increase time out from 3 seconds to 6, or a larger number. 
5. Add the environment keys `twilio_account_sid` and `twilio_auth_token` with the appropriate values obtained from your Twilio account. Also add `whatsapp-from` and `whatsapp-to` mobile numbers in the format `whatsapp:<country_code><mobile_number>`
6. Add `outgoing-webhooks` to your slack channel. 
7. Select `trigger-words` if needed, not required. 
8. Add your API trigger URL to the configuration. 
9. Save the configuration. 
10. Good to go. 

# Development 

1. Edit `src/lambda_function.py` as needed. 
2. `cd dist/`
3. `cp -rf src/* . `
4. `cp -rf venv/lib/python-2.7/site-packages/* .`
5. `zip ../lambda.zip .`
6. Upload the zip to your lambda function. 

Tip: 

Twilio does not let you send messages to multiple users with a single API call. Iter over a list to send notifications to multiple users. 

Have fun. 

