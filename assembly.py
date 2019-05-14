memory = dict()

def unknown_op(tokens, regs, mem):
    return "unknown op: " + " ".join(tokens)

def add(tokens, regs, mem):
    assert len(tokens) == 4

    rd, rsa, rsb = tokens[1:]
    regs[rd] = regs[rsa] + regs[rsb]

def add_c(tokens, regs, mem):
    assert len(tokens) == 4

    rd, rsa, const = tokens[1:]
    regs[rd] = regs[rsa] + int(const)

def load(tokens, regs, mem):
    assert len(tokens) == 4

    rd, rsa, offset = tokens[1:]
    ea = regs[rsa] + int(offset)
    regs[rd] = mem[ea]

def store(tokens, regs, mem):
    assert len(tokens) == 4

    rsrc, raddr, offset = tokens[1:]
    ea = regs[raddr] + int(offset)
    mem[ea] = regs[rsrc]


from collections import defaultdict
op_dict = defaultdict(lambda: unknown_op)
op_dict["ADD"]  = add
op_dict["ADDC"] = add_c
op_dict["LD"]   = load
op_dict["ST"]   = store

def run(cmd, regs, memory):

    if cmd in ["_regs", "ls"]:
        return str(regs)

    if cmd == "_mem":
        for addr, val in memory:
            print((addr, val))
        return

    tokens = cmd.split()
    op = tokens[0]

    return op_dict[op](tokens, regs = regs, mem = memory)

