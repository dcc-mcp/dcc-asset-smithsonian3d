from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _smithsonian3d import LICENSE, asset_descriptor, download


@skill_entry
def main(source: str, output_dir: str, **_: Any) -> dict[str, Any]:
    try:
        file_path = download(source, output_dir)
        return skill_success(
            "Smithsonian 3D file downloaded",
            file=file_path,
            source=source,
            asset_descriptor=asset_descriptor(source, file_path),
            **LICENSE,
        )
    except Exception as exc:
        return skill_exception(exc, message="Failed to download Smithsonian 3D file")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

