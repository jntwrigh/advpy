def read_generator(filename='../resources/somefile.dat', chunk_size=2048):
    try:
        with open(filename, encoding='utf-8') as f:
            data = f.read(chunk_size)
            while data:
                yield data
                data = f.read(chunk_size)
    except IOError as e:
        print(e)


for idx, data in enumerate(read_generator()):
    print(f'Chunk {idx}, size: {len(data)}')
