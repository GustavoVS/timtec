import os
import hashlib


def hash_name(path, attr):
    def wrapper(instance, filename):
        root, ext = os.path.splitext(filename)
        m = hashlib.md5()
        m.update(root.encode('utf-8'))
        name = getattr(instance, attr)
        if name:
            m.update(name.encode('utf-8'))
        filename = m.hexdigest() + ext
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper
