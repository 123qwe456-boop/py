def tracker_nested_loop(n):
    total_points = 0
    # Outer loop tracks each lap
    for lap in range(1, n + 1):
        # Inner loop manually increments 1 point for every step of that lap
        for point in range(lap):
            total_points += 1
    return total_points
