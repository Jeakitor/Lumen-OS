def recommend_profile(hardware):
  def recommend_profile(hardware):
    ram = hardware.get("ram_mb", 0)

    # Base assumption: OS is already optimized
    # Profile only controls extras

    if ram < 4096:
        return "minimal"
    elif ram < 8000:
        return "standard"
    else:
        return "standard"  # still standard by default
