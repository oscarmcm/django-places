var dj = jQuery.noConflict();

dj(function() {
  setTimeout(function() {
  var mapElement = dj("#map_location");
  var mapInput = dj("[data-id='map_place']");
  var options = {
    map: mapElement,
    mapOptions: dj(".places-widget").data("mapOptions") ? dj(".places-widget").data("mapOptions") : { zoom: 10 },
    markerOptions: dj(".places-widget").data("markerOptions") ? dj(".places-widget").data("markerOptions") : { draggable: true },
    types: ["geocode", "establishment"],
    location: mapInput && mapInput.val().length > 0 ? [dj("[data-id='map_latitude']").val(), dj("[data-id='map_longitude']").val()] : false,
  },
  geocomplete = mapInput;

  geocomplete
    .geocomplete(options)
    .bind("geocode:result", function(event, result) {
      dj("[data-id='map_latitude']").val(result.geometry.location.lat());
      dj("[data-id='map_longitude']").val(result.geometry.location.lng());
    })
    .bind("geocode:error", function(event, status){
      console.log("ERROR: " + status);
    })
    .bind("geocode:multiple", function(event, results){
      console.log("Multiple: " + results.length + " results found");
    })
    .bind("geocode:dragged", function(event, latLng){
      dj("[data-id='map_latitude']").val(latLng.lat());
      dj("[data-id='map_longitude']").val(latLng.lng());
    });

  },500)

});
