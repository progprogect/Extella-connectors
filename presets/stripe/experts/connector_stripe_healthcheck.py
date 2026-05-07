$extens("include.py")
include("import requests", ["extella-pip install requests"])

def connector_stripe_healthcheck(connector_stripe_secret_key: str = "") -> dict:
    """Проверяет Stripe secret key через GET /v1/balance."""
    base = {
        "status": "error",
        "connector_id": "stripe",
        "message": "",
        "provider_http_status": None,
        "livemode": None,
        "available_currencies": None,
    }
    key = (connector_stripe_secret_key or "").strip()
    if not key:
        base["message"] = "connector_stripe_secret_key required"
        return base
    try:
        r = requests.get(
            "https://api.stripe.com/v1/balance",
            auth=(key, ""),
            headers={"Stripe-Version": "2023-10-16"},
            timeout=30,
        )
        base["provider_http_status"] = r.status_code
        if r.status_code != 200:
            try:
                err = r.json().get("error", {})
                msg = err.get("message", r.text[:200])
            except Exception:
                msg = r.text[:200]
            base["message"] = f"HTTP {r.status_code}: {msg}"
            return base
        data = r.json()
        available = data.get("available") or []
        currencies = []
        for item in available:
            c = item.get("currency")
            if c and c not in currencies:
                currencies.append(c)
        return {
            "status": "success",
            "connector_id": "stripe",
            "message": "",
            "provider_http_status": r.status_code,
            "livemode": data.get("livemode"),
            "available_currencies": currencies,
        }
    except Exception as e:
        base["message"] = str(e)
        return base
