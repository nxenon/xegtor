# Scripts

Scripts Usage
----
    sudo python3 xegtor.py --script script_name [arguments]

ARP Cache Poisoning
----
perform arp cache poisoning for MITM

`arp_spoof.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/arp_spoof.py)

Arguments:
- `--interface` interface name **(required)**
- `--target1` target 1 **(required)**
- `--target2` target 2 **(required)**

ARP Ping
----
scan hosts in network with ARP

`arp_ping.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/arp_ping.py)

Arguments:
- `--range` ip_range [e.g. 192.168.1.0/24] **(required)**
- `--timeout` secs (default 3.5)

ICMP Ping
----
scan hosts in network with ICMP

`icmp_ping.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/icmp_ping.py)

Arguments:
- `--range` ip_range [e.g. 192.168.1.0/24] **(required)**

Syn Flood
----
this script performs syn flood attack

`syn_flood.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/syn_flood.py)

Arguments:
- `--target` TARGET **(required)**
- `--port` PORT(S) [e.g. 80 or 80,22 or 80-90] **(required)**

# Port Scanners :
TCP Syn Port Scanner
----
this script performs port scanning with TCP (`syn `method)

`tcp_ps_syn.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/tcp_ps_syn.py)

Arguments:
- `--target` TARGET **(required)**
- `--port` PORT(S) [e.g. 80 or 80,22 or 80-90] **(required)**
- `--timeout` secs (default `0.1`)

TCP Ack Port Scanner
----
this script performs port scanning with TCP (`ack `method).
- scan port states
- `stateful` firewall detection

`tcp_ps_ack.py` [Link](https://github.com/xegtor/xegtor/blob/master/scripts/tcp_ps_ack.py)

Arguments:
- `--target` TARGET **(required)**
- `--port` PORT(S) [e.g. 80 or 80,22 or 80-90] **(required)**
- `--timeout` secs (default `1.0`)

# Examples
- [Scripts Examples File](https://github.com/xegtor/xegtor/blob/master/scripts/examples.txt)