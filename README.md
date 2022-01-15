# Speedtest
This is just a wrapper for [speedtest-cli](https://github.com/sivel/speedtest-cli) from sivel. 

Prerequisite:
- you use a linux system
- [speedtest-cli](https://github.com/sivel/speedtest-cli) installed

## Executing the script regularly
One way (maybe the best way) to run a speed test on a regular basis is setting up a cron job.

A cronjob executes shell script, so first of all create a shell script. Open a terminal and enter:
```console
$ nano speedtest.sh
```
Add those there lines and save the file:

```console
#!/bin/bash
source /home/pi/.bashrc
sudo python3 /home/pi/Python/SpeedTest.py 
```

The script must be executable:
```
$ chmod u+x speedtest.sh
```
 
 Now create a cron job for the current user

```console
$ crontab -e
```
Add the end of the file add a new line, e.g.:

```console
4 * * * * /home/pi/Python/speedtest.sh >> /home/pi/Python/cronlog.txt 2>&1

```
Such a cron job is execute hourly at 1:04, 2:04, 3:04,...
If you set this to 0 (1:00, 2:00, etc) speedtest.py won't find any servers. Very strange effect!

Make also sure that the current user is added to 
``/etc/cron.allow``
If the file does not exist, create it. Otherwise the cronjob is executed for user root and very likely this user has no authority to write to your local directories or files.
