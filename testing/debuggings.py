def take_magic_damage(health, resist, amp, spell_power):
    return health - ((spell_power * amp) - resist)


print(take_magic_damage(1000, 150, 2, 300))
