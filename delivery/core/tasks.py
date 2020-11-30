from celery import shared_task, task
import requests
import json
import sys


@shared_task
def send_slack_message(message):
    url = "https://hooks.slack.com/services/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"
    serialize = {"text": message}
    byte_length = str(sys.getsizeof(serialize))
    headers = {'Content-Type': "application/json",
               'Content-Length': byte_length}
    response = requests.post(url,
                             data=json.dumps(serialize),
                             headers=headers,
                             )

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.text


@shared_task
def slack_daily_menu_reminder():

    message = "Hello\n"
    message += "I share with you today's menu :) \n"
    message += "https://nora.cornershop.io/menu/2ab88f1d-8dfb-40ec-b6c1-64478827aae5 \n"
    message += "http://localhost:7000/menu/today/ \n"
    message += "Please order before 11 AM"

    send_slack_message(message)


@shared_task
def send_whatsapp_message(fromPhone, toPhone, message):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    client.messages.create(from_=fromPhone, body=message, to=toPhone,)
