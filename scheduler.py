from backend.calendar_service import get_calendar


def get_slots():

    user1=get_calendar("user1@gmail.com")

    user2=get_calendar("user2@gmail.com")


    common=set(user1).intersection(set(user2))


    slots=[]


    for c in common:


        slot={

        "date":"2026-03-10",

        "start":c+":00",

        "end":str(int(c)+1)+":00"

        }


        # Morning preference AI

        if int(c)<12:

            slot["score"]=10

        else:

            slot["score"]=5


        # Participant overlap

        slot["participants"]=2


        slots.append(slot)



    return sorted(slots,key=lambda x:-x["score"])