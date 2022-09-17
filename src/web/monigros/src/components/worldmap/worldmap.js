// Uses the Leaflet library to display a map of the world
// https://react-leaflet.js.org/

import React, { Component }  from 'react';
import {MapContainer, TileLayer, Marker, Popup, GeoJSON} from 'react-leaflet';
import { DivIcon } from 'leaflet';

import COUNTRIES from "./countries";
import disruption from "./disruption.png";

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
        {
          "position": COUNTRIES["germany"],
          "info": "Shortage of beer in vision of the oktoberfest coming-up soon"
        },
    ]};

    this.addInfo = this.addInfo.bind(this);
  }

  addInfo(country, info) {
    this.setState({
      infos: this.state.infos.concat({
        "position": COUNTRIES[country],
        "info": info
      })
    });
  }

  render() {
    const disruption_marker = new DivIcon({
      className: 'disruption-marker',
      html: `<img src="${disruption}"/>`,
      iconSize: [20, 20],
      iconAnchor: [10, 10]
    });

    let markers = [];
    let line_coords = [];
    for (let i = 0; i < this.state.infos.length; i++) {
      const pos = this.state.infos[i].position;
      const info = this.state.infos[i].info;

      if (i > 0) {
        markers.push(
          <Marker position={pos} key={pos} icon={disruption_marker} >
            <Popup>
              {info}
            </Popup>
          </Marker>
          );

        line_coords.push([
          [pos[1], pos[0]],
          [COUNTRIES["switzerland"][1], COUNTRIES["switzerland"][0]]
        ]);
      } else {
        markers.push(
          <Marker position={pos} key={pos}>
            <Popup>
              {info}
            </Popup>
          </Marker>
          );
      }
    }

    const lines_data = {
      "type": "Feature",
      "geometry": {
          "type": "Polygon",
          "coordinates": line_coords
      }
    }


    return (
      <MapContainer className='mapcontainer' center={COUNTRIES["switzerland"]} zoom={4} scrollWheelZoom={true} style={mapstyle}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <GeoJSON key={1} data={lines_data} style={()=>({color: "#ff0000"})}/>
        {markers}

      </MapContainer>
    );
  }
}


export default WorldMap;
