# MCP-YOLO
[![PyPI](https://img.shields.io/pypi/v/mcp-yolo)](https://pypi.org/project/mcp-yolo/)
[![Downloads](https://static.pepy.tech/personalized-badge/mcp-yolo?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/mcp-yolo)
mcp-name: io.github.rjn32s/mcp-yolo

MCP-YOLO is an agent-first development platform that provides **Zero-Shot Object Detection and Segmentation** as a Model Context Protocol (MCP) server. Powered by **Ultralytics YOLOE**, it enables developers and AI agents to detect and segment objects using arbitrary text prompts without retraining.

## Key Features
- **Zero-Shot Detection:** Detect any object using natural language (e.g., "the blue coffee cup next to the spoon").
- **Instance Segmentation:** Precise polygon masks for discovered objects.
- **Flexible Image Inputs:** Supports local file paths, remote URLs, and Base64 encoded strings.
- **Agent Optimized:** Includes custom "Skills" for autonomous deployment and benchmarking.

## YOLOE Performance Reference

YOLOE builds upon the latest YOLO architectures (like YOLO11 and YOLO26) to provide state-of-the-art open-vocabulary performance.

| Model | Based On | mAP (COCO) | Speed (T4/ms) | Params (M) |
| :--- | :--- | :---: | :---: | :---: |
| **YOLOE26-N** | YOLO26-N | 40.9 | 1.7 | ~3.0 |
| **YOLOE26-S** | YOLO26-S | 48.6 | 2.5 | ~10.0 |
| **YOLOE26-L** | YOLO26-L | 55.0 | 6.2 | ~40.0 |
| **YOLOE-L** | YOLO11-L | ~52.0 | ~5.0 | ~26.0 |

*Note: Performance varies depending on the hardware and input resolution. `mcp-yolo` uses `yoloe-26l-seg.pt` by default for high precision.*

## Quick Start

### Installation
```bash
uv pip install mcp-yolo
```

### Running the Server
```bash
uv run mcp-yolo
```

##  MCP Tools

### `detect_objects`
Performs zero-shot detection.
- **Arguments:**
  - `image_source` (str): Path, URL, or Base64.
  - `classes` (list[str], optional): Custom text prompts to detect.

### `segment_objects`
Performs zero-shot instance segmentation.
- **Arguments:**
  - `image_source` (str): Path, URL, or Base64.
  - `classes` (list[str], optional): Custom text prompts to segment.

##  Publishing
This project is configured for automated PyPI publishing. See the [pypi_setup_guide.md](file:///Users/rajanshukla/.gemini/antigravity/brain/6a2d32ac-d625-45bb-8f98-3d2916ab776e/pypi_setup_guide.md) for details.
