function setupDjangoPlaces(mapConfig, markerConfig, childs) {
  var searchBox = new google.maps.places.SearchBox(childs[0]);
  var latInput = childs[1];
  var lngInput = childs[2];
  var nameInput = childs[3];
  var addressInput = childs[4];
  var countryInput = childs[5];
  var cityInput = childs[6];  
  var stateInput = childs[7];
  var gmap = new google.maps.Map(childs[8], mapConfig);

  var marker = new google.maps.Marker(markerConfig);

  if (latInput.value && lngInput.value) {
    var location = {
      lat: parseFloat(latInput.value),
      lng: parseFloat(lngInput.value)
    };
    marker.setPosition(location);
    marker.setMap(gmap);
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
      marker.setPosition(place.geometry.location);
      marker.setMap(gmap);
      console.log('place', place)


      let country 
      let city
      let state

      place.address_components.forEach(function(component) {
        if (component.types.includes("country")) {
          country = component.long_name;
        }
        if (component.types.includes("locality") || component.types.includes("postal_town")) {
          city = component.long_name;
        }
        if (component.types.includes("administrative_area_level_1")) {
          state = component.long_name;
        }
      });

      nameInput.value = place.name;
      addressInput.value = place.formatted_address;
      countryInput.value = country;
      cityInput.value = city;
      stateInput.value = state;
      latInput.value = place.geometry.location.lat();
      lngInput.value = place.geometry.location.lng();
      gmap.setCenter(place.geometry.location);
      gmap.setZoom(16);
    });
  });

  google.maps.event.addListener(marker, 'dragend', function (event) {
    latInput.value = event.latLng.lat();
    lngInput.value = event.latLng.lng();
  });
}

function initDjangoPlaces() {
  var widgets = document.getElementsByClassName('places-widget');
  for (var iter = 0; iter < widgets.length; iter++) {
    setupDjangoPlaces(
      JSON.parse(widgets[iter].dataset.mapOptions),
      JSON.parse(widgets[iter].dataset.markerOptions),
      widgets[iter].children
    );
  };
};

google.maps.event.addDomListener(window, 'load', initDjangoPlaces);
