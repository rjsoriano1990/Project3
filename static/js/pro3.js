function createMap(USinflation) {

    // Create the tile layer that will be the background of our map.
    var USmap = L.tileLayer('https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Petroleum_Administration_for_Defense_Districts.svg/1200px-Petroleum_Administration_for_Defense_Districts.svg.png', {

        attribution: '&copy; <a href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPetroleum_Administration_for_Defense_Districts&psig=AOvVaw3Yjxbr2JsTXr5h8STKq2gr&ust=1638422846536000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCMjv3KLvwfQCFQAAAAAdAAAAABAD">OpenStreetMap</a> contributors'
    });



  
  
    // Create a baseMaps object to hold the streetmap layer.
    var baseMaps = {
      "US Map": USmap
    };
  
    // Create an overlayMaps object to hold the bikeStations layer.
    var overlayMaps = {
      "US States": USstates
    };
  
    // Create the map object with options.
    var map = L.map("map-id", {
      center: [37.0902, -95.7129],
      zoom: 12,
      layers: [USmap, UStates]
    });
  
    // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
  }
  
  function createMarkers(response) {
  
    // Pull the "stations" property from response.data.
    var states = response.data.states;
  
    // Initialize an array to hold state markers.
    var stateMarkers = [];
  
    // Loop through the stations array.
    for (var index = 0; index < states.length; index++) {
      var state = states[index];
  
      // For each station, create a marker, and bind a popup with the station's name.
      var stateMarker = L.marker([state.lat, state.lon])
        .bindPopup("<h3>" + state.name + "<h3><h3>'us_gas_price_region': " + state.price + "</h3>");
  
      // Add the marker to the bikeMarkers array.
      stateMarkers.push(stateMarker);
    }
  
    // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
    createMap(L.layerGroup(stateMarkers));
  }
  
  
  // Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
  d3.json("https://gbfs.citibikenyc.com/gbfs/en/station_information.json").then(createMarkers);
  