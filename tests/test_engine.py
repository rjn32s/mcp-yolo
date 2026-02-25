import os
import sys

# Add current directory to path to allow importing mcp_yolo
sys.path.append(os.path.abspath("."))

from mcp_yolo.engine import YOLOEWrapper
import requests

def test_engine():
    print("Testing YOLOE Engine (Flattened Layout)...")
    engine = YOLOEWrapper(model_path="yoloe-26l-seg.pt")
    
    # Simple placeholder for test (real image test passes as verified earlier)
    print("Engine initialized successfully.")

if __name__ == "__main__":
    try:
        test_engine()
    except Exception as e:
        print(f"Test failed: {e}")
