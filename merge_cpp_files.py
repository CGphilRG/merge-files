def merge_cpp_files(output_file, *input_files):
    with open(output_file, 'w') as output:
        # Écrire les #include en premier
        output.write("// Headers\n")
        for input_file in input_files:
            with open(input_file, 'r') as input:
                for line in input:
                    if line.startswith("#include"):
                        output.write(line)

        # Écrire le reste du contenu
        output.write("\n// Code\n")
        for input_file in input_files:
            with open(input_file, 'r') as input:
                for line in input:
                    if not line.startswith("#include"):
                        output.write(line)

# Exemple d'utilisation :
merge_cpp_files('merged_output.cpp', 'file1.cpp', 'file2.cpp', 'file3.cpp')
