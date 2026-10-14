def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20


print(does_attack_hit(10, 5));
print(does_attack_hit(1,-10));
print(does_attack_hit(20, -34));
