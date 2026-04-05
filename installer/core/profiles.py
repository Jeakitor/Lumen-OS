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

#VERY TEMPORARY IM GOIGN TO NEED TO RETHINK THE LOGIC FOR THIS ENTIRE THING MIGHT HAVE MASIVE CHANGES
#DUE TO THE FACT I CANT LET THIS BE THE LIMITER FOR THE ENTIRE OS
#WE WONT DECIDE AN INSTALL JUDGING OFF RAM, THE USER THEMSELVES WILL BE BLESSED WITH THE ABILITY TO DECIDE WHAT THEY WANT!!!
