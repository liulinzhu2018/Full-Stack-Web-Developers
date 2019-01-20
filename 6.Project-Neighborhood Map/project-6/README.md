# Neighborhood Map
It is a single page application featuring a map of our neighborhood or a neighborhood we would like to visit,  
and this application based upon Knockout (follow an MVVM pattern, avoid updating the DOM manually with  
jQuery or JS, use observables rather than forcing refreshes manually, etc).


## App Functionality
- Filter Locations 

Includes a text input field that filters the map markers and list items to locations matching the text input or selection.

- List View

A list-view of location names is provided which displays all locations by default, and displays the filtered subset of locations when a filter is applied.
Clicking a location on the list displays unique information about the location, and animates its associated map marker.

- Map and Markers

Map displays all location markers by default, and displays the filtered subset of location markers when a filter is applied.  
Clicking a marker displays unique information about a location in an infoWindow element.


## Usage
1. Open index.html on browser.
2. Input a location and click filter button, it can filter the map markers and list items.
3. Click a location on the list, it can display unique information about the location.
4. Click a map marker, it also can display infomaiton about the location.
5. Input a city and click wiki button, it can show city information list, and click to access wiki.