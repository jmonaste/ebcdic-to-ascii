import codecs

# Input EBCDIC file and output ASCII file names
ebcdic_file = 'ebcdic_file.txt'
ascii_file = 'ascii_file.txt'

# Open the EBCDIC file in read mode and the ASCII file in write mode
with open(ebcdic_file, 'rb') as input_file, open(ascii_file, 'w') as output_file:
    # Read the contents of the EBCDIC file
    ebcdic_content = input_file.read()

    # Decode the EBCDIC content to ASCII
    ascii_content = codecs.decode(ebcdic_content, 'cp500')

    # Write the ASCII content to the output file
    output_file.write(ascii_content)

print("Conversion completed.")
