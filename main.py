import typing
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.getenv('API_TOKEN', '')
DEFAULT_STATUS = os.getenv('DEFAULT_STATUS', '')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID', '')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET', '')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', '')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME', '')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', '0'))

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-read-currently-playing",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    username=SPOTIFY_USERNAME
))

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

current_playing: typing.List[typing.Union[str, str, str]] = []


async def get_current_description():
    try:
        chat_info = await bot.get_chat(CHANNEL_ID)
        return chat_info.description
    except Exception as e:
        print(f"Error while getting channel description: {e}")
        return None


async def update_status():
    global current_playing
    try:
        current = spotify.current_user_playing_track()

        if current:
            if not current.get('is_playing', False):
                if current_playing:
                    current_description = await get_current_description()
                    if current_description != DEFAULT_STATUS:
                        print("Updating channel description to default status...")
                        await bot.set_chat_description(CHANNEL_ID, DEFAULT_STATUS)
                current_playing = ["track", "album", "artist"]
            else:
                track = current["item"]["name"]
                album = current["item"]["album"]["name"]
                artist = current["item"]["artists"][0]["name"]
                new_status = f"🎧 {artist} - {track} ({album})"

                current_description = await get_current_description()

                if new_status != current_description:
                    print("Updating channel description...")
                    await bot.set_chat_description(CHANNEL_ID, new_status)
                    print(f"🎧 Spotify | {track} - {artist}")
                    current_playing = [track, album, artist]
                else:
                    print("Description is unchanged, no update needed.")
        else:
            print("Nothing is playing or track is paused.")
            if current_playing:
                current_description = await get_current_description()
                if current_description != DEFAULT_STATUS:
                    print("Updating channel description to default status...")
                    await bot.set_chat_description(CHANNEL_ID, DEFAULT_STATUS)
            current_playing = ["track", "album", "artist"]
    except Exception as e:
        print(f"Error while updating status: {e}")


async def periodic_status_update():
    while True:
        await update_status()
        await asyncio.sleep(10)


if __name__ == '__main__':
    print("Starting the bot...")
    try:
        asyncio.run(periodic_status_update())
    except Exception as e:
        print(f"Error while running the bot: {e}")
