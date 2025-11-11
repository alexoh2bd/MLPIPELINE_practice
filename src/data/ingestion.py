# -*- coding: utf-8 -*-
# import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os

import kagglehub

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # Download latest version
    path = kagglehub.dataset_download(input_filepath, output_filepath+"medcosts.csv")
    print("Path to dataset files:", path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    input_path="saadaliyaseen/decoding-medical-costs-analyzing-insurance-data"
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    kagglehub.login()
    load_dotenv(find_dotenv())
    out_path = os.getcwd()+"/data"

    main(input_path, out_path)
