from coffee.extract import extract_cafe, extract_cappuccino_index
from coffee.transform import clean_cafe_data, clean_cappuccino_data

def run_pipeline():
    cafe = clean_cafe_data(extract_cafe())
    cappuccino_index = clean_cappuccino_data(extract_cappuccino_index())
    return cafe, cappuccino_index