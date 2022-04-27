```
Download the packet capture file and use packet analysis software to find the flag.
Download packet capture
```

```
strings network-dump.flag.pcap | tr -d ' ' | grep "pico"  
picoCTF{p4ck37_5h4rk_b9d53765}
```