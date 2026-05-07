$extens("include.py")
include("import requests", ["extella-pip install requests"])

def connector_github_healthcheck(connector_github_pat: str = "") -> dict:
    """Проверяет GitHub PAT через GET /user."""
    base = {"status": "error", "connector_id": "github", "message": "", "provider_http_status": None, "login": None}
    token = (connector_github_pat or "").strip()
    if not token:
        base["message"] = "connector_github_pat required"
        return base
    try:
        r = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=30,
        )
        base["provider_http_status"] = r.status_code
        if r.status_code != 200:
            base["message"] = f"HTTP {r.status_code}: {r.text[:200]}"
            return base
        data = r.json()
        login = data.get("login")
        return {
            "status": "success",
            "connector_id": "github",
            "message": "",
            "provider_http_status": r.status_code,
            "login": login,
        }
    except Exception as e:
        base["message"] = str(e)
        return base
