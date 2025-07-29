def evaluate(model, X_test, y_test):
    from sklearn.metrics import mean_squared_error
    preds = model.predict(X_test)
    return mean_squared_error(y_test, preds)
