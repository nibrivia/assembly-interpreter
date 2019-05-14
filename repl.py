from imp import reload
import assembly

def r_to_i(r):
    if isinstance(r, int):
        return r
    if isinstance(r, str):
        return int(r.replace("R", ""))
    else:
        raise

class RegFile:
    def __init__(self):
        self.regs = [0 for i in range(32)]

    def __getitem__(self, r):
        i = r_to_i(r)
        if i == 31:
            return 0
        else:
            return self.regs[i]

    def __setitem__(self, r, val):
        i = r_to_i(r)
        assert isinstance(val, int)
        self.regs[i] = val

    def __iter__(self):
        for i in range(32):
            yield self[i]

    def __str__(self):
        return "\n".join(["R" + str(i) + ": " + str(val) for i, val in enumerate(self)])

class Memory:
    def __init__(self, log_size = 10):
        self.mem = dict()
        self.size = 2**log_size

    def __getitem__(self, addr):
        assert isinstance(addr, int)
        assert addr < self.size

        return self.mem.get(addr, 0)

    def __setitem__(self, addr, val):
        assert isinstance(addr, int)
        assert addr < self.size

        assert isinstance(val, int)

        self.mem[addr] = val

    def __iter__(self):
        for addr, val in sorted((addr, val) for addr, val in self.mem.items()):
            yield (addr, val)

memory = Memory()
regs   = RegFile()

while True:
    cmd = input("> ")
    if cmd in ["quit", "exit"]: break

    reload(assembly)
    res = assembly.run(cmd, regs = regs, memory = memory)

    if res is not None:
        print(res)


