def detect_drifts(series: list) -> list:
    result = []
    values = [v for _, v in series]
    avg = sum(values) / len(values)
    threshold = avg * 0.25

    for i, (_, v) in enumerate(series):
        if abs(v - avg) > threshold:
            result.append((i, v))

    return result
