import os


def datapath(*args):
    here = os.path.abspath(os.path.dirname(__file__))
    data_directory = os.path.join(here, 'data')
    return os.path.join(data_directory, *args)
