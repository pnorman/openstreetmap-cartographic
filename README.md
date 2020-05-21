# OpenStreetMap Cartographic

## What is it?

A port of OpenStreetMap Carto targeting client-side rendering with vector tiles.

## How is it different from previous work?

Previous work has [used tilelive](rory) which is a technical dead-end, used existing vector tile sets which didn't have the richness of OpenStreetMap Data that OpenStreetMap Carto shows, or has not been intended to be a continuation of the OpenStreetMap Carto project.

## What do I need to run it?

- PostgreSQL 9.6 + PostGIS. PostGIS 3.0 is **strongly** recommended.
- OpenStreetMap data loaded in a database according to the [standard OpenStreetMap Carto](https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#openstreetmap-data) instructions.
- Python 3 and Tilekiln 0.0.4 or later

Install Tilekiln with
```sh
python3 -m venv venv
source venv/bin/activate
pip install tilekiln
```

## How do I get some vector tiles?

Install Tilekiln. Generate tiles with ``tilekiln-generate area -d gis vector.yaml tiles/``.

You can't generate for just a bounding box until [it is implemented in tilekiln](https://github.com/pnorman/tilekiln/issues/8) so it helps to have database CPU to throw at this.

Make a TileJSON with information about the tiles with ``tilekiln-tilejson vector.yaml "http://localhost:8000/tiles/{id}/{z}/{x}/{y}.mvt" > tiles/dev.json``

Serve up the tiles with ``./serve`` and you'll get a tilejson at ``http://localhost:8000/tiles/dev.json`` and the stylesheet at ``http://localhost:8000/openstreetmap-cartographic.json``. Load the stylesheet into something like [Fresco](https://fresco.gospatial.org/) for a better editing experience.

If you get fancy and aren't loading tiles from localhost, make sure to set your CORS headers and update the URLs.

## Why pre-generate vector tiles?

We're targeting deploying on the scale of tile.openstreetmap.org and pre-generation makes sense there. It's also way easier operationally.

## Legal

The code and cartography is licensed under CC0 as described in [LICENSE.txt](LICENSE.txt).

OpenStreetMap is a trademark of the OpenStreetMap Foundation, and is used with their permission. This project is not endorsed by or affiliated with the OpenStreetMap Foundation.
