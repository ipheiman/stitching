import os
import re

# ==== CONFIGURATION ====
folder = "/mnt/c/Users/iheiman/Desktop/CODE/demis/datasets/5x5"
dataset_name = "5x5"
grid_index = 0
slice_index = 0
rows, cols = 5, 5  # grid size

# ==== FILENAME PATTERN ====
pattern = re.compile(r"img_r(\d{3})_c(\d{3})\.tif")

# ==== RENAME FILES ====
for filename in os.listdir(folder):
    match = pattern.match(filename)
    if match:
        r = int(match.group(1)) - 1  # 0-indexed row
        c = int(match.group(2)) - 1  # 0-indexed col
        tile_index = r * cols + c

        new_name = f"{dataset_name}_g{grid_index}_t{tile_index}_s{slice_index}.tif"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)

        print(f"Renaming: {filename} → {new_name}")
        os.rename(src, dst)
