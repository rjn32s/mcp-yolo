---
description: Automatically builds the Docker container and prepares it for deployment.
---

# YOLO Deploy Skill

This skill automates the process of building the MCP-YOLOE Docker container.

## Steps

1. **Build the Docker Image**
   // turbo
   ```bash
   docker build -t mcp-yolo:latest .
   ```

2. **Tag the Image (Optional)**
   ```bash
   docker tag mcp-yolo:latest your-registry/mcp-yolo:latest
   ```

3. **Verify the Build**
   ```bash
   docker images | grep mcp-yolo
   ```
