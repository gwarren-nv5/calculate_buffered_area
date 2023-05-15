#calculate_buffered_area.py
# Created by G. Warren 5.15.23

import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon

def calculate_polygon_area(shapefile):
    # Read the shapefile
    gdf = gpd.read_file(shapefile)

    # Check if the input geometry is a polygon or multipolygon
    if not all(isinstance(geom, (Polygon, MultiPolygon)) for geom in gdf.geometry):
        raise ValueError("The input shapefile must only contain Polygon or MultiPolygon geometries")

    # Transform the geometries to an equal area projection (EPSG:6933)
    gdf = gdf.to_crs("EPSG:6933")

    # Calculate the area of the polygons (in square meters)
    gdf["area"] = gdf["geometry"].area

    # Convert the area to square miles (1 square meter = 3.86102e-7 square miles)
    gdf["area"] = gdf["area"] * 3.86102e-7

    # Sum and return the total area, rounded to 3 digits
    total_area = gdf["area"].sum()
    return round(total_area, 3)