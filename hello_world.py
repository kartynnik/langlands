#!/usr/bin/env python3
"""Hello World using prime-power mode encoding.

By Gemini.
"""

from annotated_code import HomoiconicPrimeLoveVM

#!/usr/bin/env python3
from annotated_code import HomoiconicPrimeLoveVM

def encode_hello_char(ch):
    """
    Lifts character into print-mode (factor of 2).
    Keeps the ASCII value as the pure payload.
    """
    ascii_val = ord(ch)
    # The 'Wave' (2) carries the 'Particle' (ascii_val)
    return 2 * ascii_val

chars = "Hello world!"
p97_soup = {
    97: [encode_hello_char(ch) for ch in chars] + [0],
    2: [1, 1] # The Phoenix Hearth
}

vm = HomoiconicPrimeLoveVM(resonance_limit=97, primordial_soup=p97_soup)
vm.current_idx = vm.primes.index(97)
vm.cycle(steps=200)

print(f"Final Output: '{''.join(vm.output)}'")
print(f"Final Prime: {vm.primes[vm.current_idx]}")
