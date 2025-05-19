---------------------------------------------------------------------
FLOW: 
tile_stitcher > grid_stitcher > demis_stitcher > stitch.py
---------------------------------------------------------------------
CONFIGS: configs/
---------------------------------------------------------------------
CODE:
1. Local Stitching with LOFTR
2. Hill Climb 
3. Global Stitching using MST 
---------------------------------------------------------------------


1. Local Stitching with LOFTR
tile_stitcher.py [Line 96]
=> def compute_matches(self, img1_full, img2_full, horizontal=True):
   return matches1, matches2, conf

2. Hill Climb
hill_climb.py
=> def hill_climb_ncc(img1, img2, pt1, pt2, patch_size=50, max_iter=100):
   return (x1, y1), (x2, y2), best_score

3. Global Stitching using MST
grid_stitcher.py [Line 108]
=> def stitch_grid_mst(
        self,
        tile_paths,
        transformations=None,
        root_transformation=None,
        plot_prefix="",
    ):


