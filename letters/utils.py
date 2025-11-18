import requests


def get_location_by_ip(ip_address: str):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url, timeout=3)

        if response.status_code != 200:
            return {
                "ip_address": ip_address,
                "country": None,
                "state": None
            }

        data = response.json()

        return {
            "ip_address": ip_address,
            "country": data.get("country"),
            "state": data.get("region"),
        }

    except Exception:
        return {
            "ip_address": ip_address,
            "country": None,
            "state": None
        }


def get_user_location(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    if ip in ("127.0.0.1", "localhost"):
        ip = "8.8.8.8"

    return get_location_by_ip(ip)
