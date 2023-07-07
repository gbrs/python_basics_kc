a = "div*2"
# result = "<div></div><div></div>"

# a = "p*1"
# result = "<p></p>"

# a = "li*3"
# result = "<li></li><li></li><li></li>"

result = f'<{a[:-2]}></{a[:-2]}>' * int(a[-1])

print(result)
