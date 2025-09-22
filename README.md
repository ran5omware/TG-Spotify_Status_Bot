# Spotify Status Bot

This project is a Telegram bot that updates the description of a Telegram channel based on the current track playing on Spotify. If the track is paused or nothing is playing, the bot will revert to a default status.

## Features

- Checks which track is currently playing on Spotify.
- Updates the Telegram channel description with the track name, album, and artist.
- If the track is paused or nothing is playing, it reverts the description to a default status.
- Works using `spotipy` for Spotify API integration and `aiogram` for Telegram API integration.
- Authorization via Spotify OAuth with the ability to save the token for automatic renewal.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ran5omware/TG-Spotify_Status_Bot.git
cd TG-Spotify_Status_Bot
```

### 2. Create a virtual environment

For Python 3, create a virtual environment:

```bash
python3 -m venv spotify-status-env
source spotify-status-env/bin/activate  # For Linux/Mac
.\spotify-status-env\Scripts\activate  # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Spotify authorization data

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application Redirect URIs you can make http://127.0.0.1:8888/callback.
2. Get your **Client ID**, **Client Secret**, and set the **Redirect URI** for OAuth.
3. Save these details in a `.env` file or replace the corresponding variables in the code:
   ```python
   SPOTIFY_CLIENT_ID = 'your_spotify_client_id'
   SPOTIFY_CLIENT_SECRET = 'your_spotify_client_secret'
   SPOTIFY_REDIRECT_URI = 'your_spotify_redirect_uri'
   SPOTIFY_USERNAME = 'your_spotify_username'
   API_TOKEN = 'your_telegram_bot_token'
   DEFAULT_STATUS = 'Hello!\nThis is default status'
   CHANNEL_ID = '-12345678'
   ```

### 5. Spotify Authorization

On the first run, the script will generate a link for you to authorize the bot on Spotify. You'll need to visit the link, log in, and grant access to your Spotify account. After that, an authorization token file will be created next to `main.py`, which can be used for subsequent runs without the need to reauthorize.

### 6. Running the Bot

To run the bot:

```bash
python path_to_the_bot_dir/TG-Spotify_Status_Bot/main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Potential improvements

- The ability to customize the status update (e.g., scheduling updates).
- Adding a command for manual status updates.
- Extending functionality to work with other music streaming services.

---

**Note:** Ensure your bot has admin rights in the Telegram channel to update the description.

---

This README covers all the main steps for setting up and running the bot. Feel free to adapt it depending on additional configurations or requirements for your project.
