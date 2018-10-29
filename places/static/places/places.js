function setupDjangoPlaces(mapConfig, childs) {
  var marker = null;
  var searchBox = new google.maps.places.SearchBox(childs[0]);
  var latInput = childs[1];
  var lngInput = childs[2];
  var gmap = new google.maps.Map(childs[3], mapConfig);

  if (latInput.value && lngInput.value) {
    var location = {
      lat: parseFloat(latInput.value),
      lng: parseFloat(lngInput.value)
    };
    marker = new google.maps.Marker({position: location, map: gmap});
    gmap.setCenter(location);
    gmap.setZoom(16);
  };

  searchBox.addListener('places_changed', function () {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    places.forEach(function (place) {
      if (!place.geometry) {
        console.log('Returned place contains no geometry');
        return;
      };
      if (marker) {
        marker.setMap(null);
      };
      marker = new google.maps.Marker({position: place.geometry.location, map: gmap});
      latInput.value = place.geometry.location.lat();
      lngInput.value = place.geometry.location.lng();
      gmap.setCenter(place.geometry.location);
      gmap.setZoom(16);
    });
  });
}

function initDjangoPlaces() {
  var widgets = document.getElementsByClassName('places-widget');
  for (var iter = 0; iter < widgets.length; iter++) {
    setupDjangoPlaces(
      JSON.parse(widgets[iter].dataset.mapOptions),
      widgets[iter].children
    );
  };
};

google.maps.event.addDomListener(window, 'load', initDjangoPlaces);
