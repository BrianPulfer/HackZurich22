// Uses the Leaflet library to display a map of the world
// https://react-leaflet.js.org/

import React, { Component }  from 'react';
import {MapContainer, TileLayer, Marker, Popup} from 'react-leaflet';

import COUNTRIES from "./countries";

const mapstyle = { 
  "height":  window.innerHeight + "px"
};

class WorldMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      infos: [
        {
          "position": COUNTRIES["switzerland"],
          "info": "This is where products are shipped"
        },
    ]};
  }

  render() {
    let markers = [];
    for (let i = 0; i < this.state.infos.length; i++) {
      const pos = this.state.infos[i].position;
      const info = this.state.infos[i].info;

      markers.push(
      <Marker position={pos} key={pos}>
        <Popup>
          {info}
        </Popup>
      </Marker>
      );
    }

    return (
      <MapContainer className='mapcontainer' center={COUNTRIES["switzerland"]} zoom={4} scrollWheelZoom={true} style={mapstyle}>
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
