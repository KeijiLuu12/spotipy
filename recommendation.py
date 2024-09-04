from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyPKCE
import keys


scope = "user-top-read user-read-private playlist-modify-private"

def get_top_artists(timeframe, num):

    top_artists_list = []

    sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=keys.client_id, redirect_uri= keys.redirect_uri, scope=scope)) #authentication
    
    top_artists = sp.current_user_top_artists(limit=num, time_range = timeframe)

    for artist in top_artists['items']:
        top_artists_list.append((artist['uri'], artist['name'], artist['images'][0]['url']))
        
    return top_artists_list

def get_top_songs(timeframe, num):

    top_songs_list = []

    sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=keys.client_id, redirect_uri= keys.redirect_uri, scope=scope))

    top_songs = sp.current_user_top_tracks(limit=num, time_range=timeframe)

    for song in top_songs['items']:
        
        top_songs_list.append((song['name'], song['album']['images'][0]['url'], song['artists'][0]['name'])) # format used for each song in the list is title, image and artist

    return top_songs_list

def create_playlists_recommendation(time, num):

    top_artist_seeds = [i[0] for i in get_top_artists(time, 5)]

    user_id = get_user_id()

    recommendation_list = []

    sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=keys.client_id, redirect_uri= keys.redirect_uri, scope=scope))

    playlist_name = "Recommended for you " + datetime.today().strftime('%B %d %Y')

    playlist = sp.user_playlist_create(user_id, playlist_name, False)

    playlist_id = playlist["id"]

    recommendation = sp.recommendations(seed_artists=top_artist_seeds, limit=num)

    for track in recommendation['tracks']:
        recommendation_list.append(track['uri'])

    sp.user_playlist_add_tracks(user_id, playlist_id, recommendation_list)

    return(playlist_id)

def display_reco(playlist_id):

    sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=keys.client_id, redirect_uri= keys.redirect_uri, scope=scope))

    playlist = sp.playlist(playlist_id )

    recommendations_image = []

    for song in playlist['tracks']['items']:
        recommendations_image.append(song['track']['album']['images'][0]['url'])


    return recommendations_image


    
def get_user_id():

    sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=keys.client_id, redirect_uri= keys.redirect_uri, scope=scope))

    user_info = sp.me()

    user_id = str(user_info['id'])

    return user_id
