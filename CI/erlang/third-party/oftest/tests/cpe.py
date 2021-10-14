"""
Basic protocol and dataplane test cases

It is recommended that these definitions be kept in their own
namespace as different groups of tests will likely define
similar identifiers.

Current Assumptions:

  The switch is actively attempting to contact the controller at the address
indicated in oftest.config.

"""

import time
import sys
import logging

import unittest
import random

from oftest import config
import oftest.controller as controller
import oftest.dataplane as dataplane
import oftest.base_tests as base_tests
import ofp

import oftest.illegal_message as illegal_message

from oftest.testutils import *
from oftest.cpetestutils import *

TEST_VID_DEFAULT = 2


class PPPOE_LearnIP(base_tests.DataPlaneOnly):
    """
    Test CPE learn Wan IP when receive the PPPOE Packet in inner port
    """
    def runTest(self):
        # Need at least two ports
        self.assertTrue(len(config["port_map"]) > 1, "Too few ports for test")

        of_ports = config["port_map"].keys()
        of_ports.sort()
        d_port = of_ports[2]
        exp_port = of_ports[0]
        pkt = simple_pppoe_packet()

        logging.info("Wan Learn PPPOE IP  Test, send to port %s" % d_port)
        self.dataplane.send(d_port, str(pkt))

        (rcv_port, rcv_pkt, pkt_time) = self.dataplane.poll(port_number=exp_port, timeout=3, exp_pkt=None)
        self.assertTrue(rcv_pkt is not None, "Did not receive packet")
        logging.debug("Packet len " + str(len(rcv_pkt)) + " in on " +
                      str(rcv_port))
        logging.debug("Packet expect " + str(pkt))
        self.assertEqual(str(pkt), str(rcv_pkt), 'Response packet does not match send packet')
        (rcv_port, rcv_pkt, pkt_time) = self.dataplane.poll(port_number=exp_port, timeout=10, exp_pkt=None)
        self.assertTrue(rcv_pkt is not None, "Did not receive packet")
        rev_decode = inspect_packet(scapy.Ether(rcv_pkt))
        logging.debug("rcv packet " + rev_decode)
        self.assertTrue('icmp' in rev_decode and '192.168.22.2' in rev_decode)

if __name__ == "__main__":
    print "Please run through oft script:  ./oft --test_spec=cpe"
