from django.core.management.base import BaseCommand
import csv
import uuid

from gocheap.models import Company, Drivers, Trips


class Command(BaseCommand):
    help = "Load CSV data (no headers, ; delimiter, UTF-8 BOM supported)"

    def handle(self, *args, **kwargs):

        # ========= COMPANY =========
        # CSV format: CompanyName ; CompanyID
        with open('data/Company.csv', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if not row:
                    continue

                Company.objects.get_or_create(
                    CompanyID=int(row[1]),
                    defaults={
                        'CompanyName': row[0]
                    }
                )

        self.stdout.write("✔ Company loaded")

        # ========= DRIVERS =========
        # CSV format: DriverID ; CompanyID ; Name ; Phone ; CarModel
        with open('data/Drivers.csv', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if not row:
                    continue

                Drivers.objects.get_or_create(
                    DriverID=int(row[0]),
                    defaults={
                        'Company': Company.objects.get(CompanyID=int(row[1])),
                        'Name': row[2],
                        'Phone': row[3],
                        'CarModel': row[4]
                    }
                )

        self.stdout.write("✔ Drivers loaded")

        # ========= TRIPS =========
        # CSV format:
        # TripID ; DriverID ; CompanyID ; Pickup ; Dropoff ; Distance ; Price ; Duration
        with open('data/Trips.csv', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if not row:
                    continue

                Trips.objects.get_or_create(
                    TripID=uuid.UUID(row[0]),
                    defaults={
                        'Driver': Drivers.objects.get(DriverID=int(row[1])),
                        'Company': Company.objects.get(CompanyID=int(row[2])),
                        'PickupArea': row[3],
                        'DropoffArea': row[4],
                        'DistanceKM': float(row[5]),
                        'Price': float(row[6]),
                        'TripDurationMin': int(row[7]),
                    }
                )

        self.stdout.write(self.style.SUCCESS("\n🎉 CSV DATA LOADED SUCCESSFULLY"))