import pickle

def to_pickle(file_path, file, protocol=4):
    """dump file to pickle"""
    with open(file_path, "wb") as fp:
        pickle.dump(file, fp, protocol)
        
def from_pickle(file_path):
    """load pickle file"""
    with open(file_path, "rb") as fp:
        return pickle.load(fp)
