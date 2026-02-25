import os
import base64
import requests
import io
from PIL import Image
from fastmcp import FastMCP
from mcp_yolo.engine import YOLOEWrapper

# Initialize FastMCP server
mcp = FastMCP("mcp-yolo")

# Global engine instance for warm loading
_engine = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = YOLOEWrapper(model_path="yoloe-26l-seg.pt")
    return _engine

def process_image_source(source: str):
    """
    Detects and processes the image source (path, URL, or base64).
    Returns a source that Ultralytics can handle (path or PIL Image).
    """
    # Check if it's base64
    if source.startswith("data:image") or ";base64," in source:
        try:
            header, encoded = source.split(";base64,")
            decoded = base64.b64decode(encoded)
            return Image.open(io.BytesIO(decoded))
        except Exception as e:
            raise ValueError(f"Failed to decode base64 image: {e}")
    
    # Check if it looks like a URL
    if source.startswith(("http://", "https://")):
        # We can let Ultralytics handle URLs directly, 
        # but sometimes it's safer to download if headers are needed.
        # However, passing the URL string directly is most efficient for Ultralytics.
        return source

    # Assume it's a file path
    if not os.path.exists(source):
        raise FileNotFoundError(f"Image path '{source}' does not exist.")
    
    return source

@mcp.tool()
def detect_objects(image_source: str, classes: list[str] = None):
    """
    Perform zero-shot object detection on an image.
    
    Args:
        image_source: Path to image, URL, or base64 data string.
        classes: Optional list of class names to detect (zero-shot).
    """
    try:
        processed_source = process_image_source(image_source)
        engine = get_engine()
        detections = engine.detect(processed_source, classes)
        return detections
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def segment_objects(image_source: str, classes: list[str] = None):
    """
    Perform zero-shot instance segmentation on an image.
    
    Args:
        image_source: Path to image, URL, or base64 data string.
        classes: Optional list of class names to segment (zero-shot).
    """
    try:
        processed_source = process_image_source(image_source)
        engine = get_engine()
        segmentations = engine.segment(processed_source, classes)
        return segmentations
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
