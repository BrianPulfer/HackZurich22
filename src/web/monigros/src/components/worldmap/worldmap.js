// Uses the Leaflet library to display a map of the world
// https://react-leaflet.js.org/

import React, { Component }  from 'react';
import {MapContainer, TileLayer, Marker, Popup, GeoJSON} from 'react-leaflet';
import { DivIcon } from 'leaflet';

import COUNTRIES from "./countries";
import disruption from "./disruption.png";
import DBPath from './../../DB/DB_files/table_process_url.json';

const mapstyle = { 
  "height":  window.innerHeight + "px"
};

class WorldMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      infos: {
        "Original": {
          "position": COUNTRIES["switzerland"],
          "info": "This is where products are shipped"
        },
    }};

    this.addInfo = this.addInfo.bind(this);
    this.readJson = this.readJson.bind(this);
  }

  addInfo(country, info, url, id, kind) {
    let infonew = this.state.infos
    infonew[id] = {
      "position": COUNTRIES[country],
      "info": info,
      "url": url,
      "kind": kind
    }
    this.setState({
      infos: infonew
    })};

  readJson(){
    for (let i = 0; i < DBPath.length; i++) {
          this.addInfo(
            DBPath[i]["Country"],
            DBPath[i]["resume"],
            DBPath[i]["url"],
            DBPath[i]["process_ID"],
            DBPath[i]["labels"][0][0]
          )
    }
  }

  componentDidMount() {
    this.interval = setInterval(() => this.readJson(), 1000);
  }
  componentWillUnmount() {
    clearInterval(this.interval);
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
    //for (let i = 0; i < this.state.infos.length; i++) {
    let i = 0;
    for (var key in this.state.infos) {
      
      const pos = this.state.infos[key].position;
      const info = this.state.infos[key].info;
      const url = this.state.infos[key].url;
      const kind = this.state.infos[key].kind;
      
      if (i > 0) {
        markers.push(
          <Marker position={pos} key={pos} icon={disruption_marker} >
            <Popup>
            <b>"WARNING:"</b> <i>{kind}</i> <br/>
            {info}
            <br/><br/>
            <a href={url}>source</a>
            </Popup>
          </Marker>
          );

        line_coords.push([
          [COUNTRIES["switzerland"][1], COUNTRIES["switzerland"][0]],
          [pos[1], pos[0]]
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
      i++;
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
