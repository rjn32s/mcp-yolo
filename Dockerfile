# Use a stable Python image
FROM python:3.12-slim

# Add MCP Metadata Label
LABEL "mcp-name"="io.github.rjn32s/mcp-yolo"

# Install system dependencies for OpenCV and Ultralytics
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files
COPY . .

# Install dependencies and the package
RUN uv sync --frozen

# CMD runs the server via stdio
CMD ["uv", "run", "mcp-yolo"]
