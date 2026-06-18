from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _smithsonian3d import LICENSE, S3_BASE, list_s3


@skill_entry
def main(
    query: str | None = None,
    limit: int = 10,
    extensions: list[str] | None = None,
    **_: Any,
) -> dict[str, Any]:
    try:
        allowed = {("." + e.lower().lstrip(".")) for e in (extensions or ["glb", "gltf", "obj", "usdz"])}
        needle = (query or "").lower()
        files = []
        for item in list_s3(max_keys=1000):
            key = item["key"]
            if not any(key.lower().endswith(ext) for ext in allowed):
                continue
            if needle and needle not in key.lower():
                continue
            files.append({"key": key, "url": f"{S3_BASE}/{key}", "size": item["size"], **LICENSE})
            if len(files) >= limit:
                break
        return skill_success("Smithsonian 3D files found", files=files, count=len(files))
    except Exception as exc:
        return skill_exception(exc, message="Failed to search Smithsonian 3D files")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

