import requests

BASE = "http://127.0.0.1:8000"


def show_response(label, r):
    print(f"\n--- {label} ---")
    print("Status:", r.status_code)

    # Always print raw text first (helps debug)
    print("Raw response:")
    print(r.text)

    # Try to parse JSON if possible
    try:
        print("JSON:")
        print(r.json())
    except Exception:
        print("(Response is not valid JSON)")


def main():
    print("=== Pokemon ETB Tracker Console Client ===")

    # ---------------- CREATE ----------------
    create_payload = {
        "user_id": 1,
        "set_id": 1,
        "item_name": "Client Test ETB",
        "sealed": True
    }

    r = requests.post(f"{BASE}/items", json=create_payload)
    show_response("CREATE", r)

    if r.status_code != 200:
        print("Create failed — stopping test.")
        return

    item_id = r.json().get("item_id")

    # ---------------- GET ----------------
    r = requests.get(f"{BASE}/items/{item_id}")
    show_response("GET", r)

    # ---------------- UPDATE ----------------
    update_payload = {
        "user_id": 1,
        "set_id": 2,
        "item_name": "Updated Client Test ETB",
        "sealed": False
    }

    r = requests.put(f"{BASE}/items/{item_id}", json=update_payload)
    show_response("UPDATE", r)

    # ---------------- GET AGAIN ----------------
    r = requests.get(f"{BASE}/items/{item_id}")
    show_response("GET AFTER UPDATE", r)

    # ---------------- DELETE ----------------
    r = requests.delete(f"{BASE}/items/{item_id}")
    show_response("DELETE", r)

    # ---------------- GET AFTER DELETE ----------------
    r = requests.get(f"{BASE}/items/{item_id}")
    show_response("GET AFTER DELETE", r)


if __name__ == "__main__":
    main()