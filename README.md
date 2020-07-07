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


# Usage in Linux:

```console
user@guanaco:~$ git clone https://github.com/achauque/xPL-printclient.git

user@guanaco:~$ cd xPL-printclient/linux
user@guanaco:~/xPL-printclient/linux$ python xPL-printclient IP_ADDRESS PORT PRINT_PORT
```

<strong>example:</strong> <br>
First check privilege to write device (/dev/usb/lp0)
```console
user@guanaco:~/xPL-printclient/linux$ python xPL-printclient 127.0.0.1 9100 /dev/usb/lp0
```