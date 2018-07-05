#!/usr/bin/env python

import os
from datetime import datetime
import sys
import json
import csv
import requests


    pxgrid = input("What is the FQDN of the ISE PxGrid API Server? ")
    pxgrid_user = input("What user will the script be using? ")
    pxgrid_pass = input("What is the password? ")
    print("We'll be connecting to {} with username {} and password {}.".format(str(pxgrid),str(pxgrid_user),str(pxgrid_pass)))

if __name__ == '__main__':
