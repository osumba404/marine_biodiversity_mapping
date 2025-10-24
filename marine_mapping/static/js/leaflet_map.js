(function(){
  const map = L.map('map').setView([-4.5, 39.5], 7);
  const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // Reefs layer
  fetch('/api/reefs/?format=geojson')
    .then(res => res.json())
    .then(data => {
      const reefStyle = {
        color: '#1f78b4',
        weight: 1,
        fillOpacity: 0.4
      };
      const reefs = L.geoJSON(data, {
        style: reefStyle,
        onEachFeature: function (feature, layer) {
          const p = feature.properties || {};
          layer.bindPopup(`<strong>${p.name || 'Reef'}</strong><br/>Type: ${p.reef_type || 'N/A'}<br/>Condition: ${p.condition_score ?? 'N/A'}`);
        }
      });
      reefs.addTo(map);
    })
    .catch(() => {});

  // Occurrences layer (verified only)
  fetch('/api/occurrences/?format=geojson')
    .then(res => res.json())
    .then(data => {
      const occurrences = L.geoJSON(data, {
        pointToLayer: (feature, latlng) => L.circleMarker(latlng, {
          radius: 5,
          color: '#e31a1c',
          fillColor: '#fb9a99',
          fillOpacity: 0.8,
          weight: 1
        }),
        onEachFeature: (feature, layer) => {
          const p = feature.properties || {};
          const img = p.photo_url ? `<br/><img src="${p.photo_url}" style="max-width:200px;display:block;"/>` : '';
          layer.bindPopup(`<strong>${p.species_name || 'Species'}</strong><br/>Observed: ${p.observed_at || 'N/A'}${img}`);
        }
      });
      occurrences.addTo(map);
    })
    .catch(() => {});
})();
