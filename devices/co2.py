import mh_z19


class Co2:
    @staticmethod
    def get_data():
        return mh_z19.read_all()
