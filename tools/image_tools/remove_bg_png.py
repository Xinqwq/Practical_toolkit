#!usrbinenv python3
# -- coding utf-8 --

Batch background removal (Optional humanobject model + black edge fix + mode presets + user parameters)
After running, you can choose the model and preset mode by number, or set custom parameters manually.


import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set U2NET model home directory
U2NET_HOME = os.getenv(U2NET_HOME) or os.path.expanduser(~.u2net)
os.environ[U2NET_HOME] = U2NET_HOME

try
    from rembg import remove, new_session
    from PIL import Image, ImageFilter
    import numpy as np
except ImportError
    sys.exit(Please install required packages first pip install rembg pillow numpy)

# Supported image extensions
SUPPORT_EXT = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}

# ========= Preset Modes ==========
PRESETS = {
    1 {
        name Ultra Clean (may lose details),
        f_threshold 245, b_threshold 10, erode 1, blur 0.0, min_alpha 200
    },
    2 {
        name Balanced Mode (recommended for most cases),
        f_threshold 230, b_threshold 15, erode 0, blur 0.3, min_alpha 128
    },
    3 {
        name Detail Preserving Mode (safe for fine hairhat edges),
        f_threshold 200, b_threshold 20, erode 0, blur 0.8, min_alpha 100
    },
    4 {
        name Super Soft Mode (keep all details, smooth edges, may leave background traces),
        f_threshold 180, b_threshold 25, erode 0, blur 1.2, min_alpha 80
    },
    5 {
        name Non-human Object Mode (graywhite grid or general object background),
        f_threshold 200, b_threshold 40, erode 0, blur 0.5, min_alpha 128
    },
    6 {
        name Custom Mode,
    }
}
# ============================

# ========= User Input ==========
def ask_int(prompt, default)
    s = input(f{prompt} (default {default}) ).strip()
    return int(s) if s.isdigit() else default

def ask_float(prompt, default)
    s = input(f{prompt} (default {default}) ).strip()
    try
        return float(s) if s else default
    except
        return default

def ask_path(prompt, default=.)
    s = input(f{prompt} (default {default}) ).strip()
    return Path(s) if s else Path(default)

def choose_model()
    print(==== Model Selection ====)
    print(1. u2net_human_seg (human segmentation))
    print(2. u2net (general objectbackground))
    choice = ask_int(Choose model number, 1)
    return u2net_human_seg if choice == 1 else u2net

def get_user_params()
    print(==== Mode Selection ====)
    for k, v in PRESETS.items()
        print(f{k}. {v['name']})
    mode = ask_int(Choose mode number, 2)

    root = ask_path(Input image directory, .)
    workers = ask_int(Number of threads, 8)

    if mode in PRESETS and mode != 6
        params = PRESETS[mode].copy()
        params.pop(name, None)
        print(fUsing preset mode {PRESETS[mode]['name']}  Parameters={params})
    else
        print(Manual parameter input (press Enter to use default))
        params = {
            f_threshold ask_int(Foreground threshold [recommended 180~240], 230),
            b_threshold ask_int(Background threshold [recommended 5~40], 20),
            erode ask_int(Erode size [0~5, larger shrinks foreground], 0),
            blur ask_float(Gaussian blur radius [0~2.0], 0.3),
            min_alpha ask_int(Minimum foreground alpha [0~255], 128),
        }
    return root, workers, params

# ============================

def make_out_path(src_path Path, root Path) - Path
    # Create output path under 'transparent' subfolder
    rel = src_path.relative_to(root)
    out_dir = root  transparent  rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir  (src_path.stem + .png)

def process_one(src Path, root Path, params dict, model_name str)
    out = make_out_path(src, root)
    try
        with Image.open(src) as im
            im = im.convert(RGBA)
            no_bg = remove(
                im,
                session=new_session(model_name),
                alpha_matting=True,
                alpha_matting_foreground_threshold=params[f_threshold],
                alpha_matting_background_threshold=params[b_threshold],
                alpha_matting_erode_size=params[erode]
            )

            # Apply Gaussian blur to alpha channel
            if params[blur]  0
                alpha = no_bg.getchannel(A).filter(ImageFilter.GaussianBlur(radius=params[blur]))
                no_bg.putalpha(alpha)

            # Ensure minimum alpha
            alpha_np = np.array(no_bg.getchannel(A))
            alpha_np = np.where(alpha_np  0, np.maximum(alpha_np, params[min_alpha]), alpha_np)
            no_bg.putalpha(Image.fromarray(alpha_np))

            no_bg.save(out, PNG)
        return fOK  {src.name}
    except Exception as e
        return fERR {src.name}  {e}

def main()
    model_name = choose_model()
    root, workers, params = get_user_params()

    if not root.is_dir()
        sys.exit(fDirectory not found {root})

    imgs = [p for p in root.rglob('') if p.suffix.lower() in SUPPORT_EXT]
    if not imgs
        print(No supported images found); return

    print(fFound {len(imgs)} images. Starting background removal... Model={model_name})
    ok = 0
    with ThreadPoolExecutor(max_workers=workers) as pool
        futures = {pool.submit(process_one, p, root, params, model_name) p for p in imgs}
        for f in as_completed(futures)
            msg = f.result()
            print(msg)
            if msg.startswith(OK) ok += 1
    print(fAll done! Success {ok}{len(imgs)}. Transparent images saved in {root}transparent)

if __name__ == __main__
    main()
