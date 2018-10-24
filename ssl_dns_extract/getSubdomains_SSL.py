#!/usr/bin/env python3
import json
import socket
import ssl
import sys


def getcert(addr, timeout=None):
    with socket.create_connection(addr, timeout=timeout) as sock:
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname=addr[0]) as sslsock:
            return sslsock.getpeercert()


def main(argv):
    host = argv[1]
    port = int(argv[2]) if len(argv) > 2 else 443
    print(json.dumps(getcert((host, port)), indent=2, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv)
