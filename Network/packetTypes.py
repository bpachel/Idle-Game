from enum import Enum

class PacketType(Enum):
    MESSAGE             = 1
    PING                = 2
    LOGIN               = 3
    REGISTER            = 4
    GET_STATS           = 5
    GET_ITEMS           = 6
    GET_ITEM_INFO       = 7
    SAVE_STATS          = 8
    SAVE_ITEMS          = 9
    LOGOUT               = 10