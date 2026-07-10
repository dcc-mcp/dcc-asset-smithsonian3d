---
name: smithsonian3d-assets
description: Search, inspect, and download Smithsonian CC0 3D files as validated AssetDescriptors.
license: MIT
compatibility: "dcc-mcp-core 0.19+, Python 3.7+"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - asset
      - smithsonian
      - open-access
      - cc0
      - 3d-models
      - download
    search-hint: "smithsonian 3d, open access 3d, cc0 museum model, voyager document, glb, usdz, download"
    produces: [asset_descriptor]
    tools: tools.yaml
---

# Smithsonian 3D Assets

Use this skill for Smithsonian Open Access 3D files. It exposes S3 object
search, Voyager document derivative listing, and direct downloads.

`download_smithsonian3d_file` returns an `asset_descriptor` with the local file, source URL,
and CC0 attribution. Pass that descriptor to a DCC adapter import skill; this source skill does
not modify a DCC scene.

