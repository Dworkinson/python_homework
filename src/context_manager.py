class Open:
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self._path, self._mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


if __name__ == '__main__':
    with Open('catdog.py', 'r') as var:
        print(var.read())
