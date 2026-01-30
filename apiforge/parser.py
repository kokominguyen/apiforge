import json
import yaml


def load_spec(path: str) -> dict:
    if path.endswith(".json"):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    if path.endswith((".yml", ".yaml")):
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    raise ValueError("Unsupported OpenAPI format")


def parse_endpoints(spec: dict) -> list[dict]:
    endpoints = []

    for path, methods in spec.get("paths", {}).items():
        for method, meta in methods.items():
            endpoints.append({
                "name": meta.get(
                    "operationId",
                    f"{method}_{path.strip('/').replace('/', '_')}"
                ),
                "method": method.lower(),
                "path": path
            })
    return endpoints
