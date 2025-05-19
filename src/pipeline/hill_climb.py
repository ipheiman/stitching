def compute_ncc(patch1, patch2):
    patch1 = patch1.astype(np.float32)
    patch2 = patch2.astype(np.float32)
    mean1 = patch1.mean()
    mean2 = patch2.mean()
    numerator = np.sum((patch1 - mean1) * (patch2 - mean2))
    denominator = np.sqrt(np.sum((patch1 - mean1)**2) * np.sum((patch2 - mean2)**2))
    return numerator / (denominator + 1e-6)

def hill_climb_ncc(img1, img2, pt1, pt2, patch_size=50, max_iter=100):
    # Initialize all directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # pt1: (x,y) keypoint on img1
    # pt2: (x,y) keypoint on img2
    x1, y1 = int(pt1[0]), int(pt1[1])
    x2, y2 = int(pt2[0]), int(pt2[1])
    half = patch_size // 2 

    def get_patch(img, x, y):
        return img[y - half:y + half, x - half:x + half]

    best_score = compute_ncc(get_patch(img1, x1, y1), get_patch(img2, x2, y2))

    for _ in range(max_iter):
        improved = False
        for dx, dy in directions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            try:
                p1_patch = get_patch(img1, nx1, ny1)
                p2_patch = get_patch(img2, nx2, ny2)
                if p1_patch.shape != (patch_size, patch_size) or p2_patch.shape != (patch_size, patch_size):
                    continue
                score = compute_ncc(p1_patch, p2_patch)
                if score > best_score:
                    x1, y1, x2, y2 = nx1, ny1, nx2, ny2
                    best_score = score
                    improved = True
                    break
            except:
                continue
        if not improved:
            break
    return (x1, y1), (x2, y2), best_score
