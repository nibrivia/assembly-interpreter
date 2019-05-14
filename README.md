# assembly-interpreter
A python-based assembly interpreter for teaching purposes

This is a start of an attempt to have a good "toy OS" for students to learn the basics of scheduling and such.

# Running it

Right now, there is a simple [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) you can run
with `python3 repl.py`. The currently supported operations are:

- `ADD`,
- `ADDC`,
- `LD`,
- `ST`.

In addition to assembly instructions, there are interpreter commands: 

 - `quit`, `exit`, which stop the interpreter,
 - `_regs` which prints all the registers,
 - `_mem` which prints all locations in memory that have been used.
 
Lemme know if you have any questions!


# Developing on the REPL

So REPL for assembly is only useful for simple programs (no branches), but it is very useful to debug and show
examples in. You can easily add instructions by adding new entries to the `op_dict` array. These changes can be 
made "live", the REPL forces python to reload new code. This is very useful for active development/demonstrations.
