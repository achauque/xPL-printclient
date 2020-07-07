# xPL-printclient
This module is a interface for xPL-printserver.

# Usage in Windows:

```console
c:\xPL-printclient\LPT\python xPL-printclient IP_ADDRESS PORT PRINT_PORT
```
<strong>example:</strong> <br>

```console
c:\xPL-printclient\LPT\python xPL-printclient 127.0.0.1 9100 LPT1
```

<strong>USB to LPT:</strong> <br>
Firs step: share print in control panel.

```console
c:\NET USE LPT1 \\localhost\shared_printer /PERSISTENT:YES
```
