import os
import pandas as pd

from apiserver.models import SeoulGu as Gu
from django.core.management.base import BaseCommand, CommandError
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "Insert Gu data"

    def handle(self, *args, **options):
        self.stdout.write("!start insert Gu data!")
        rain_file_path = os.path.join(BASE_DIR, "res", "gu", "rain_gu.csv")
        rain_df = pd.read_csv(rain_file_path)
        for rain_row in rain_df.itertuples():
            rain_row_dict = rain_row._asdict()

            di = {
                "name": rain_row_dict.get("구청명"),
                "rain_gu_code": rain_row_dict.get("구청코드"),
            }
            gu_objects = Gu(**di)
            gu_objects.save()
