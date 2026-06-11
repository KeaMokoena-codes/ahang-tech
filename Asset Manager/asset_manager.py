equipments = [{"tool": "Air_compressor", "id": 111, "status": "Available", "assigned_to": None}, 
             {"tool": "Plate_compactor","id": 112, "status": "Available", "assigned_to": None}, 
             {"tool": "Concrete_mixer", "id": 113, "status": "Available", "assigned_to": None}]         

def list_assets():
    print("\n--- Current Site Assets ---")
    for tools in equipments:
        print(f"Tool: {tools["tool"]}, ID: {tools["id"]}, Status: {tools["status"]}.")

# list_assets()

def asset_checkout(asset_id, worker_name):
    for item in equipments:
        if item["id"] == asset_id:
            if item["status"] == "Available":
                item["status"] = "Checked Out"
                item["assigned_to"] = worker_name
                print(f"The {item["tool"]} has been successfully assigned to {item["assigned_to"]}.")
                return
            else:
                print(f"There was an error assigning the {item["tool"]}. Current status: {item['tool']}, Status: {item['status']}, Assigned To: {item['assigned_to']}. If all fields are correct, kindly verify the Asset ID.")

# asset_checkout(111, "Keamogetswe")                     

# def list_assets():
#     """Prints all assets currently in the system."""
#     print("\n--- Current Site Assets ---")
#     for item in inventory:
#         print(f"ID: {item['id']} | {item['name']} | Status: {item['status']} | Assigned To: {item['assigned_to']}")
#     print("---------------------------\n")