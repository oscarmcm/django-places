function initDjangoPlaces() {
  var input = document.getElementById('id_location_0');
  var marker = null;
  var mapLocation = { lat: 38.971584, lng: -95.235072 };
  var searchBox = new google.maps.places.SearchBox(input);
  var latInput = document.getElementById('id_location_1');
  var lngInput = document.getElementById('id_location_2');

  var gmap = new google.maps.Map(
    document.getElementById('map_location'),
    {center: mapLocation, zoom: 10}
  );

  if (latInput.value && lngInput.value) {
    var location = {
      lat: parseFloat(latInput.value),
      lng: parseFloat(lngInput.value)
    }
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
      }
      if (marker) {
        marker.setMap(null)
      };
      marker = new google.maps.Marker({position: place.geometry.location, map: gmap});
      document.getElementById('id_location_1').value = place.geometry.location.lat();
      document.getElementById('id_location_2').value = place.geometry.location.lng();
      gmap.setCenter(place.geometry.location);
      gmap.setZoom(16);
    });
  });
}

google.maps.event.addDomListener(window, 'load', initDjangoPlaces);
