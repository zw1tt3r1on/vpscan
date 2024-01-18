# vpscan
vpscan is a simple scanner to detect unauthenticated varnish cache purge issues

# Requirements
vpscan uses python 3 and does not need any additional dependencies 

# Usage
vpscan can be used to check for a single domain
```
vpscan.py -d sampledomain.com
[VULNERABLE] sampledomain.com
```

It also supports inputs from a list of domains from a text file
```
vpscan.py -l sample_list.txt
[NOT VULNERABLE] domain1.com
[NOT VULNERABLE] domain2.com
[NOT VULNERABLE] domain3.com
[VULNERABLE] domain4.com
```

### Support my projects 
![](https://github.com/zw1tt3r1on/RDRD/assets/64955404/8ebb3761-a320-4343-8f63-7e0d1a3eb964)
https://www.buymeacoffee.com/zw1tt3r1on
