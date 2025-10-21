import requests

PISTON_URL = "https://emkc.org/api/v2/piston/execute"


def run_java_code(code, stdin_data=""):
    payload = {
        "language": "java",
        "version": "15.0.2",  # ✅ required by emkc.org version
        "files": [{"name": "Main.java", "content": code}],
        "stdin": stdin_data,  # ✅ required even if empty
    }

    try:
        res = requests.post(PISTON_URL, json=payload, timeout=10)
        res.raise_for_status()
        result = res.json()
        return result.get("run", {}).get("output", "")
    except Exception as e:
        return f"[Error] {e}"
