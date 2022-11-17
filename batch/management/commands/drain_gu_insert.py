import os
import pandas as pd

from apiserver.models import SeoulGu as Gu
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "insert drain gu data"

    def handle(self, *args, **options):
        self.stdout.write("start insert drain gu data!")

        drain_file_path = os.path.join(BASE_DIR, "res", "gu", "drain_gu.csv")

        drain_df = pd.read_csv(drain_file_path)

        for drain_row in drain_df.itertuples():
            drain_row_dict = drain_row._asdict()

            di = {
                "name": drain_row_dict.get("구분명") + "구",
                "drain_gu_code": drain_row_dict.get("구분코드"),
            }
            gu_objects = Gu.objects.get(name=di["name"])
            gu_objects.drain_gu_code = di["drain_gu_code"]
            gu_objects.save()
