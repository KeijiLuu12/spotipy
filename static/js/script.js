const timeFrame = document.getElementById('top-artist-time');

var top1 = document.getElementById('top-artist-image1');
var top2 = document.getElementById('top-artist-image2');
var top3 = document.getElementById('top-artist-image3');
var top4 = document.getElementById('top-artist-image4');
var top5 = document.getElementById('top-artist-image5');

var top1Name = document.getElementById('top-artist-name1');
var top2Name = document.getElementById('top-artist-name2');
var top3Name = document.getElementById('top-artist-name3');
var top4Name = document.getElementById('top-artist-name4');
var top5Name = document.getElementById('top-artist-name5');

var generateButton = document.getElementById('spotify-button');

var arrayImage = new Array(top1, top2, top3, top4, top5);
var arrayName = new Array(top1Name, top2Name, top3Name, top4Name, top5Name);

var artistHeader = document.getElementById('artist-header');

function changeTimeframe() {

    if (timeFrame.value == 'short_term') { // when 4 weeks option is chosen, updates images and names of artists to be the user's top 5 in the last 4 weeks

        const url = 'http://127.0.0.1:5000/top-artist-short' // url where json file is stored for user's top 5 artists from the last 4 weeks where their image, name is using the Spotify API
        fetch(url)
        .then(response => response.json()) // takes the response from this url, and turns into a json 
        .then (json => { // talong the data from the now converted json, loops through it to update elements on the top artists page
            for (var i = 0; i < json.length; i++) {
                arrayImage[i].src = json[i]['image']
                arrayName[i].innerHTML = '<b>' + json[i]['name'] + '</b>'
            }
        })

        artistHeader.innerHTML = "Your Top 5 artists of the last 4 weeks are:";
       
    }

    if (timeFrame.value == 'medium_term') {

        const url = 'http://127.0.0.1:5000/top-artist-medium'
        fetch(url)
        .then(response => response.json())
        .then (json => {
            for (var i = 0; i < json.length; i++) {
                arrayImage[i].src = json[i]['image']
                arrayName[i].innerHTML = '<b>' + json[i]['name'] + '</b>'
            }
        })

        artistHeader.innerHTML = "Your Top 5 artists of the last 6 months are:";

    }

    if (timeFrame.value == 'long_term') {

        const url = 'http://127.0.0.1:5000/top-artist-long'
        fetch(url)
        .then(response => response.json())
        .then (json => {
            for (var i = 0; i < json.length; i++) {
                arrayImage[i].src = json[i]['image']
                arrayName[i].innerHTML = '<b>' + json[i]['name'] + '</b>'
            }
        })

        artistHeader.innerHTML = "Your Top 5 artists of all time are:";

    }

}

var timeValue = {'timeframe': timeFrame.value};
