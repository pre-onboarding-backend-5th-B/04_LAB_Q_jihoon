import os
import pandas as pd

from apiserver.models import SeoulGu as Gu
from apiserver.models import RainLocation as Location
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "insert rain location data"

    def handle(self, *args, **options):
        self.stdout.write("start insert rain location data!")

        rain_file_path = os.path.join(BASE_DIR, "res", "location", "rain_code.csv")

        rain_df = pd.read_csv(rain_file_path)

        for rain_row in rain_df.itertuples():
            rain_row_dict = rain_row._asdict()
            gu_code = rain_row_dict.get("구청코드")
            di = {
                "gu": Gu.objects.get(rain_gu_code=gu_code),
                "location_info": rain_row_dict.get("강우량계명"),
                "location_code": rain_row_dict.get("강우량계코드")
            }
            
            location_objects = Location(**di)
            location_objects.save()