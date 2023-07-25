from flask import Flask
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keys


scope = "user-top-read user-read-private playlist-modify-private"

def get_top_artists():

    top_artists_list = []

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=keys.client_id, client_secret= keys.client_secret, redirect_uri= keys.redirect_uri, scope=scope))

    top_artists = sp.current_user_top_artists(limit=5, time_range = "short_term")

    for artist in top_artists['items']:
        top_artists_list.append(artist['uri'])
        
    return top_artists_list

def create_playlists_recommendation():

    top_artist_seeds = get_top_artists()

    user_id = get_user_id()

    recommendation_list = []

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= keys.client_id, client_secret= keys.client_secret, redirect_uri= keys.redirect_uri, scope=scope))

    playlist_name = "Recommended for you " + datetime.today().strftime('%B %d %Y')

    playlist = sp.user_playlist_create(user_id, playlist_name, False)

    playlist_id = playlist["id"]

    recommendation = sp.recommendations(seed_artists=top_artist_seeds, limit=20)

    for track in recommendation['tracks']:
        recommendation_list.append(track['uri'])


    sp.user_playlist_add_tracks(user_id, playlist_id, recommendation_list)

    return(playlist_id)
    
def get_user_id():

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= keys.client_id, client_secret= keys.client_secret, redirect_uri= keys.redirect_uri, scope=scope))

    user_info = sp.me()

    user_id = str(user_info['id'])

    return user_id
