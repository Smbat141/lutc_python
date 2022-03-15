#!/usr/bin/python3
"""
################################################################################
On 'send' click in main root window: display composition page
################################################################################
"""
import commonhtml, os, sys
from externs import mailconfig

commonhtml.editpage(kind='Write', headers={'From': mailconfig.myaddress})
