
if (!$) {
  var $ = jQuery = django.jQuery;
}

$(function() {

  var options = {
    map: "#map_location",
    mapOptions: { zoom: 10 },
    markerOptions: { draggable: true },
    types: ["geocode", "establishment"],
  },
  geocomplete = $("#id_place");

  if ( $('#id_location').val() ) {
    options.location = $('#id_location').val()
  }

  geocomplete
    .geocomplete(options)
    .bind("geocode:result", function(event, result) {
      $('#id_location').val(result.geometry.location.lat() + ',' + result.geometry.location.lng());
    })
    .bind("geocode:error", function(event, status){
      console.log("ERROR: " + status);
    })
    .bind("geocode:multiple", function(event, results){
      console.log("Multiple: " + results.length + " results found");
    })
    .bind("geocode:dragged", function(event, latLng){
      $('#id_location').val(latLng.lat() + ',' + latLng.lng());
    });

});
