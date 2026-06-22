import zlib

text = "hello world!hello world!hello world!hello world!"

compressed = zlib.compress(text.encode())

decompressed = zlib.decompress(compressed).decode()

print("Compressed:", compressed)
print("Decompressed:", decompressed)

# encode() converts the string to bytes. zlib.compress() compresses the bytes. zlib.decompress() decompresses the bytes.
# decode() converts the bytes back to a string.zlib.compress() works only with bytes-like objects, not Python strings.