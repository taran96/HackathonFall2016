$.getJSON(room, function(json1) {
    $.each(json1, function(key, data) {
        var latLng = new google.maps.LatLng(data.lat, data.lng); 
        // Creating a marker and putting it on the map
        var marker = new google.maps.Marker({
            position: latLng,
            map: map,
            title: data.title
        });
    });
});