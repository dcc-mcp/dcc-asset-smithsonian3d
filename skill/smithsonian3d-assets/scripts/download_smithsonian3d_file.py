from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _smithsonian3d import LICENSE, download


@skill_entry
def main(source: str, output_dir: str, **_: Any) -> dict[str, Any]:
    try:
        file_path = download(source, output_dir)
        return skill_success("Smithsonian 3D file downloaded", file=file_path, source=source, **LICENSE)
    except Exception as exc:
        return skill_exception(exc, message="Failed to download Smithsonian 3D file")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)

