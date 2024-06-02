import random
from datetime import datetime
from apps.cabinets.factories import CabinetFactory
from apps.cabinets.models import Cabinet
from apps.doctors.factories import DoctorFactory
from apps.doctors.models import Doctor
from apps.intervals.models import Interval
from apps.schedule.factories import ScheduleFactory
from apps.schedule.models import Schedule


def generate_random_data_for_intervals(n=10, days=1717339746):
    """
    Generate random data for testing.
    """
    schedule = ScheduleFactory()
    doctors = Doctor.objects.all()

    for i in range(n):
        time = random.randint(days, days + 24 * 60 *60 * 7)
        Interval.objects.create(
            schedule=schedule,
            doctor=random.choice(doctors),
            start=datetime.fromtimestamp(time),
            end=datetime.fromtimestamp(time + random.randint(60 * 60, 60 * 60 * 7)),
        )
    

def generate_random_data_for_doctors(n=10):
    """
    Generate random data for testing.
    """
    
    cabinets = Cabinet.objects.all()

    if cabinets.count() < 5:
        return False
    
    for i in range(n):
        random_cabinets = random.sample(list(cabinets), random.randint(2,5))
        random_cabinet = random.choice(random_cabinets)
        doctor = DoctorFactory(priority_cabinet=random_cabinet)
        doctor.cabinets.add(*random_cabinets)
    
    return True


def generate_random_data_for_cabinets(n=10):
    """
    Generate random data for testing.
    """
    for i in range(n):
        cabinet = CabinetFactory()
        cabinet.number = str(random.randint(1, 1000))
        cabinet.save()
        
    return True


def remove_all_data():
    """
    Remove all data.
    """
    Interval.objects.all().delete()
    Doctor.objects.all().delete()
    Cabinet.objects.all().delete()
    Schedule.objects.all().delete()

    return True
