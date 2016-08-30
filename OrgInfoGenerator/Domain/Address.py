class Address(object):
    """
    Coordinates
    """

    def __init__(self, address_info):
        self.address_value = address_info['unrestricted_value']
        self.latitude = address_info['data']['geo_lat']
        self.longitude = address_info['data']['geo_lon']
