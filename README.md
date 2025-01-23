# Qobuz Downloader with GUI

Scrape and download `.flac` music from Qobuz, asynchronously.
<br>
Comes with a convenient GUI that offers various features, making the whole process much easier and faster.

## Features

- **Browse and remember Download Directory**: Easily set the download directory and the application remembers your preferences.
- **Paste from Clipboard**: Quickly paste URLs from the clipboard into the application.
- **Clear URLs**: Conveniently clear the list of download URLs with a single click.
- **Parallel Downloads**: Download multiple files simultaneously, saving time.
- **Album Cover Metadata Support**: Automatically includes album cover metadata in the downloaded files.
- **No Account Required**: No need to have a Qobuz account, as it is provided when the app requested the configs from my github API.
- Added two app types, for those who want faster app, download the Qobuz-DL_folder.zip and run the main.exe there, while who wants simpler one, download the Qobuz-DL.exe

![GUI Preview](https://user-images.githubusercontent.com/67509348/236596246-62a7cbd9-faad-4153-8f87-dc5b2a79a0c4.png)

## Module usage

Using `qobuz-dl` as a module is really easy. Basically, the only thing you need is `QobuzDL` from `core`.

```python
import logging
from qobuz_dl.core import QobuzDL

logging.basicConfig(level=logging.INFO)

email = "your@email.com"
password = "your_password"

qobuz = QobuzDL()
qobuz.get_tokens() # get 'app_id' and 'secrets' attrs
qobuz.initialize_client(email, password, qobuz.app_id, qobuz.secrets)

qobuz.handle_url("https://play.qobuz.com/album/va4j3hdlwaubc")
```

Attributes, methods and parameters have been named as self-explanatory as possible.

## Fun Fact

I use this program daily!

## Disclaimer

- This tool was written for educational purposes. I will not be responsible if you use this program in bad faith. By using it, you are accepting the [Qobuz API Terms of Use](https://static.qobuz.com/apps/api/QobuzAPI-TermsofUse.pdf).
- `qobuz-dl` is not affiliated with Qobuz