from src.data.load_data import load_dataset
from src.features.build_features import preprocess
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate

def main():
    train_df, test_df = load_dataset("data/raw/train.csv", "data/raw/test.csv")
    train_df = preprocess(train_df)
    test_df = preprocess(test_df)
    model = train_model(train_df.drop("target", axis=1), train_df["target"])
    mse = evaluate(model, test_df.drop("target", axis=1), test_df["target"])
    print("Test MSE:", mse)

if __name__ == "__main__":
    main()
