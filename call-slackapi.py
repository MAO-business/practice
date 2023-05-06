from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-5201449299137-5197091566626-nsDMjD3t0fNmAyEG09fljDkI")

try:
    response = client.files_upload(
        channels="#proj-test",
        file="path/to/file",
    )
    print("File uploaded successfully")
except SlackApiError as e:
    print("Error uploading file: {}".format(e))