from apps.doctors.models import Doctor
from apps.intervals.models import Interval


def make_schedule(
    doctors: list[Doctor],
    intervals: list[Interval],
) -> list[Interval]:
    """Моя кривая версия распредилениея кабинетов"""
    
    for interval in intervals: # идем по каждому интервалу
        if interval.cabinet is not None: # и проверяем, есть ли кабинет, если уже есть, то пропускаем
            continue
        
        doctor = interval.doctor
        avaliable_cabinets = {} # сюда складываем доступные для выбора кабинеты, в которых может принимать этот доктор, если кабинет доступен, то True
        for cabinet in doctor.cabinets.all(): # добавляем кабинеты в которых может принимать доктор в доступные кабинеты 
            avaliable_cabinets[cabinet] = True 

        for interval2 in intervals: # перебираем дугие интервалы на наличие пересечений с нашим интервалом
            if interval2.cabinet is None: # если кабинет не задан, пересечения нет
                continue
                                                
            if ( # проверка пересечение
                interval2.start <= interval.start < interval2.end or 
                interval2.start < interval.end <= interval2.end
            ):
                avaliable_cabinets[interval2.cabinet] = False # если наложение есть, то кабинет нельзя выбрать

        if doctor.priority_cabinet is not None and avaliable_cabinets[doctor.priority_cabinet]: 
            # если у врача есть приорететный кабинет и он доступен, выбираем его
            interval.cabinet = doctor.priority_cabinet
            interval.save()
        else:                                      
            # из доступных кабинетов выбираем первый доступный и записываем его в интервал
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

    у доктора есть атрибуты id, first_name, last_name, father_name, priority_cabinet, cabinets:
    обращаться к ним через точку:
    doctor.id - id доктора

    у кабинета это id, number, description, start, end. (start, end) - это время работы кабинета
    у интервала id, start, end, doctor, cabinet

    исключение!! список кабинетов для доктора - doctor.cabinets.all()
    
    перезаписать кабинет и сохранить интервал в бд:
    interval.cabinet = cabinet
    interval.save()

    """
