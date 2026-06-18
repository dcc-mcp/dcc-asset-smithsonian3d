---
name: smithsonian3d-assets
description: Search, inspect, and download Smithsonian Open Access CC0 3D files.
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    display_name: Smithsonian 3D Assets
    group: asset.download.cc0
    default_icon: package
    affinity: any
    marketplace: dcc-asset-smithsonian3d
    tools: tools.yaml
    execution: sync
    permissions:
      - network
      - filesystem
    examples:
      - "Search Smithsonian Open Access 3D GLB files"
      - "List derivatives for a Smithsonian 3D document"
      - "Download a Smithsonian 3D GLB file"
    contact:
      name: dcc-mcp team
      url: https://github.com/dcc-mcp/dcc-asset-smithsonian3d
    install:
      add_source: "dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-smithsonian3d"
      then_install: "dcc-mcp-cli marketplace install dcc-asset-smithsonian3d"
---

# Smithsonian 3D Assets

Use this skill for Smithsonian Open Access 3D files. It exposes S3 object
search, Voyager document derivative listing, and direct downloads.

