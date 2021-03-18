"""# 8 task: задачи с сайта https://acmp.ru   """
"""Для заезда в оздоровительный лагерь организаторы решили заказать автобусы.
Известно, что в лагерь собираются поехать N детей и M взрослых. 
Каждый автобус вмещает K человек. 
В каждом автобусе, в котором поедут дети, должно быть не менее двух взрослых.
Определите, удастся ли отправить в лагерь всех детей и взрослых, и если да, 
то какое минимальное количество автобусов требуется для этого заказать.  """

child_num = 10
adult_num = 4
bus_capacity = 7
bus_quontity = 0
bus_child_free_place = 0

while child_num != 0:
    bus_child_free_place = bus_capacity - 2
    child_num = child_num - bus_child_free_place
    adult_num = adult_num - 2
    bus_quontity += 1
    if child_num < 0 <= adult_num:
        bus_quontity = 0
        break
    elif child_num <= 0 and adult_num <= 0:
        break
print(bus_quontity)
