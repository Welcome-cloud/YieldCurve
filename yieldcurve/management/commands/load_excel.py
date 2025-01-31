import pandas as pd
from django.core.management.base import BaseCommand
from yieldcurve.models import YieldCurve
import pandas as pd
from django.core.management.base import BaseCommand
from yieldcurve.models import YieldCurve
import pandas as pd
from django.core.management.base import BaseCommand
from yieldcurve.models import YieldCurve

YieldCurve.objects.all().delete()

class Command(BaseCommand):
    help = "Загружает данные из эксель в модель"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="C:/Users/NBKR/yield_db.xlsx")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            df = pd.read_excel(file_path)

            required_columns = [
                'Date', 'YTM_1d', 'YTM_7d', 'YTM_14d', 'YTM_28d', 'YTM_91d',
                'YTM_182d', 'YTM_12m', 'YTM_2y', 'YTM_3y', 'YTM_5y', 'YTM_7y', 'YTM_10y',
            ]
            for column in required_columns:
                if column not in df.columns:
                    self.stderr.write(self.style.ERROR(f"Колонка '{column}' отсутствует в Excel!"))
                    return

            objects = [
                YieldCurve(
                date=row['Date'],
                ytm_1d=row['YTM_1d'],
                ytm_7d=row['YTM_7d'],
                ytm_14d=row['YTM_14d'],
                ytm_28d=row['YTM_28d'],
                ytm_91d=row['YTM_91d'],
                ytm_182d=row['YTM_182d'],
                ytm_12m=row['YTM_12m'],
                ytm_2y=row['YTM_2y'],
                ytm_3y=row['YTM_3y'],
                ytm_5y=row['YTM_5y'],
                ytm_7y=row['YTM_7y'],
                ytm_10y=row['YTM_10y'],
                )
                for _, row in df.iterrows()
            ]
            YieldCurve.objects.bulk_create(objects)

            self.stdout.write(self.style.SUCCESS(f"Данные из файла '{file_path}' успешно загружены!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка загрузки данных {e}"))