import pandas as pd
from yieldcurve.models import YieldCurve

def import_excel_to_db(file_path):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        date = row ['Date']
        for column in df.columns[1:]:
            maturity = column
            yield_value = row[column]
            if not pd.isna(yield_value):
                YieldCurve.objects.create(date=date, maturity=maturity, yield_value=yield_value)
            
    file_path = "C:/Users/NBKR/yield_db.xlsx"
    import_excel_to_db(file_path)
    print("Данные успешно импортированы")