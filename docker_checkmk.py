#!/usr/bin/python

import json
from docker import Client
import subprocess
import re

cli = Client(base_url='unix:///var/lib/docker/socketfile')
containers = cli.containers()


for i in range(len(containers)):
     c = containers[i]
     c_name = json.dumps(c.values()[-2])
     NAME = ''.join(re.split(r'[\["\]\'\/]', c_name))
     p = subprocess.Popen(["docker", "top", NAME, "aux"], stdout=subprocess.PIPE)
     out = p.stdout.read()
     memory = json.dumps(out).split()[13]
     if ( int(float(memory)) <= 75 ): print "0 %sMemory count=%s;75;90;0;100 OK - %s Memory used %s%%" %(NAME,memory,NAME,memory)
     if ( int(float(memory)) >= 75 ) and ( memory <= 85 ): print "1 %sMemory count=%s;75;90;0;100 Warning - %s Memory used %s%%" %(NAME,memory,NAME,memory)
     if ( int(float(memory)) >= 85 ) and ( memory <=100 ): print "2 %sMemory count=%s;75;90;0;100 Critical - %s Memory used %s%%" %(NAME.memory,NAME,memory)
     cpu = json.dumps(out).split()[12]
     if ( int(float(cpu)) <= 75 ): print "0 %sCPU count=%s;75;90;0;100 OK - %s CPU used %s%%" %(NAME,cpu,NAME,cpu)
     if ( int(float(cpu)) >= 75 ) and ( cpu <= 85 ): print "1 %sCPU count=%s;75;90;0;100 Warning - %s CPU  used %s%%" %(NAME,cpu,NAME,cpu)
     if ( int(float(cpu)) >= 85 ) and ( cpu <=100 ): print "2 %sCPU count=%s;75;90;0;100 Critical - %s CPU used %s%%" %(NAME,cpu,NAME,cpu)
