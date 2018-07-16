import msgpack


def deserialize(cassette_string):
    try:
        return msgpack.unpackb(cassette_string)
    except (OutOfData, ValueError) as e:
        raise ValueError(str(e))


def serialize(cassette_dict):
    return msgpack.packb(cassette_dict)
