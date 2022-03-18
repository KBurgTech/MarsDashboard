import requests

URL = "https://api.nasa.gov/insight_weather/?api_key=gRN4Kg2n53Qd3L91seeZMhPTdv9phB9IOFG9VWvb&feedtype=json&ver=1.0"


def get_fake_weather():
    return {  # Start of summary data for Sol 259
        "AT": {"av": -71.233, "ct": 326642, "mn": -101.024, "mx": -27.149},
        # Atmospheric temperature data for Sol 259
        "HWS": {"av": 4.35, "ct": 154146, "mn": 0.156, "mx": 17.617},  # Horizontal wind speed data for Sol 259
        "PRE": {"av": 761.006, "ct": 163012, "mn": 742.1498, "mx": 780.3891},  # Pressure data for Sol 259
        "WD": {  # Wind direction summary for Sol 259
            # N.B. only a subset of the WD keys are shown in this sample
            "most_common": {"compass_degrees": 202.5, "compass_point": "SSW", "compass_right": -0.382683432365,
                            # Wind direction data for most common compass point
                            "compass_up": -0.923879532511, "ct": 28551},
            # N.B. count (key “ct”) is 28551, which is the number of
            # WD readings in this compass point
            "8": {"compass_degrees": 180.0, "compass_point": "S", "compass_right": 0.0,
                  # Wind direction data for compass point 8=South; count is less
                  "compass_up": -1.0, "ct": 17699},  # than that for most common point; points 1-7 and 11-16 are
            # excluded in this example to save space, but the counts could
            # be used to display a wind rose histogram c.f. this website.
            "9": {"compass_degrees": 202.5, "compass_point": "SSW", "compass_right": -0.382683432365,
                  # Wind direction data for compass point 9=SSW
                  "compass_up": -0.923879532511, "ct": 28551},
            # N.B. count (key “ct”) is 28551, which matches that of the
            # most common key above i.e. this is the same point
            "10": {"compass_degrees": 225.0, "compass_point": "SW", "compass_right": -0.707106781187,
                   "compass_up": -0.707106781187, "ct": 27124}
        },
        "First_UTC": "2019-08-19T08:03:59Z", "Last_UTC": "2019-08-20T08:43:34Z",
        "Season": "winter"  # Miscellaneous provance: UTC range; season.
    }


def get_weather():
    response = requests.get(URL)
    data = response.json()
    if not data["sol_keys"]:
        return get_fake_weather()
    else:
        return data[data["sol_keys"][-1]]
