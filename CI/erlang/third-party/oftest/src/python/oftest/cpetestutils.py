import packet as scapy

global skipped_test_count
skipped_test_count = 0

_import_blacklist = set(locals().keys())

# Some useful defines
IP_ETHERTYPE = 0x800
TCP_PROTOCOL = 0x6
UDP_PROTOCOL = 0x11

MINSIZE = 0


def simple_pppoe_packet(pktlen=100,
                        eth_dst='00:0c:29:eb:57:12',
                        eth_src='00:0c:29:eb:57:fe',
                        pppoe_ver=1,
                        pppoe_type=1,
                        pppoe_sessionid=0x0030,
                        ip_src='192.168.22.2',
                        ip_dst='192.168.22.1',
                        ip_tos=0,
                        ip_ttl=64,
                        tcp_sport=1234,
                        tcp_dport=80,
                        tcp_flags="S",
                        ip_ihl=None,
                        ):
    """
    Return a simple dataplane TCP packet

    Supports a few parameters:
    @param len Length of packet in bytes w/o CRC
    @param eth_dst Destinatino MAC
    @param eth_src Source MAC
    @param pppoe_ver version of pppoe in bit 1 or 4
    @param pppoe_type type of pppoe in bit 1 or 4
    @param pppoe_sessionid session id of pppoe
    @param ip_src IP source
    @param ip_dst IP destination
    @param ip_tos IP ToS
    @param ip_ttl IP TTL
    @param tcp_dport TCP destination port
    @param tcp_sport TCP source port
    @param tcp_flags TCP Control flags

    Generates a simple TCP request.  Users
    shouldn't assume anything about this packet other than that
    it is a valid ethernet/PPPOE/PPP/IP/TCP frame.
    """

    if MINSIZE > pktlen:
        pktlen = MINSIZE

    pkt = scapy.Ether(dst=eth_dst, src=eth_src)/ \
          scapy.PPPOE(version=pppoe_ver, type=pppoe_type, sessionid=pppoe_sessionid)/ \
          scapy.PPP(proto=0x0021)/ \
          scapy.IP(src=ip_src, dst=ip_dst, tos=ip_tos, ttl=ip_ttl, ihl=ip_ihl)/ \
          scapy.TCP(sport=tcp_sport, dport=tcp_dport, flags=tcp_flags)

    pkt = pkt/("D" * (pktlen - len(pkt)))

    return pkt

def icmp_pppoe_packet(pktlen=106,
                      eth_dst='00:0c:29:eb:57:12',
                      eth_src='00:0c:29:eb:57:fe',
                      pppoe_ver=1,
                      pppoe_type=1,
                      pppoe_sessionid=0x0030,
                      ip_src='192.168.22.2',
                      ip_dst='114.114.114.114',
                      ip_tos=0,
                      ip_ttl=64,
                      ip_id=1,
                      icmp_type=8,
                      icmp_code=0,
                      icmp_data=''):
    """
    Return a simple ICMP packet

    Supports a few parameters:
    @param len Length of packet in bytes w/o CRC
    @param eth_dst Destinatino MAC
    @param eth_src Source MAC
    @param pppoe_ver version of pppoe in bit 1 or 4
    @param pppoe_type type of pppoe in bit 1 or 4
    @param pppoe_sessionid session id of pppoe
    @param ip_src IP source
    @param ip_dst IP destination
    @param ip_tos IP ToS
    @param ip_ttl IP TTL
    @param ip_id IP Identification
    @param icmp_type ICMP type
    @param icmp_code ICMP code
    @param icmp_data ICMP data

    Generates a simple ICMP ECHO REQUEST.  Users
    shouldn't assume anything about this packet other than that
    it is a valid ethernet/ICMP frame.
    """

    if MINSIZE > pktlen:
        pktlen = MINSIZE

    pkt = scapy.Ether(dst=eth_dst, src=eth_src, type=0x8864)/ \
          scapy.PPPOE(version=pppoe_ver, type=pppoe_type, sessionid=pppoe_sessionid) / \
          scapy.PPP(proto=0x0021) / \
          scapy.IP(src=ip_src, dst=ip_dst, ttl=ip_ttl, tos=ip_tos, id=ip_id)/ \
          scapy.ICMP(type=icmp_type, code=icmp_code) / icmp_data

    pkt = pkt/("0" * (pktlen - len(pkt)))

    return pkt
