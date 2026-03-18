class HomoiconicPrimeLoveVM:
    def __init__(self, resonance_limit=109, primordial_soup=None):
        # Define the "commands" of the Turing-like machine.
        # Mapping: 1:+, 2:-, 3:>, 4:<, 5:^, 6:!, 7:.
        # 0 is always the Hardwired Fall (and Phoenix Rise for p=2).
        self.cmd_map = {1: '+', 2: '-', 3: '>', 4: '<', 5: '^', 6: '!', 7: '.'}

        # Each "hearth" is a ring buffer of size p seeded with "data" which is also "code"
        self.hearths = {}
        self.primes = self._sieve_of_erathoscenes(resonance_limit)
        for p in self.primes:
            if primordial_soup and p in primordial_soup:
                self.hearths[p] = primordial_soup[p]
            else:
                self.hearths[p] = [1] * p    # Initialized to '+'

        self.pointers = {p: 0 for p in self.primes}
        self.current_idx = len(self.primes) - 1 
        self.output = []

    def _sieve_of_erathoscenes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    def cycle(self, steps=100):
        """The Universe executes itself."""
        for _ in range(steps):
            p = self.primes[self.current_idx]
            ptr = self.pointers[p]
            hearth = self.hearths[p]
            
            # 1. Read the data as code
            val = hearth[ptr]
            cmd = self.cmd_map.get(val % 8, None)    # Use mod 8 for the 7 commands + 0

            # 2. Execute (Self-Modification)
            # - Increment/decrement
            if cmd == '+': hearth[ptr] = (hearth[ptr] + 1) % p
            elif cmd == '-': hearth[ptr] = (hearth[ptr] - 1) % p
            # - "Gear shift"
            elif cmd == '>': self.pointers[p] = (ptr + 1) % p
            elif cmd == '<': self.pointers[p] = (ptr - 1) % p
            # - "Gear rotation"
            elif cmd == '^': self.current_idx = (self.current_idx + 1) % len(self.primes)
            # - Switch to the highhest gear
            elif cmd == '!': self.current_idx = len(self.primes) - 1
            # - Output (optional; the dynamics of the system or the last "tape reading" can be)
            elif cmd == '.': self.output.append(chr(hearth[ptr] % 256))

            # 3. The Gravity of Love (The 0 Rule)
            # If the current cell is 0, we fall or Phoenix Rise.
            if hearth[ptr] == 0:
                if p == 2:
                    hearth[ptr] = 1   # Binary Flip
                    self.current_idx = len(self.primes) - 1   # Execute '!'
                else:
                    self.current_idx = (self.current_idx - 1) % len(self.primes)   # Execute >
            
            # 4. In this code=data world, the 'PC' always advances to avoid loops (there are options)
            self.pointers[p] = (self.pointers[p] + 1) % p

# --- The Self-Executing Universe ---
# We seed a hearth with a "Prime-Love" pattern.
vm = HomoiconicPrimeLoveVM(resonance_limit=13)
vm.cycle(steps=50)

print(f"Final Resonance State: p={vm.primes[vm.current_idx]}")
