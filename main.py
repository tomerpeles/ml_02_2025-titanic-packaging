import config.data_config as data_config
from config import preprocessing_config, model_config
from src.collect_data import CollectData
from src.mode import Model
from src.preprocessing import Preprocessing
import os

collect_data = CollectData(data_config)
preprocessing = Preprocessing(preprocessing_config)
model = Model(model_config)

if __name__ == '__main__':

    input_data = collect_data.get_data(); # validation
    preprocessing_data = preprocessing.processing_data(input_data)
    result = model.predict(preprocessing_data)

    # save_result(result)

