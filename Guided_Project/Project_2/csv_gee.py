import arcpy
import ee
import pandas as pd
import geopandas

def get_elevation_from_gee(csv_file= r"C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\boundary.csv",
                           shapefile =r'C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\boundary.shp',
                            factoryCode = 32119):
    
    #earth engine image access
    ee.Authenticate()
    ee.Initialize(project='vegetation--sav')
    dem = ee.Image('USGS/3DEP/10m')

    #read from the csv file
    
    table = pd.read_csv(csv_file)
   

    #create a shapefile from the csv file
    gdf = geopandas.GeoDataFrame(table)
    gdf.set_geometry(
        geopandas.points_from_xy(gdf['X'], gdf['Y']),
        inplace=True, crs=f'EPSG:{factoryCode}')

    
    gdf.to_file(shapefile)

    #add field to the shapefile
    arcpy.management.AddField(shapefile,'elevation',"FLOAT")
    print("reading from GEE for elevation values...")

    #read elevation fro gee and write values to the shapefile
    geom_list = []
    with arcpy.da.SearchCursor(shapefile,['SHAPE@XY','elevation'],spatial_reference=4326) as cursor:
        for row in cursor:
            X,Y =row[0]
            geom = ee.Geometry.Point([X,Y])
            geom_list.append(geom)
    geom_col = ee.FeatureCollection(geom_list)
    elev = dem.sampleRegions(geom_col).getInfo().get('features')
    i=0
    with arcpy.da.UpdateCursor(shapefile, ['elevation']) as cursor:
        for row in cursor:       
            elevation = elev[i]['properties']['elevation']
            row[0]=elevation 
            cursor.updateRow(row)
            i +=1
        
if __name__ == "__main__":
    import sys
    if len(sys.argv)>3:
        
        csv_file = sys.argv[1]
        shapefile = sys.argv[2]
        factoryCode = int(sys.argv[3])
        
    else:
        csv_file = r"C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\boundary.csv"
        shapefile =r"C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\boundary.shp"
        factoryCode = 32119     
    get_elevation_from_gee(csv_file, shapefile, factoryCode)
    print("Elevation values added to the shapefile.")