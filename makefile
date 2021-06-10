SRC_DIR = ../src/

All: FastPID.o
	gcc -shared -o libFastPID.so FastPID.o
	
FastPID.o: $(SRC_DIR)FastPID.c	
	gcc -c -Wall -Werror -fpic $(SRC_DIR)FastPID.c