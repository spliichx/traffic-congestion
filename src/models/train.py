def train_model(X_train, y_train):
    from sklearn.ensemble import GradientBoostingRegressor
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)
    return model
