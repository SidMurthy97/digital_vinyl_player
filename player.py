#TODO: Specify Device ID/think about what happens if no device is active
    #This isnt possible. I will have to make the rpi an active device...
#TODO: Add logger

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import logging

CLIENT_ID = os.getenv("VINYL_CLIENT_ID")
CLIENT_SECRET = os.getenv("VINYL_CLIENT_SECRET")
DEVICE_ID = os.getenv("VINY_DEVICE_ID")

id_to_track = {703790094799:['spotify:track:043dDJ9u0PQ3ooAXMgcwOe',None],
               565828783159:['spotify:track:0gplL1WMoJ6iYaPgMCL0gX', "easy on me"]} 


#setup spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://google.com/",
        scope="user-read-playback-state,user-modify-playback-state"))

#setup reader
reader = SimpleMFRC522()

#setup logger 
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

prev_id = None
while True:
    try:
        wait_msg = "waiting for rfid"
        print(wait_msg)
        logging.info(wait_msg)
        id = reader.read_id()
        print(f"read if as: {id}")

        '''Play a track if its a recognised ID, but not if its the immediately
        previous ID. This is to block a song restarting if a tag has been 
        left on the player. This should get cleared at some point'''
        if id in id_to_track and id != prev_id:
            # logging.info(f"playing {id_to_track[id][1]}")
            prev_id = id
            track = id_to_track[id][0]
            sp.start_playback(device_id=DEVICE_ID,uris = [track])

    #print the error if it occurs
    except Exception as e:
        print("error is: ", e)
        

    except KeyboardInterrupt:
        break

GPIO.cleanup()