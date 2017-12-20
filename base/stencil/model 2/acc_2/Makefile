
SHELL=/bin/sh

# FILE
TARGET = life
EXT = .c

# GNU Compiler flags
# COMPILER = gcc
# CFLAGS = -O3
# CFLAGS = -O3 -fopenmp

# PGI Compiler flags
COMPILER = pgc++
# CFLAGS = -O3
# CFLAGS = -O3 -mp
# CFLAGS = -O3 -acc -ta=tesla:cc30,time -Minfo=all
# CFLAGS = -O3 -acc -ta=tesla:cc30
CFLAGS = -O3 -acc -ta=tesla:cc30

# Debug parameters
DGENERATIONS = 100
DGRID_SIZE = 1000


# Test parameters
GENERATIONS = 100
GRID_SIZES = 250 500 750 1000 1250 1500 2000 3000
# GRID_SIZES = 250
ITERATIONS = 1 2 3


compile:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) $(CFLAGS) -D Generations=$(DGENERATIONS) -D N=$(DGRID_SIZE)

run: clean compile
	./$(TARGET)

run_test: clean
	@date | tee Time.txt
	@echo "\nRowDim \t ColDim \t Status \t T.Real(sg) \t T.Usuario(sg) \t T.Kernel(sg) \t CPU \t Memoria(KB)" | tee -a Time.txt; \

	@for size in $(GRID_SIZES); do \
		$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) $(CFLAGS) -D Generations=$(GENERATIONS) -D N=$$size; \
		for iteration in $(ITERATIONS); do \
			/usr/bin/time -f "%e \t %U \t %S \t %P \t %M" ./$(TARGET)  2>&1 | tee -a Time.txt; \
		done;\
	done 

# This feature do not work in the pgicontainer 
# it need the nvidia-settings that comes with 
# the nvidia driver that is not present into the container.
device_top:
	@watch ../../utils/gpumonitor.sh

clean:
	@clear
	rm -f $(TARGET) *.txt *.dat