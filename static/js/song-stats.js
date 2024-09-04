const timeFrame = document.getElementById("top-songs-time");
const numTopSongs = 50;

let arrayTopSongsName = new Array(numTopSongs);
let arrayTopSongsImage = new Array(numTopSongs);

for (var i = 0; i < numTopSongs; i++) {

    arrayTopSongsName[i] = document.getElementById("top-song-name" + (i+1));
    arrayTopSongsImage[i] = document.getElementById("top-song-image" + (i+1));

}


function changeTimeframe() {

    if (timeFrame.value == 'short_term') { // when 4 weeks option is chosen, updates images and names of artists to be the user's top 5 in the last 4 weeks

        const url = 'http://127.0.0.1:5000/top-songs-short' // url where json file is stored for user's top 50 artists from the last 4 weeks where their image, name is using the Spotify API
        fetch(url)
        .then(response => response.json()) // takes the response from this url, and turns into a json 
        .then (json => { // talong the data from the now converted json, loops through it to update elements on the top artists page
            for (var i = 0; i < numTopSongs; i++) {
                arrayTopSongsImage[i].src = json[i]['image'];
                arrayTopSongsName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['song_name'] +  '</b>' + " | " + json[i]["artist"] 
            }
        })
       
    }

    if (timeFrame.value == 'medium_term') { // when 4 weeks option is chosen, updates images and names of artists to be the user's top 5 in the last 4 weeks

        const url = 'http://127.0.0.1:5000/top-songs-medium' // url where json file is stored for user's top 50 artists from the last 4 weeks where their image, name is using the Spotify API
        fetch(url)
        .then(response => response.json()) // takes the response from this url, and turns into a json 
        .then (json => { // talong the data from the now converted json, loops through it to update elements on the top artists page
            for (var i = 0; i < numTopSongs; i++) {
                arrayTopSongsImage[i].src = json[i]['image']
                arrayTopSongsName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['song_name'] +  '</b>' + " | " + json[i]["artist"] 
            }
        })
       
       
    }

    if (timeFrame.value == 'long_term') { // when 4 weeks option is chosen, updates images and names of artists to be the user's top 5 in the last 4 weeks

        const url = 'http://127.0.0.1:5000/top-songs-long' // url where json file is stored for user's top 50 artists from the last 4 weeks where their image, name is using the Spotify API
        fetch(url)
        .then(response => response.json()) // takes the response from this url, and turns into a json 
        .then (json => { // talong the data from the now converted json, loops through it to update elements on the top artists page
            for (var i = 0; i < numTopSongs; i++) {
                arrayTopSongsImage[i].src = json[i]['image']
                arrayTopSongsName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['song_name'] +  '</b>' + " | " + json[i]["artist"] 
            }
        })
       
    }


}