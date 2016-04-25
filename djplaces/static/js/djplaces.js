
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
        //details: "#id_location"
      })
      .bind("geocode:result", function(event, result){
        console.log("Result: " + result.formatted_address + result.lat + ',' + result.lng);
      })
      .bind("geocode:error", function(event, status){
        console.log("ERROR: " + status);
      })
      .bind("geocode:multiple", function(event, results){
        console.log("Multiple: " + results.length + " results found");
      });
  });

