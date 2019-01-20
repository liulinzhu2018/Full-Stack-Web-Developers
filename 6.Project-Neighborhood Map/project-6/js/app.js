"use strict";
var Loc = function(data) {
    this.id = data.id;
    this.title = data.title;
    this.location = data.location;
};
var map;
// Create a new blank array for all the listing markers.
var markers = [];
var largeInfowindow;

function initMap() {
    // Constructor creates a new map - only center and zoom are required.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 40.7413549,
            lng: -73.9980244
        },
        zoom: 13,
        mapTypeControl: false
    });
    largeInfowindow = new google.maps.InfoWindow();
    // Style the markers a bit. This will be our listing marker icon.
    var defaultIcon = makeMarkerIcon('0091ff');
    // Create a "highlighted location" marker color for when the user
    // mouses over the marker.
    var highlightedIcon = makeMarkerIcon('FFFF24');
    // The following group uses the location array to create an array of markers on initialize.
    locations.forEach(function(locItem) {
        // Get the position from the location array.
        var position = locItem.location;
        var title = locItem.title;
        // Create a marker per location, and put into markers array.
        var marker = new google.maps.Marker({
            map: map,
            draggable: true,
            position: position,
            title: title,
            animation: google.maps.Animation.DROP,
            icon: defaultIcon,
            id: locItem.id
        });
        // Push the marker to our array of markers.
        markers.push(marker);
        // Create an onclick event to open an infowindow at each marker.
        marker.addListener('click', function() {
            populateInfoWindow(this, largeInfowindow);
            showWikiInfo(this.title);
        });
        // Create animation at marker
        marker.addListener('click', function() {
            window.setTimeout(toggleBounce(this), 2000);
        });
        // Two event listeners - one for mouseover, one for mouseout,
        // to change the colors back and forth.
        marker.addListener('mouseover', function() {
            this.setIcon(highlightedIcon);
        });
        marker.addListener('mouseout', function() {
            this.setIcon(defaultIcon);
        });
    });
    showMarkers();
}
// This function takes in a COLOR, and then creates a new marker
// icon of that color. The icon will be 21 px wide by 34 high, have an origin
// of 0, 0 and be anchored at 10, 34).
function makeMarkerIcon(markerColor) {
    var markerImage = new google.maps.MarkerImage(
        'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|' +
        markerColor + '|40|_|%E2%80%A2', new google.maps.Size(21, 34), new google
        .maps.Point(0, 0), new google.maps.Point(10, 34), new google.maps.Size(
            21, 34));
    return markerImage;
}

function toggleBounce(marker) {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
}
// This function populates the infowindow when the marker is clicked. We'll only allow
// one infowindow which will open at the marker that is clicked, and populate based
// on that markers position.
function populateInfoWindow(marker, infowindow) {
    // Check to make sure the infowindow is not already opened on this marker.
    if (infowindow.marker != marker) {
        infowindow.marker = marker;
        infowindow.setContent('<div>' + marker.title + '</div>');
        infowindow.open(map, marker);
        // Make sure the marker property is cleared if the infowindow is closed.
        infowindow.addListener('closeclick', function() {
            infowindow.marker = null;
        });
    }
}
// This function will loop through the markers array and display them all.
function showMarkers() {
    var bounds = new google.maps.LatLngBounds();
    // Extend the boundaries of the map for each marker and display the marker
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
        bounds.extend(markers[i].position);
    }
    map.fitBounds(bounds);
}
// This function will loop through the listings and hide them all.
function hideMarkers() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
}
// This function will show location Infowindow
function showLoc(id) {
    if (id < markers.length) {
        populateInfoWindow(markers[id], largeInfowindow);
    } else {
        window.alert("no location!");
    }
}

var wikiList = ko.observableArray([]);

function showWikiInfo(cityStr) {
    var wikiUrl = 'http://en.wikipedia.org/w/api.php?action=opensearch&search=' +
        cityStr + '&format=json&callback=wikiCallback';
    wikiList.destroyAll();
    $.ajax({
        url: wikiUrl,
        dataType: "jsonp",
        success: function(response) {
            var articleList = response[1];
            for (var i = 0; i < articleList.length; ++i) {
                var articleStr = articleList[i];
                var wikiElem = {};
                wikiElem.title = articleList[i];
                var url = 'http://en.wikipedia.org/wiki/' +
                    articleStr;
                wikiElem.url = url;
                wikiList.push(wikiElem);
            }
        }
    }).fail(function() {
        alert(
            'There is something wrong. Loading wiki information failed.'
        );
    });
}
var ViewModel = function() {
    var self = this;
    // list all location
    this.locList = ko.observableArray([]);
    this.showLocList = function() {
        self.locList.destroyAll();
        locations.forEach(function(locItem) {
            self.locList.push(new Loc(locItem));
        });
    };
    this.showLocList();
    // when click one location in the list,
    // view open the infomation window for the associated marker
    // and show wiki list
    this.setLoc = function(clickedLoc) {
        showLoc(clickedLoc.id);
        showWikiInfo(clickedLoc.title);
    };
    // filt location list and filt markers
    this.inputTitle = ko.observable("");
    this.locationList = function() {
        this.showMarkerAndList();
        var input = this.inputTitle();
        self.locList.remove(function(item) {
            return item.title.toLowerCase().indexOf(input.toLowerCase()) <
                0;
        });
        markers.forEach(function(markItem) {
            if (markItem.title.toLowerCase().indexOf(input.toLowerCase()) <
                0) {
                markItem.setMap(null);
            }
        });
    };
    // show city wikipedia data
    this.showWiki = function() {
        showWikiInfo(this.inputTitle());
    };
    // show all markers on map and list all location
    this.showMarkerAndList = function() {
        showMarkers();
        this.showLocList();
    };
    // hide all markers on map
    this.hideMarkers = function() {
        hideMarkers();
    };
};
ko.applyBindings(new ViewModel());