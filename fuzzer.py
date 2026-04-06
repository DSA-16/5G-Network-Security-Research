#!/usr/bin/env python3
from boofuzz import *

def main():
    # Targeting the signaling node (AMF/Erlang)
    target_ip = "192.168.1.100"
    target_port = 11000 

    session = Session(
        target=Target(connection=TCPSocketConnection(target_ip, target_port)),
    )

    # Define the message structure [Length(4 bytes)][Type(1 byte)][Payload]
    s_initialize("signaling_msg")
    s_size("payload_len", length=4, fuzzable=True) 
    s_byte(0x01, name="msg_type", fuzzable=True)   
    s_string("AAAA", name="payload", fuzzable=True) 
    s_static("\x00\x00") 

    session.connect(s_get("signaling_msg"))
    session.fuzz()

if __name__ == "__main__":
    main()
