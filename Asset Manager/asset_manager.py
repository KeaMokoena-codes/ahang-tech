equipments = [{"tool": "air_compressor", "id": 111, "status": "Available"}, 
             {"tool": "plate_compactor","id": 112, "status": "Available"}, 
             {"tool": "concrete_mixer", "id": 113, "status": "Available"}]         

def list_assets():
    print("\n--- Current Site Assets ---")
    for tools in equipments:
        print(f"Tool: {tools["tool"]}, ID: {tools["id"]}, Status: {tools["status"]}")

list_assets()

# def list_assets():
#     """Prints all assets currently in the system."""
#     print("\n--- Current Site Assets ---")
#     for item in inventory:
#         print(f"ID: {item['id']} | {item['name']} | Status: {item['status']} | Assigned To: {item['assigned_to']}")
#     print("---------------------------\n")