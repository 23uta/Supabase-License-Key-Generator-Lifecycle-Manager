import string
import secrets
from supabase import create_client, Client

# 1. Connect the application to the cloud server (replace with your own project credentials)
SUPABASE_URL = "YOUR_URL"
SUPABASE_KEY = "YOUR_KEY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# Function to generate a 16-character alphanumeric key (case-sensitive)
def generate_16_digit_code():
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(16))


# --- [Delete any old expired keys associated with this device] ---
def delete_expired_key_for_hwid(hwid):
    """
    Searches for any keys tied to the same hwid. If the status is "Expired",
    it deletes it from the database so it can be replaced with a fresh key.
    Returns True if any key was deleted.
    """
    try:
        response = supabase.table("keys_table").select("*").eq("hwid", hwid).execute()
        records = response.data

        if not records:
            return False

        deleted_any = False
        for record in records:
            if record.get("status") == "Expired":
                supabase.table("keys_table").delete().eq("code", record["code"]).execute()
                print(f"🗑  Old expired key deleted (code: {record['code']})")
                deleted_any = True
            else:
                print(f"⚠️  Found an existing key for this device with status "
                      f"'{record.get('status')}' — left untouched (only 'Expired' keys are auto-deleted).")

        return deleted_any

    except Exception as e:
        print(f"An error occurred while checking old keys: {e}")
        return False


# --- [Function 1: Create a key and upload it to the server] ---
def create_and_upload_key(name, hwid):
    # First: If there is an old expired key for the same device, delete it
    delete_expired_key_for_hwid(hwid)

    generated_code = generate_16_digit_code()

    # Insert a new row into the cloud server table
    data = {
        "name": name,
        "hwid": hwid,
        "code": generated_code,
        "status": "Unused"  # Set automatically as unused
    }

    try:
        supabase.table("keys_table").insert(data).execute()
        print(f"your code was generated ...")
        print(f"name: {name} | code: {generated_code} | status: Unused\n")
    except Exception as e:
        print(f"An error occured : {e}")


if __name__ == "__main__":
    print("1.[generate a new key] \n 2.[exit]")
    x = input(">>>").strip()
    if x == "1":
        name = input("enter your name : ")
        hwid = input("enter your device id : ")  # In the final version, the code gets the hwid automatically
        create_and_upload_key(name, hwid)
    elif x == "2":
        input("press [enter] to exit")
    else:
        print("invalid input , please choose 1 or 2")