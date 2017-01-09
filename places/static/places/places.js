var dj = jQuery.noConflict();

dj(function() {
  var mapElement = dj("#map_location");
  var mapInput = dj("#map_place input");
  var options = {
    map: mapElement,
    mapOptions: dj(".places-widget").data("mapOptions") ? dj(".places-widget").data("mapOptions") : { zoom: 10 },
    markerOptions: dj(".places-widget").data("markerOptions") ? dj(".places-widget").data("markerOptions") : { draggable: true },
    types: ["geocode", "establishment"],
    location: mapInput.val().length > 0 ? [dj("#map_latitude input").val(), dj("#map_longitude input").val()] : false,
  },
  geocomplete = mapInput;

  geocomplete
    .geocomplete(options)
    .bind("geocode:result", function(event, result) {
      dj("#map_latitude input").val(result.geometry.location.lat());
      dj("#map_longitude input").val(result.geometry.location.lng());
    })
    .bind("geocode:error", function(event, status){
      console.log("ERROR: " + status);
    })
    .bind("geocode:multiple", function(event, results){
      console.log("Multiple: " + results.length + " results found");
    })
    .bind("geocode:dragged", function(event, latLng){
      dj("#map_latitude input").val(latLng.lat());
      dj("#map_longitude input").val(latLng.lng());
    });

});
