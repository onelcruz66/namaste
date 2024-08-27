

from .models import TimeSlots
from django.shortcuts import redirect

# label_to_field = {
#     '9:00': 'nine',
#     '10:00': 'ten',
#     '11:00': 'eleven',
#     '12:00': 'twelve',
#     '1:00': 'one',
#     '2:00': 'two',
#     '3:00': 'three',
#     '4:00': 'four',
#     '5:00': 'five'
# }

def handlePostRequestForNewTimeSlot(request, lastAppointment):
    try:

        new_time_slot_record = TimeSlots(
            date = lastAppointment.date,
            hour_selected = request.POST.get('hour_selected')
        )
        new_time_slot_record.save()
        time_slot = new_time_slot_record.hour_selected
        subtractTimeSlotFromDb(new_time_slot_record, time_slot)
        return redirect('payment')
    except Exception as e:
        print(f'Error while setting time slot: {e}')
        print("time_slot:", time_slot)


def handlePostRequestForExistingTimeSlot(request, timeSlotObject):

    try:
        time_slot = request.POST.get('hour_selected')
        subtractTimeSlotFromDb(timeSlotObject, time_slot)
        
        return redirect('payment')
    except Exception as e:
        print(e)
        print("time_slot:", time_slot)


def subtractTimeSlotFromDb(dbObject, time_slot):
    if time_slot == '9:00' and dbObject.nine != 0:
        dbObject.nine = dbObject.nine - 1
        dbObject.save()
        return
    elif time_slot == '10:00' and dbObject.ten != 0:
        dbObject.ten = dbObject.ten - 1
        dbObject.save()
        return
    elif time_slot == '11:00' and dbObject.eleven != 0:
        dbObject.eleven = dbObject.eleven - 1
        dbObject.save()
        return
    elif time_slot == '12:00' and dbObject.twelve != 0:
        dbObject.twelve = dbObject.twelve - 1
        dbObject.save()
        return
    elif time_slot == '1:00' and dbObject.one != 0:
        dbObject.one = dbObject.one - 1
        dbObject.save()
        return
    elif time_slot == '2:00' and dbObject.two != 0:
        dbObject.two = dbObject.two - 1
        dbObject.save()
        return
    elif time_slot == '3:00' and dbObject.three != 0:
        dbObject.three = dbObject.three - 1
        dbObject.save()
        return
    elif time_slot == '4:00' and dbObject.four != 0:
        dbObject.four = dbObject.four - 1
        dbObject.save()
        return
    elif time_slot == '5:00' and dbObject.five != 0:
        dbObject.five = dbObject.five - 1
        dbObject.save()
        return
    else:
        return