leak = "9df83b0.804b000.80489c3.f7f87d80.ffffffff.1.9df6160.f7f95110.f7f87dc7.0.9df7180.1.9df8390.9df83b0.6f636970.7b465443.306c5f49.345f7435.6d5f6c6c.306d5f79.5f79336e.35386130.32356533.fffc007d.f7fc2af8.f7f95440.e8a7aa00.1.0.f7e24be9.f7f960c0.f7f875c0.f7f87000.fffcb1b8.f7e1558d.f7f875c0.8048eca.fffcb1c4.0.f7fa9f09.804b000.f7f87000.f7f87e20.fffcb1f8.f7fafd50.f7f88890.e8a7aa00.f7f87000.804b000.fffcb1f8.8048c86.9df6160.fffcb1e4.fffcb1f8.8048be9.f7f873fc.0.fffcb2ac.fffcb2a4.1.1.9df6160.e8a7aa00.fffcb210.0.0.f7dcaf21.f7f87000.f7f87000.0.f7dcaf21.1.fffcb2a4.fffcb2ac.fffcb234.1.0.f7f87000.f7faa70a"
flag = ""
for data in leak.split("."):
    try:
        data = bytearray.fromhex(data).decode()[::-1]
        flag += data
    except:
        continue

print(flag)
