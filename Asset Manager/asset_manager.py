equipments = { 
    "tool" : {"name": "air_compressor", 
               "id": 111, 
               "status": "Available"},
    "tool" : {"name": "plate_compactor",
               "id": 112,
               "status": "Available"},
    "tool" : {"name": "concrete_mixer",
               "id": 113,
               "status": "Available"},         
}

for key, dict2 in equipments.items():        
    equipments["tool"]["status"] = "Changed"
    print(f"Tool: {key}, Description: {dict2}")