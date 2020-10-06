from dataclasses import dataclass
import pandas as pd
import os
import xlrd
import googlemaps
from googlemaps import Client

@dataclass
class FileReader:
    
    context: str =''
    fname: str =''
    train: object = None
    test: object = None
    id: str = ''
    label: str =''

    def new_file(self) -> str:
        return os.path.join(self.context + self.fname)

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self,header,usecols) -> object:
        return pd.read_excel(self.new_file(), header=header, usecols=usecols)

    def create_gmaps(self):
        return googlemaps.Client(key='')