#GLOBAL PAGINATION CAN BE SPECIFIED AT SETTINGS.PY FROM LINES 74 TO 79

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


#three types of pagination:
#1.PageNumberPagination
#2.LimitOffsetPagination(from ,upto)
#3.CursorPagination (orders the page based on logic)

class EmployeePagination(PageNumberPagination):
    page_size=12  #no of items to be displayed

    page_query_param='pageno' #this the query string specified after http://127.0.0.1:8000/api/ i.e http://127.0.0.1:8000/api/?pageno=4....default is page.

    page_size_query_param='num' # per page how many items to be displayed... http://127.0.0.1:8000/api/?num=20&pageno=13

    max_page_size=20 #you can request only 20 pages if not it will display only 20

    last_page_strings=['end']  # displays last page...http://127.0.0.1:8000/api/?pageno=end  ...default is last



class EmployeePagination1(LimitOffsetPagination): #how many items(limit)..from which index (offset)
    pass # the default offset and limit values are PAGE_SIZE defined in settings.py
    default_limit=20 # http://127.0.0.1:8000/api/?offset=56..you dont need to specify limit
    
    limit_query_param='mylimit' #http://127.0.0.1:8000/api/?myoffset=1&mylimit=45

    offset_query_param='myparam'
    max_limit=30    

class EmployeePagination2(CursorPagination): #fetch records based on employee attribute i.e ascending order of emp sal
    #ordering='empsal' # fetch emp sal in ascending order
    ordering='-empid' #fetch emp sal in descending order  http://127.0.0.1:8000/api/
    page_size=5


#############
#DJANGO FILTERING AND SEARCHING
####################
# 2 types of filtering
#1.Plain vanilla filtering
# -->you need to override "get_queryset" method and you need to implement the filter manually/


#2.Djago rest framwork filtering


class EmployeeFilteringandsearching(PageNumberPagination):
    page_size=20
    page_query_param='mypage'



