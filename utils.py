def cross_out(data: str):
    data = list(data)
    return "".join(list(map(lambda i: f"{i}̶", data)))
