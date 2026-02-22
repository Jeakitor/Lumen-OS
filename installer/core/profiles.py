def recommend_profile(hardware):
    ram = hardware.get("ram_mb")

    if ram is None:
        return "standard"

    if ram < 4096:
        return "low_spec"
    else:
        return "standard"
