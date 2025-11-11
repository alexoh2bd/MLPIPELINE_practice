from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging
from pathlib import Path
import os
import pandas as pd

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    df = pd.read_csv(input_filepath)
    xcols= ["age","bmi","children"]
    X_train,X_test,y_train,y_test = train_test_split(df[xcols], df['charges'], test_size=0.2)
    print(y_train)
    print(len(X_train), len(y_train), len(X_test),len(y_test))
    model = LinearRegression()
    model.fit(X_train,y_train)
    preds = model.predict(X_test)

    return mean_squared_error(preds,y_test)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    in_path = os.getcwd()+"/data/processed/insurance.csv"
    results_path = os.getcwd()+"/data/preds.csv"
    print("MSE:",main(in_path, results_path))