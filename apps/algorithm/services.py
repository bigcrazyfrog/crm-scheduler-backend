from apps.algorithm.test_data.service import *
from apps.doctors.models import Doctor
from apps.intervals.models import Interval


def make_schedule(
    doctors: list[Doctor],
    intervals: list[Interval],
) -> list[Interval]:
    """Моя кривая версия распредилениея кабинетов"""
    
    for interval in intervals: # идем по каждому интервалу
        # и проверяем, есть ли кабинет, если уже есть, то пропускаем
        if interval.cabinet is not None:
            continue
        
        doctor = interval.doctor
        # сюда складываем доступные для выбора кабинеты, в которых может принимать 
        # этот доктор, если кабинет доступен, то True
        avaliable_cabinets = {}
        # добавляем кабинеты в которых может принимать доктор
        # в доступные кабинеты 
        for cabinet in doctor.cabinets.all():
            avaliable_cabinets[cabinet] = True 

        # перебираем дугие интервалы на наличие пересечений с нашим интервалом
        for interval2 in intervals:
            if interval2.cabinet is None: # если кабинет не задан, пересечения нет
                continue

            if ( # проверка пересечение
                interval2.start <= interval.start < interval2.end or
                interval2.start < interval.end <= interval2.end
            ):
                # если наложение есть, то кабинет нельзя выбрать
                avaliable_cabinets[interval2.cabinet] = False

        if (
            doctor.priority_cabinet is not None 
            and avaliable_cabinets[doctor.priority_cabinet]
        ):
            # если у врача есть приорететный кабинет и он доступен, 
            # выбираем его
            interval.cabinet = doctor.priority_cabinet
            interval.save()
        else:                                      
            # из доступных кабинетов выбираем первый доступный 
            # и записываем его в интервал
            for cabinet, avaliable in avaliable_cabinets.items():
                if avaliable:
                    interval.cabinet = cabinet
                    interval.save()
                    break


def make_schedule_v2(
    doctors: list[Doctor],
    intervals: list[Interval],
) -> list[Interval]:
    """Версия вторая

    doctors - список докторов
    intervals - список интервалов

    --- это как списки в питоне ---
    doctors[0] - первый доктор и тд
    for doctor in doctors - перебор списка

    у доктора есть атрибуты
    id, first_name, last_name, father_name, priority_cabinet, cabinets:
    обращаться к ним через точку:
    doctor.id - id доктора

    у кабинета это id, number, description, start, end. (start, end)
    - это время работы кабинета
    у интервала id, start, end, doctor, cabinet

    исключение!! список кабинетов для доктора - doctor.cabinets.all()
    
    перезаписать кабинет и сохранить интервал в бд:
    interval.cabinet = cabinet
    interval.save()

    """
