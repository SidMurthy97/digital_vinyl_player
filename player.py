'''Execute this script to run the player'''

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.getenv("VINYL_CLIENT_ID")
CLIENT_SECRET = os.getenv("VINYL_CLIENT_SECRET")

id_to_track = {703790094799:'spotify:track:043dDJ9u0PQ3ooAXMgcwOe',
               565828783159:'spotify:track:0gplL1WMoJ6iYaPgMCL0gX'} 




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://google.com/",
        scope="user-read-playback-state,user-modify-playback-state"))

reader = SimpleMFRC522()


while True:
    try:
        print("waiting for rfid")
        id = reader.read_id()
        print(f"read if as: {id}")

        if id in id_to_track:
            print("track exists")
            track = id_to_track[id]
            sp.start_playback(uris = [track])
    finally:
        GPIO.cleanup()