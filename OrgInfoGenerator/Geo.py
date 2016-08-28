class Geo(object):
    """
    Coordinates
    """

    def __init__(self, address_info):
        self.address_value = address_info['unrestricted_value']
        self.geo_lat = address_info['data']['geo_lat']
        self.geo_lon = address_info['data']['geo_lon']
