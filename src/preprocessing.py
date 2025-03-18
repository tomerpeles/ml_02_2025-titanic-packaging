from src.exceptions import DependencyException
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

class Preprocessing():
    def __init__(self,config):
        self.scaler_file = config.scaler_file
        self.labelencoder_file = config.label_encoder_file
        self.processing_map = config.processing_map

    def load_dependency(self):
        try:
            with open(self.scaler_file, 'rb') as f:
                self.scaler = pickle.load(f)

            with open(self.labelencoder_file, 'rb') as f:
                self.labelencoder_array = pickle.load(f)

                self.labelencoder_sex = self.labelencoder_array[self.processing_map['sex_label_encoder']]
                self.labelencoder_embarked = self.labelencoder_array[self.processing_map['embarked_label_encoder']]
                self.labelencoder_cabin = self.labelencoder_array[self.processing_map['cabin_label_encoder']]

        except Exception as e:
            raise DependencyException('Preprocessing load_dependency failed') from e

    def _processing_data(self,dataset):
        dataset['Sex'] = self.labelencoder_sex.transform(dataset['Sex'].astype(str))
        dataset['Embarked'] = self.labelencoder_embarked.transform(dataset['Embarked'].astype(str))
        dataset['Cabin'] = self.labelencoder_cabin.transform(dataset['Cabin'].astype(str))

        dataset['Age'] = dataset['Age'].fillna(self.processing_map['age_fillna'])
        dataset['Embarked'] = dataset['Embarked'].fillna(self.processing_map['embraked_fillna'])

        dataset = dataset.drop(['Name', 'Ticket', 'PassengerId'], axis=1)

        dataset[self.processing_map['scalaer_columns']] = self.scaler.transform(dataset[self.processing_map['scalaer_columns']])

        dataset = dataset.drop('Survived', axis=1)  # dataset
        return dataset


    def processing_data(self,dataset):
        self.load_dependency()
        return self._processing_data(dataset)

