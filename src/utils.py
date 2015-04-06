# this is just a test
import numpy as np
import glob


def read_features(directory='../data/', feature='fft'):
    """
    Utilty function to read all the features and labels into a numpy
        array
    Args:
        directory (string) : path to the data dir
        feature (string): the feature you want to get
    Returns:
        Tuple of (class labels, featureset)
    """

    glob_id = directory + '*.' + feature + '.npy'
    all_features = glob.glob(glob_id)
    # trims filename and splits on periods to get just the class type
    class_name_list = [name[8:len(name)-1].split('.')[0] for name in
                       all_features]
    # makes a set
    classes = {name for name in class_name_list}
    # makes a dict of features with numeric label
    classes = {name: val for val, name in enumerate(classes)}
    # makes a vector of labels
    label_vec = [classes[lab] for lab in class_name_list]
    class_labels = np.array(label_vec)
    # reads all the features in via numpy
    return (classes, class_labels,
            np.array([np.load(f) for f in all_features]))



