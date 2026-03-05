import os
from PIL import Image

assets_dir = r"C:\Users\natha\.gemini\antigravity\scratch\AstraAOA_repo\assets"

for filename in os.listdir(assets_dir):
    if filename.endswith(".png"):
        img_path = os.path.join(assets_dir, filename)
        try:
            with Image.open(img_path) as img:
                # Resize if larger than 1920 to save size
                max_size = 1920
                if img.width > max_size or img.height > max_size:
                    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                webp_path = os.path.join(assets_dir, filename.replace(".png", ".webp"))
                img.save(webp_path, format="WEBP", quality=80, method=4)
                print(f"Saved {webp_path}")
            os.remove(img_path)
            print(f"Removed {img_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
