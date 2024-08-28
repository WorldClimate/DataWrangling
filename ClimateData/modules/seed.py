import orchestrator as orc

data = {
    "locations":[
    {
        "city_name": "New York",
        "country": "United States",
    },{
        "city_name": "Jakarta",
        "country": "Indonesia",
    },{
        "city_name": "Oxford",
        "country": "England",
    },{
        "city_name": "Mumbai",
        "country": "India",
    },
    {
        "city_name": "San Francisco",
        "country": "United States",
    },
    {
        "city_name": "Lagos",
        "country": "Nigeria",
    }],
#    "query_types":["num_days_above_80", "num_days_above_90", "num_days_above_100", "precip", "tempmax", "tempmin"]
    # "locations":[
    # {
    #     "city_name": "New York",
    #     "country": "United States",
    # }],
    "query_types":["dew"]
}

for location in data["locations"]:
    print(location["city_name"])
    # print(f"Processing data for {location.city_name}")
    for query_type in data["query_types"]:
        print(f"Processing data for {query_type}")
        orc.orchestrate(location, query_type, 10)