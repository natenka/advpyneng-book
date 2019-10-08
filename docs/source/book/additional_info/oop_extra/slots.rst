Атрибут __slots__
-----------------


Пример кода из модуля `ipaddress <https://github.com/python/cpython/blob/3.7/Lib/ipaddress.py#L385>`__

.. code:: python

    class _IPAddressBase:

        """The mother class."""

        __slots__ = ()

        @property
        def exploded(self):
            """Return the longhand version of the IP address as a string."""
            return self._explode_shorthand_ip_string()

        @property
        def compressed(self):
            """Return the shorthand version of the IP address as a string."""
            return str(self)


    @functools.total_ordering
    class _BaseAddress(_IPAddressBase):

        """A generic IP object.
        This IP class contains the version independent methods which are
        used by single IP addresses.
        """

        __slots__ = ()

        def __int__(self):
            return self._ip

        def __eq__(self, other):
            try:
                return (self._ip == other._ip
                        and self._version == other._version)
            except AttributeError:
                return NotImplemented

        def __lt__(self, other):
            if not isinstance(other, _BaseAddress):
                return NotImplemented
            if self._version != other._version:
                raise TypeError('%s and %s are not of the same version' % (
                                 self, other))
            if self._ip != other._ip:
                return self._ip < other._ip
            return False

    class _BaseV4:

        """Base IPv4 object.
        The following methods are used by IPv4 objects in both single IP
        addresses and networks.
        """

        __slots__ = ()
        _version = 4
        # Equivalent to 255.255.255.255 or 32 bits of 1's.
        _ALL_ONES = (2**IPV4LENGTH) - 1
        _DECIMAL_DIGITS = frozenset('0123456789')

        # the valid octets for host and netmasks. only useful for IPv4.
        _valid_mask_octets = frozenset({255, 254, 252, 248, 240, 224, 192, 128, 0})

        _max_prefixlen = IPV4LENGTH
        # There are only a handful of valid v4 netmasks, so we cache them all
        # when constructed (see _make_netmask()).
        _netmask_cache = {}

        def _explode_shorthand_ip_string(self):
            return str(self)


    class IPv4Address(_BaseV4, _BaseAddress):

        """Represent and manipulate single IPv4 Addresses."""

        __slots__ = ('_ip', '__weakref__')

        def __init__(self, address):

            """
            Args:
                address: A string or integer representing the IP
                  Additionally, an integer can be passed, so
                  IPv4Address('192.0.2.1') == IPv4Address(3221225985).
                  or, more generally
                  IPv4Address(int(IPv4Address('192.0.2.1'))) ==
                    IPv4Address('192.0.2.1')
            Raises:
                AddressValueError: If ipaddress isn't a valid IPv4 address.
            """
