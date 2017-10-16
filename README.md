Rancher Upgrader
================

Code | https://github.com/cr0hn/rancher-upgrader
---- | ----------------------------------------------
Issues | https://github.com/cr0hn/rancher-upgrader/issues
Python version | Python 3.5 or above
Author | Daniel García (cr0hn) - @ggdaniel
Last version | 1.0.0

*The script needs Python 3 (really I don't test it in Python 2)*

Briefing
========

This project try to solve the problem of upgrading Rancher stack services without the need of using the UI.

Why
===

Because one of the most useful thinks of a PaaS is to automate the deployment process thought your C.I. system.

With this script you can do that. 

Installation
============

Installation process is so easy:

```bash

> python3 -m pip install rancher_upgrader
```

Usage
=====

The script is self-explained, to get help, only use *-h* option:

```bash

> rancher-upgrader -h

usage: rancher-upgrader.py [-h] -n STACK_NAME -s SERVICE_NAME -i NEW_IMAGE -u
                           RANCHER_URL -a RANCHER_ACCESS_KEY -k
                           RANCHER_SECRET_KEY [--retires MAX_RETRIES]
                           [--sleep]

Rancher service upgrader

optional arguments:
  -h, --help            show this help message and exit
  -n STACK_NAME         stack name.
  -s SERVICE_NAME       service name
  -i NEW_IMAGE          new docker image to push in the service
  -u RANCHER_URL        rancher portal url
  -a RANCHER_ACCESS_KEY
                        rancher secret key
  -k RANCHER_SECRET_KEY
                        rancher access key

Extra options:
  --retires MAX_RETRIES
                        maximum number of retries to check upgrade process
  --sleep               sleep time while checking upgrading process
```

Important things
================

- Rancher upgrader will try to upgrade a specific service of a stack
- If the upgrade fails, automatically It will do a rollback
- Rancher upgrader will do the complete upgrade process, including the confirmation of the upgrade process when the upgrading process was finished


License
=======

This project is distributed under [BSD clausule 3](<https://github.com/cr0hn/rancher_upgrader/blob/master/LICENSE)


