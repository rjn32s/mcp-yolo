---
description: Runs an automated performance benchmark on local hardware to recommend YOLOE model size.
---

# YOLO Bench Skill

This skill benchmarks the YOLOE model on your local hardware (CPU/GPU/MPS) to determine the best model size.

## Steps

1. **Run Benchmark Script**
   // turbo
   ```bash
   uv run python -c "from ultralytics import YOLOE; import time; m = YOLOE('yoloe-26l-seg.pt'); start = time.time(); m.predict('bus.jpg'); print(f'Inference time: {time.time() - start:.4f}s')"
   ```

2. **Compare Model Sizes**
   > [!NOTE]
   > For faster performance on edge hardware, consider using `yoloe-26s-seg.pt` (Small) or `yoloe-26n-seg.pt` (Nano).
