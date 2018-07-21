import json, base64, sys, time, imp
import random, threading, os
from multiprocessing import Queue

from bitbucket.bitbucket import Bitbucket

trojan_id = "abc"

trojan_config = "%s.json" % trojan_id
data_path = 'data/%s/' % trojan_id
trojan_modules = []
configured = False
task_queue = Queue()