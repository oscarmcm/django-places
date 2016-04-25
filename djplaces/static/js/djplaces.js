
  $(document).ready(function() {
    $("#id_place")
      .geocomplete({
        map: "#map_location",
        mapOptions: {
          zoom: 10
        },
        markerOptions: {
          draggable: true
        }
      })
      .bind("geocode:result", function(event, result) {
        var coordinates = result.geometry.location.lat() + ',' + result.geometry.location.lng();
        $('#id_location').val(coordinates);
      })
      .bind("geocode:error", function(event, status){
        console.log("ERROR: " + status);
      })
      .bind("geocode:multiple", function(event, results){
        console.log("Multiple: " + results.length + " results found");
      });
  });

