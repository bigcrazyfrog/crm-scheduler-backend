from apps.doctors.models import Doctor
from apps.intervals.models import Interval


def make_schedule(
    doctors: list[Doctor],
    intervals: list[Interval],
) -> list[Interval]:
    """Без комментариев просто это что."""
    
    for interval in intervals:
        if interval.cabinet is not None:
            continue
        
        doctor = interval.doctor
        avaliable_cabinets = {}
        for cabinet in doctor.cabinets.all():
            avaliable_cabinets[cabinet] = True

        for interval2 in intervals:
            if interval2.cabinet is None:
                continue
                                                
            if (
                interval2.start <= interval.start < interval2.end or 
                interval2.start < interval.end <= interval2.end
            ):
                avaliable_cabinets[interval2.cabinet] = False

        for cabinet, avaliable in avaliable_cabinets.items():
            if avaliable:
                interval.cabinet = cabinet
                interval.save()
                break


def shedule() -> list[Interval]:
    """Код будет тут, примеры данных ниже."""
    doctors = Doctor.objects.all()
    intervals = Interval.objects.all()

    make_schedule(doctors, intervals)
