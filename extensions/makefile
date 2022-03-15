#############################################################
# Compile hello.c into a shareable object file on Cygwin,
# to be loaded dynamically when first imported by Python.
#############################################################

PYLIB = /usr/include/x86_64-linux-gnu/python3.8
PYINC = /usr/include/python3.8

hello.so: hello.c
	gcc hello.c -g -I$(PYINC) -shared -L$(PYLIB) -lpython3.8 -o hello.so
clean:
	rm -f hello.so core

