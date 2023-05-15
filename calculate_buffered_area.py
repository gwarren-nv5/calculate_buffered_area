#calculate_buffered_area.py
# Created by G. Warren 5.15.23

import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

def calculate_polygon_area(shapefile, units="square miles"):
    # Read the shapefile
    gdf = gpd.read_file(shapefile)

    # Check if the input geometry is a polygon or multipolygon
    if not all(isinstance(geom, (Polygon, MultiPolygon)) for geom in gdf.geometry):
        raise ValueError("The input shapefile must only contain Polygon or MultiPolygon geometries")

    # Transform the geometries to an equal area projection (EPSG:6933)
    gdf = gdf.to_crs("EPSG:6933")

    # Calculate the area of the polygons (in square meters)
    gdf["area"] = gdf["geometry"].area

    # Convert the area -- default to sq miles
    if units == "square miles":
        gdf["area"] = gdf["area"] * 3.86102e-7
    elif units == "square kilometers":
        gdf["area"] = gdf["area"] * 1e-6
    elif units == "square meters":
        pass
    elif units == "square feet":
        gdf["area"] = gdf["area"] * 10.7639
    elif units == "acres":
        gdf["area"] = gdf["area"] * 0.000247105
    else:
        raise ValueError("The units must be one of the following: square miles, square kilometers, square meters, square feet, or acres")

    # Sum and return the total area, rounded to 3 digits
    total_area = gdf["area"].sum()
    return round(total_area, 3)
    return units
