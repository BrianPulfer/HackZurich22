import React, { Component }  from 'react';
import {MapContainer, TileLayer, Marker, Popup} from 'react-leaflet';

const switzerland = [46.8182, 8.2275];
const mapstyle = { "height": "1080px"};

class WorldMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      infos: [
        {
          "position": switzerland,
          "info": "This is where products are shipped"
        }
    ]};
  }

  render() {
    let markers = [];
    for (let i = 0; i < this.state.infos.length; i++) {
      const pos = this.state.infos[i].position;
      const info = this.state.infos[i].info;

      markers.push(
      <Marker position={pos}>
        <Popup>
          {info}
        </Popup>
      </Marker>
      );
    }

    return (
      <MapContainer className='mapcontainer' center={switzerland} zoom={4} scrollWheelZoom={true} style={mapstyle}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {markers}
      </MapContainer>
    );
  }
}

export default WorldMap;
