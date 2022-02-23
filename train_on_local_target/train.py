from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from azureml.core.run import Run
import os
import numpy as np
import mylib
# sklearn.externals.joblib is removed in 0.23
try:
    from sklearn.externals import joblib
except ImportError:
    import joblib

os.makedirs('./outputs', exist_ok=True)

X, y = load_diabetes(return_X_y=True)

# allow_offline=True by default, so can be run locally as well
# If allow_offline=True (the default), actions against the Run 
# object will be printed to standard out, such as log etc.
run = Run.get_context()

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0)

data = {"train": {'X': X_train, 'y': y_train},
        "test": {'X': X_test, 'y': y_test}}

# list of numbers from 0.0 to 1.0 with a 0.05 interval
alphas = mylib.get_alphas()

for alpha in alphas:
    # Use Ridge algorithm to create a regression model
    reg = Ridge(alpha=alpha)
    reg.fit(data["train"]['X'], data["train"]['y'])

    preds = reg.predict(data["test"]["X"])
    mse = mean_squared_error(preds, data["test"]['y'])
    run.log('alpha', alpha)
    run.log('mse', mse)

    model_file_name = 'ridge_{0:.2f}.pkl'.format(alpha)
    model_dir_path = os.path.join('./outputs/', model_file_name)
    # save model in the outputs folder so it automatically get uploaded
    with open(model_dir_path, "wb") as file:
        joblib.dump(value=reg, filename=model_dir_path)
    
    print('alpha is {0:.2f}, and mse is {1:0.2f}'.format(alpha, mse))
