from __future__ import annotations

import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


S3_BASE = "https://smithsonian-open-access.s3.us-west-2.amazonaws.com"
API_BASE = "https://3d-api.si.edu/content/document"
LICENSE = {
    "license_name": "CC0 1.0 Universal",
    "license_url": "https://www.si.edu/openaccess/faq",
    "usage_notice": "Smithsonian Open Access 3D assets are CC0/public domain dedication items.",
}


def _url(path_or_url: str) -> str:
    if path_or_url.startswith(("http://", "https://")):
        return path_or_url
    return f"{S3_BASE}/{urllib.parse.quote(path_or_url)}"


def list_s3(prefix: str = "3d/", max_keys: int = 1000) -> list[dict[str, Any]]:
    url = f"{S3_BASE}/?list-type=2&prefix={urllib.parse.quote(prefix)}&max-keys={max_keys}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        root = ET.fromstring(resp.read())
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    items = []
    for contents in root.findall("s3:Contents", ns):
        key = contents.findtext("s3:Key", default="", namespaces=ns)
        size = contents.findtext("s3:Size", default="0", namespaces=ns)
        items.append({"key": key, "size": int(size)})
    return items


def document(document_id: str) -> dict[str, Any]:
    url = f"{API_BASE}/{urllib.parse.quote(document_id)}/document.json"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download(source: str, output_dir: str) -> str:
    url = _url(source)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    target = Path(output_dir) / Path(urllib.parse.urlparse(url).path).name
    req = urllib.request.Request(url, headers={"User-Agent": "dcc-mcp-smithsonian3d/0.1"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        target.write_bytes(resp.read())
    return str(target)

