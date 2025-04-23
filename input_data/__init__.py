import glob

sermons = {}
for filename in glob.glob("input_data/*.txt"):
    with open(filename, 'r') as f:
        sermons[filename] = f.read()

__all__ = ["sermons"]