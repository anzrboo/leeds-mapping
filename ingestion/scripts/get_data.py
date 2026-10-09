import geopandas as gpd
import pandas as pd
import requests

base = "https://mapservices.leeds.gov.uk/arcgis/rest/services/Public/Boundary/FeatureServer/query"
page = 1000
params = {
    "where": "1=1",
    "outFields": "*",
    "outSR": 27700,
    "orderByFields": "OBJECTID",
    "resultRecordCount": page,
    "f": "geojson",
}

frames, offset = [], 0
while True:
    r = requests.get(base, params={**params, "resultOffset": offset}, timeout=60)
    r.raise_for_status()
    feats = r.json().get("features", [])
    if not feats:
        break
    frames.append(gpd.GeoDataFrame.from_features(feats))
    if len(feats) < page:
        break
    offset += len(feats)

gdf = pd.concat(frames, ignore_index=True).set_crs(27700)
print(len(gdf), gdf.total_bounds)