# 🔑 Supabase License Key Generator & Lifecycle Manager

A secure, cryptographically sound Python utility designed to generate case-sensitive 16-character license keys and automatically manage key lifecycles using **Supabase** as the remote cloud backend. This component handles the administrative side of a subscription ecosystem by generating new keys and sweeping away stale, expired data.

---

## 🎯 Key Use Cases

This module serves as an administrative control layer or backend script for:
* **🎫 License Code Generation:** Instantly minting unique, secure activation tokens to distribute to clients, customers, or storefront platforms.
* **🧹 Database Maintenance & Housekeeping:** Automatically cleaning out obsolete, expired subscription rows associated with a specific machine before issuing a replacement.
* **🛡️ Secure Serial Dispensing:** Leveraging cryptographically secure pseudo-random number generation (CSPRNG) to guarantee generated strings cannot be systematically guessed or predicted.

---

## ✨ Features

* 🎲 **Cryptographically Secure:** Utilizes Python's `secrets` module instead of standard `random` to ensure tokens are completely safe for high-security subscription validation.
* 🗑️ **Automated Overwrite Sweeper:** Scans for existing keys bound to the given Hardware ID (HWID); if they are flagged as `Expired`, they are automatically deleted to clear up database storage.
* 🛑 **Safety Constraints:** Protects active subscriptions by leaving keys marked as `Activated` or `Unused` completely untouched during the cleanup phase.
* ☁️ **Direct Cloud Synchronization:** Inserts raw structured datasets immediately into a Supabase cloud database, rendering them available for client applications instantly.

---

## 🛠️ Requirements & Dependencies

Install the official Supabase runtime engine through `pip`:

```bash
pip install supabase

```

---

## 🗄️ Database Table Compatibility

This management script writes directly to a **`keys_table`** table within Supabase. The table column types should mirror the following configuration:

| Column Name | Data Type | Constraint Layer |
| --- | --- | --- |
| `name` | `text` | User or client identification label |
| `code` | `text` | Primary / Unique indexing key (16 characters) |
| `hwid` | `text` | Target hardware device signature identifier |
| `status` | `text` | Initial state default assigned as `"Unused"` |

---

## 🚀 How to Run

1. Open the script and modify the credentials block with your live project parameters:
```python
SUPABASE_URL = "YOUR_LIVE_SUPABASE_PROJECT_URL"
SUPABASE_KEY = "YOUR_LIVE_SUPABASE_ANON_OR_SERVICE_KEY"

```


2. Execute the administrative utility inside your workstation shell:
```bash
python main.py

```


3. Choose option `1`, pass in a user profile name, provide a device HWID signature, and the script will automatically register the new token in your cloud dashboard.

```

```