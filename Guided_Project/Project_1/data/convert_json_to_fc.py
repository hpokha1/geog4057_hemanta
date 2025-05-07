import json
import arcpy
import os

def jsonToFC(input_file, output_file):
    with open(input_file, 'r') as file:
        tax_json = json.load(file)

    workspace = os.path.dirname(output_file)
    fcname = os.path.basename(output_file)
    
    if arcpy.Exists(output_file):
        arcpy.management.Delete(output_file)

    arcpy.management.CreateFeatureclass(out_path=workspace, out_name=fcname,
                                        geometry_type='POLYGON',
                                        spatial_reference=4269)  # 4269 is the EPSG code for NAD83

    fields = tax_json['meta']['view']['columns']
    field_names = []
    for ind, field in enumerate(fields):
        name = field['fieldName']
        if name == 'the_geom':
            continue
        if ':' in name:
            name = name.split(':')[1]
        if name.lower() == 'id':
            name = 'id2'
        if len(name) > 10:
            name = name[:10]
        field_names.append(name)

    field_type = ['TEXT', 'TEXT', 'LONG', 'LONG', 'TEXT', 'LONG', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT']
    for ind, field_name in enumerate(field_names):
        arcpy.management.AddField(output_file,
                                  field_name=field_name,
                                  field_type=field_type[ind])

    field_names.append('SHAPE@')

    with arcpy.da.InsertCursor(output_file, field_names=field_names) as cursor:
        for row in tax_json['data']:
            new_row = []
            for ind, value in enumerate(row):
                if ind == 8:
                    continue
                if value is None:
                    value = ""
                new_row.append(value)
            geom = arcpy.FromWKT(row[8])
            new_row.append(geom)
            cursor.insertRow(new_row)

def main():
    input_file = r'C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\no_tax.json'
    output_file = r'C:\Users\hpokha1\OneDrive - Louisiana State University\Documents\GitHub\geog4057\project\data\notax_fc.shp'
    jsonToFC(input_file, output_file)

if __name__ == "__main__":
    main()