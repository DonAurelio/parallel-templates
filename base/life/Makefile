# FILE
TARGET = life
EXT = .c
COMPILER = gcc

# Test parameters
GENERATIONS=1000
GRID_SIZE=1000

compile:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=10

run: clean compile
	./$(TARGET)

compile_test:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=$(GENERATIONS) -D RowDim=$(GRID_SIZE) -D ColDim=$(GRID_SIZE)

run_test: clean compile_test
	./$(TARGET)

clean:
	rm -f $(TARGET) *.txt *.dat
	@clear


