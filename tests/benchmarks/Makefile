BENCHMARKS = \
	 helloworld \
	 write_1e4 \
	 write_1e5 \
	 write_1e6 \
	 write_1e7
GRAPHENEDIR = $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)

all: $(BENCHMARKS)

$(filter write_%,$(BENCHMARKS)): %: write_pages.c
	$(CC) $(CFLAGS) $< -o $@
write_1e4 : CFLAGS += -DPAGECOUNT=10000
write_1e5 : CFLAGS += -DPAGECOUNT=100000
write_1e6 : CFLAGS += -DPAGECOUNT=1000000
write_1e7 : CFLAGS += -DPAGECOUNT=10000000

.PHONY: clean
clean:
	$(RM) $(BENCHMARKS)
