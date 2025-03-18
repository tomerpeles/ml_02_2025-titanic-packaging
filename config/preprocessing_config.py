import os

# label_encoder_file = os.getenv('label_encoder_file')
label_encoder_file = 'models/v1/labelencoder_v1.pkl'
scaler_file = 'models/v1/scaler_v1.pkl'


processing_map = {
    'sex_label_encoder' : 'le_sex',
    'embarked_label_encoder' : 'le_embarked',
    'cabin_label_encoder' : 'le_cabin',
    'age_fillna' : 28.46275356382107,
    'embraked_fillna' : 2,
    'scalaer_columns': ['Age', 'Fare', 'Pclass', 'SibSp', 'Parch']
}