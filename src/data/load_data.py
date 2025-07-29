

def load_dataset(train_path, test_path):
    import pandas as pd
    return pd.read_csv(train_path), pd.read_csv(test_path)
