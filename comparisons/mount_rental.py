def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime chanrge"
    return "no charges yet"


print(check_mount_rental(10, 5))
print(check_mount_rental(10, 10))
print(check_mount_rental(10, 15))
