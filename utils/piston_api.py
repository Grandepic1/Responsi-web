import requests


def run_java_code(code: str) -> str | None:
    """Execute Java code using Piston API and return its output."""
    url = "https://emkc.org/api/v2/piston/execute"
    payload = {
        "language": "java",
        "version": "15.0.2",
        "files": [{"name": "Main.java", "content": code}],
    }

    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        data = res.json()
        return data.get("run", {}).get("output", "")
    except Exception as e:
        print("Error:", e)
        return None
