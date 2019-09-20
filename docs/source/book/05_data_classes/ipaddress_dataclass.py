from dataclasses import asdict, astuple, replace, dataclass, field

@dataclass(order=True, frozen=True)
class IPAddress:
    ip: str
    mask: int = 24


if __name__ == "__main__":
    ip1 = IPAddress('10.1.1.1', 28)
    ip2 = IPAddress('10.2.2.1', 28)
    ip3 = IPAddress('10.3.3.1', 28)
    ip4 = IPAddress('10.4.4.1', 28)
    ip_list = [ip3, ip2, ip1, ip4]
    print(sorted(ip_list))

