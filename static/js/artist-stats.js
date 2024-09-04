const timeFrame = document.getElementById("top-artist-time");
const numTopArtists = 50;

let arrayTopArtistName = new Array(numTopArtists);
let arrayTopArtistImage = new Array(numTopArtists);


for (var i = 0; i < numTopArtists; i++) {

    arrayTopArtistName[i] = document.getElementById("top-artist-name" + (i+1));
    arrayTopArtistImage[i] = document.getElementById("top-artist-image" + (i+1));

}

function changeTimeframe() {

    if (timeFrame.value == 'short_term') { // when 4 weeks option is chosen, updates images and names of artists to be the user's top 5 in the last 4 weeks

        const url = 'http://127.0.0.1:5000/top-artist-short' // url where json file is stored for user's top 50 artists from the last 4 weeks where their image, name is using the Spotify API
        fetch(url)
        .then(response => response.json()) // takes the response from this url, and turns into a json 
        .then (json => { // talong the data from the now converted json, loops through it to update elements on the top artists page
            for (var i = 0; i < numTopArtists; i++) {
                arrayTopArtistImage[i].src = json[i]['image']
                arrayTopArtistName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['name'] + '</b>'
            }
        })
       
    }

    if (timeFrame.value == 'medium_term') {

        const url = 'http://127.0.0.1:5000/top-artist-medium'
        fetch(url)
        .then(response => response.json())
        .then (json => {
            for (var i = 0; i < numTopArtists; i++) {
                arrayTopArtistImage[i].src = json[i]['image']
                arrayTopArtistName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['name'] + '</b>'
            }
        })

    }

    if (timeFrame.value == 'long_term') {

        const url = 'http://127.0.0.1:5000/top-artist-long'
        fetch(url)
        .then(response => response.json())
        .then (json => {
            for (var i = 0; i < numTopArtists; i++) {
                arrayTopArtistImage[i].src = json[i]['image']
                arrayTopArtistName[i].innerHTML = '<b>' + (i+1) +  ". " + json[i]['name'] + '</b>'
            }
        })

    }

}
