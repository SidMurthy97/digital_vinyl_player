'''Execute this script to run the player'''

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.getenv("VINYL_CLIENT_ID")
CLIENT_SECRET = os.getenv("VINYL_CLIENT_SECRET")

id_to_track = {703790094799:'spotify:track:043dDJ9u0PQ3ooAXMgcwOe'} 




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://google.com/",
        scope="user-read-playback-state,user-modify-playback-state"))

reader = SimpleMFRC522()


test_id = 703790094799
track = id_to_track[test_id]
#sp.start_playback(uris = [track])