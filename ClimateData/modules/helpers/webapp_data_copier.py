import shutil

def copy(location, combined_output_location, query_type):
        # Copy the processed data to the web app
    hyphenated_city = location['city_name'].replace(' ', '-').lower()
    source_file = open(combined_output_location+'.json', 'rb')
    destination_file = open('../../../Climate Platform/ClimatePlatform/data/'+hyphenated_city+'/combined_'+query_type+'.json', 'wb')
    shutil.copyfileobj(source_file, destination_file)
    print('Data copied to web app')
    return True