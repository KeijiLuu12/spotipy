from flask import Flask, render_template, request, jsonify
import recommendation

app = Flask(__name__)

@app.route('/home')
def home():

    return render_template('home.html')

@app.route('/artist-stats')
def stats_artist():

    top_artist = recommendation.get_top_artists('short_term', 50) # gets access to information from Spotify API with artists' images, name and compiles it into a list

    return render_template('artist-stats.html', artists=top_artist) #returns the html template, with the top_artist list subbing in for the elements that involve a user's top artists

@app.route('/song-stats')
def stats_song():

    top_songs = recommendation.get_top_songs('short_term', 50) # same as above function but with user's top songs

    return render_template('song-stats.html', songs=top_songs)
    
@app.route('/artists', methods=['GET', 'POST'])
def top_artists():

    if request.method == "POST": # Once generate is clicked, receives the information entered about what kind of playlist is being generated (timeframe of top artists, number of songs) received from the JS script

        timeframe = request.form.get('time-period')

        num_songs = request.form.get('num-songs')

        recommendation.create_playlists_recommendation(timeframe, int(num_songs)) # takes information from JavaScript and creates the playlist based on user selection
        
        return render_template('playlist-generated.html') # takes usser to a success page

    top_artist = recommendation.get_top_artists('short_term', 5) # gets user's top artist from last 4 weeks to display thei image and name

    return render_template('top-artist.html', artists=top_artist ) # page that displays when user first clicks login and successfully links their account

@app.route('/generated')
def generated():

    return render_template('playlist-generated.html')

@app.route('/top-artist-medium') #following functions utilize Spoify API to get information on top artist/songs for different time frames and stores that information as a json file to be accessed when the user clicks on different timeframe options within the top-artist page so JS can dynmanically update information on the page
def top_artist_timeframe_medium():

    top_artist = recommendation.get_top_artists('medium_term', 50) #top artists of past 6 months

    artist_json = [] # creates list representing json file
  
    for artist in top_artist: #loops through json file for each artist to get important data needed from Spotify API like their image and name

        artist_json.append({"name": artist[1], "image": artist[2]})
       

    top_artist = jsonify(artist_json)

    return top_artist

@app.route('/top-artist-short') 
def top_artist_timeframe_short():

    top_artist = recommendation.get_top_artists('short_term', 50)

    artist_json = []
   
    for artist in top_artist:

        artist_json.append({"name": artist[1], "image": artist[2]})
        

    top_artist = jsonify(artist_json)

    return top_artist

@app.route('/top-artist-long') 
def top_artist_timeframe_long():

    top_artist = recommendation.get_top_artists('long_term', 50)

    artist_json = []

    for artist in top_artist:

        artist_json.append({"name": artist[1], "image": artist[2]}) # get_top_songs returns tuple with artist uri, artist name and artist image, since we don't need uri, takes only items at index 1 and 2 which are name and image

    top_artist = jsonify(artist_json)

    return top_artist

@app.route('/top-songs-short')
def top_song_timeframe_short():

    top_songs = recommendation.get_top_songs("short_term", 50)

    song_json = []

    for song in top_songs:

        song_json.append({"song_name": song[0], "image": song[1], "artist": song[2]})

    top_songs = jsonify(song_json)

    return top_songs

@app.route('/top-songs-medium')
def top_song_timeframe_medium():

    top_songs = recommendation.get_top_songs("medium_term", 50)

    song_json = []

    for song in top_songs:

        song_json.append({"song_name": song[0], "image": song[1], "artist": song[2]})

    top_songs = jsonify(song_json)

    return top_songs

@app.route('/top-songs-long')
def top_song_timeframe_long():

    top_songs = recommendation.get_top_songs("long_term", 50)

    song_json = []

    for song in top_songs:

        song_json.append({"song_name": song[0], "image": song[1], "artist": song[2]})

    top_songs = jsonify(song_json)

    return top_songs


@app.route('/gettime', methods=['POST'])
def get_time():

    data= request.get_json()
    time = data['timeframe']
    return time
    
