docker_checkmk
==============

Monitor Docker container CPU and Memory

Start
=====
* Start docker with following option either by passing this parameter over command line or by editing /etc/sysconfig/docker file.
	other_args="-H unix:///var/lib/docker/socketfile"

* I prefer to start docker socket api over remote api because of security reason.

How to user
===========
* Copy this file in check_mk local check directory (/usr/lib/check_mk_agent/plugins) 
* check the output by running check_mk_agent command.
<<<local>>>
0 containernameMemory count=29.4;75;90;0;100 OK - containername Memory used 29.4%
0 containernameCPU count=1.9;75;90;0;100 OK - containername CPU used 1.9%
* Check_mk will generate graph using these values.
