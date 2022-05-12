from os import environ

host = environ["CTFD_HOST"]
api_token = environ["CTFD_API_KEY"]
sleep_time = 30 # seconds
webhook_url = environ["DISCORD_WEBHOOK_URL"]


print(host)
print(api_token)
print(webhook_url)
