import json


def reset_temp_data():
    try:
        with open("temp_data.json", "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)
    except Exception as e:
        print(f"Error: {e}")
