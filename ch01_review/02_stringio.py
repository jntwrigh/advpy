import io

buffer = io.StringIO()
buffer.write('This is the initial buffer value.\n')
print('Added to buffer.', file=buffer)
buffer_results = buffer.getvalue()
buffer.close()

print(buffer_results)