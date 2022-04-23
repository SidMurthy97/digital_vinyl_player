'''Execute this script to run the player'''

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.getenv("VINYL_CLIENT_ID")
CLIENT_SECRET = os.getenv("VINYL_CLIENT_SECRET")

 
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8080",
        scope="user-read-playback-state,user-modify-playback-state"))
        