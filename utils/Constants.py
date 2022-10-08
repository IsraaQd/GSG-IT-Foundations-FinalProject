class Constants:
    # employment_type
    FULL_TIME = True
    PART_TIME = False

    # order_status
    ACTIVE_ORDER = 1
    EXPIRED_ORDER = 2
    CANCELED_ORDER = 3

    # book_status
    ACTIVE_BOOK = True
    INACTIVE_BOOK = False


class App_Utils:

    @staticmethod
    def check_value_if_empty(*value: str):
        for item in value:
            if item.isspace() or item == "":
                return True
