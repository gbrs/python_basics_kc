n = 7266
hours, minutes, seconds = n // 3600, (n - n // 3600 * 3600) // 60, n % 60
# hours = n // 3600
# minutes = (n - hours * 3600) // 60
# seconds = (n - hours * 3600) % 60

print(hours, minutes, seconds)