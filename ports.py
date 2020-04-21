import sqlite3
from werkzeug.security import safe_str_cmp


class Port:
    def __init__(self, id, NmapVersion, IpStatus, OpenPorts, networkIp):
        self.id = id
        self.networkIp = networkIp
        self.NmapVersion = NmapVersion
        self.IpStatus = IpStatus
        self.OpenPorts = OpenPorts


@classmethod
def find_by_ip(cls, networkIp):
    connection = sqlite3.connect()
    cursor = connection.cursor()
    query = "SELECT * FROM ports Where networkIp=?"
    result = cursor.execute(query, (networkIp,))
    row = result.fetchone()
    if row:
        find_by_ip = cls(*row)
    else:
        find_by_ip = None

        connection.close()
        return find_by_ip

    from ports import Port


networkIp_mapping = {u.networkIp: u for u in Port}


def authenticate(networkIp):
    ports = Port.find_by_ip(networkIp)
    if ports and safe_str_cmp(ports.networkIp):
        return ports
