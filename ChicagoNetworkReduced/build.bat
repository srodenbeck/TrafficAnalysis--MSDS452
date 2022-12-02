#!/bin/bash
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml.gz --fringe-factor 1 --insertion-density 1 -o osm.passenger.trips.xml -r osm.passenger.rou.xml -e 600 --trip-attributes "departLane=\"best\"" --fringe-start-attributes "departSpeed=\"max\"" --validate --remove-loops --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --min-distance.fringe 10 --allow-fringe.min-length 1000 --lanes
