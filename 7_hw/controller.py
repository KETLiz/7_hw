# сборка проекта

import view
import model
import logger

def buttom_click():
    choose_num = view.choose_add_or_search()
    if choose_num == 1:
        name = model.add_contact()
        logger.write(*name)
    elif choose_num == 2:
        name = view.contact_to_s()
        base = logger.get_base()
        result = model.search_contact(base, name)
        view.search(result)
