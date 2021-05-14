from enum import Enum

class PacketType(Enum):
    """
        Unused
        Return None
        Arguments:
            n any type
    """
    MESSAGE             = 1

    """
        For Testing Connection
        Arguments:
            str 'ping'
        Return Packet
            str 'pong'
    """
    PING                = 2

    """
        Login to server
        Arguments:
            str 'username'
            str 'password'
        Return Packet
            int
                '0' - failed
                '1' - success
    """
    LOGIN               = 3

    """
        Register account
        Arguments:
            str 'username'
            str 'password'
            str 'email'
        Return Packet
            int
                '0' - failed
                '1' - success
    """
    REGISTER            = 4

    """
        Get User Stats
        [Must be logged in]
        Arguments:
            None
        Return Packet
            Decimal 'might'
            Decimal 'cunning'
            Decimal 'psyche'
            Decimal 'lore'
            Decimal `gold`
            Decimal `treasure`
            Decimal `might`
            Decimal `cunning`
            Decimal `psyche`
            Decimal `lore`
            Decimal `stamina`
            Decimal `health`
            Decimal `ploy`
            Decimal `spirit`
            Decimal `clarity`
    """
    GET_STATS           = 5
    
    """
        Get User Items
        [Must be logged in]
        Arguments:
            None
        Return Packet
            int 'n'
            (n times)
                int 'item_id'
    """
    GET_ITEMS           = 6

    """
        Get User Items
        [Must be logged in]
        Arguments:
            None
        Return Packet
            str 'name'
            str 'type'
            Decimal 'req_might'
            Decimal 'req_cunning'
            Decimal 'req_psyche'
            Decimal 'req_lore'
            Decimal 'might'
            Decimal 'cunning'
            Decimal 'psyche'
            Decimal 'lore'
    """
    GET_ITEM_INFO       = 7

    """
        Save Stats to Database
        Arguments:
            None
            [Must be logged in]
        Arguments:
            Decimal 'might'
            Decimal 'cunning'
            Decimal 'psyche'
            Decimal 'lore'
            Decimal `gold`
            Decimal `treasure`
            Decimal `might`
            Decimal `cunning`
            Decimal `psyche`
            Decimal `lore`
            Decimal `stamina`
            Decimal `health`
            Decimal `ploy`
            Decimal `spirit`
            Decimal `clarity`
        Return Packet
            int
                '0' - failed
                '1' - success
    """
    SAVE_STATS          = 8
    
    """
        Save Items to Database
        Arguments:
            None
            [Must be logged in]
        int 'n'
            (n times)
                str 'name'
                str 'type'
                Decimal 'req_might'
                Decimal 'req_cunning'
                Decimal 'req_psyche'
                Decimal 'req_lore'
                Decimal 'might'
                Decimal 'cunning'
                Decimal 'psyche'
                Decimal 'lore'
        Return Packet
            int
                '0' - failed
                '1' - success
    """
    SAVE_ITEMS          = 9

    """
        Logout from server
        Arguments:
            None
        Return Packet
            None
    """
    LOGOUT               = 10