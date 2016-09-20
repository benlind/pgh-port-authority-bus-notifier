# Bus Notifier for the Pittsburgh Port Authority

This script monitors the Port Authority tracking website for the Thackeray stop at the University of Pittsburgh. When a bus on the passed <buses> list appears on the schedule, the user will be notified with an alert.

## Usage

```
bus.py [-h] [-d {OUTBOUND,INBOUND}] [buses [buses ...]]

positional arguments:
  buses                 buses to watch for

optional arguments:
  -h, --help            show this help message and exit
  -d {OUTBOUND,INBOUND}, --direction {OUTBOUND,INBOUND}
                        direction the bus will travel
```
