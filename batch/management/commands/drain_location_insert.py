import os
import pandas as pd

from apiserver.models import SeoulGu as Gu
from apiserver.models import DrainLocation as Location
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "insert drain location data"

    def handle(self, *args, **options):
        self.stdout.write("start insert drain location data!")

        drain_file_path = os.path.join(BASE_DIR, "res", "location", "drain_code.csv")

        drain_df = pd.read_csv(drain_file_path)

        for drain_row in drain_df.itertuples():
            drain_row_dict = drain_row._asdict()
            gu_code = drain_row_dict.get("구분코드")
            di = {
                "gu": Gu.objects.get(drain_gu_code=gu_code),
                "location_info": drain_row_dict.get("위치정보"),
                "location_code": drain_row_dict.get("고유번호")
            }
            location_objects = Location(**di)
            location_objects.save()
