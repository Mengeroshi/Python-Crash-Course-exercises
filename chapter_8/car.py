def car(mnfr, model, **car_info):
    """
    return the information that you insert in a dictionary
    """
    car_info["manufacturer"] = mnfr
    car_info["model name"] = model
    return car_info