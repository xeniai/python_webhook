import requests

#this is a dummy webhook id
webhook_id = 'thisisadummywebhookidyouneedtogenerateinyourslackaccount'

#Send msg to Slack Channel via Webhook
def send_slackmsg_webhook(message):
    if '"' in message:
        send_msg=message.replace('"','')
    else:
        send_msg = message
        
    payload = '{"text": "%s"}' % send_msg
    result = requests.post(webhook_id, payload)

def read_file(file):
    with open(file, 'r') as fread:
        for line in fread:
            send_slackmsg_webhook(line)

if __name__ == "__main__":
    read_file('file.txt')