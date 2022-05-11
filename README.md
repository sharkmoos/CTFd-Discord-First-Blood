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

- [x] `sleep_time`: The frequency CTFd is queried.
- [ ] Custom blood messages

### To-Do

- [ ] Random select from a number of messages

