# CTF Discord - CTFd First Blood Integration

Author: sharkmoos

## Use

There are three key fields in `./src/config.py`

```py
api_token = "" # The API token for CTFd

host = "" # The URL of the CTFd infrastructure

webhook_url = "" # The webhook for discord
```

Other configurables include:

- `sleep_time`: The frequency CTFd is queried.
- `first_blood_announce_string` : The string that is used for the discord announcement

