from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _smithsonian3d import API_BASE, LICENSE, document


@skill_entry
def main(document_id: str, **_: Any) -> dict[str, Any]:
    try:
        doc = document(document_id)
        assets = []
        for model in doc.get("models", []):
            for derivative in model.get("derivatives", []):
                for asset in derivative.get("assets", []):
                    if asset.get("type") != "Model":
                        continue
                    url = f"{API_BASE}/{document_id}/{asset.get('uri')}"
                    assets.append(
                        {
                            "uri": asset.get("uri"),
                            "url": url,
                            "usage": derivative.get("usage"),
                            "quality": derivative.get("quality"),
                            "byte_size": asset.get("byteSize"),
                            "num_faces": asset.get("numFaces"),
                            **LICENSE,
                        }
                    )
        return skill_success("Smithsonian 3D document listed", document_id=document_id, assets=assets)
    except Exception as exc:
        return skill_exception(exc, message="Failed to list Smithsonian 3D document")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

