from typing import Any
import httpx


def get_auth_token(username: str, password: str) -> str | None:
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    result = httpx.post(
        "https://services.sc.kamaz.tech/auth/token", headers=headers, data=data
    )
    if result.status_code == 200:
        data = result.json()
        return data.get("access_token")
    return None


def load_services(token: str, json: dict[str, Any]) -> bool:
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    result = httpx.post(
        "https://services.sc.kamaz.tech/v1/services/load", headers=headers, json=json
    )
    if result.status_code == 200:
        data = result.json()
        return data.get("ok", False)
    return False
