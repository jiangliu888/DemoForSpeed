import xmltodict


def load_xml(data):
    return xmltodict.parse(data)
