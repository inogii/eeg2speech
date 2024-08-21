import os

def combine_files(output_file, parts):
    with open(output_file, 'wb') as outfile:
        for part in parts:
            with open(part, 'rb') as infile:
                outfile.write(infile.read())

def main():
    # Output directory for downloaded chunks
    output_dirs = ["data/checkpoints/inogii_audioldm_checkpoints"]
    
    for output_dir in output_dirs:
        # Determine the appropriate output file based on the type of chunks found
        if any(f.startswith("dataset.zip.part") for f in os.listdir(output_dir)):
            output_file = "data/dataset/reassembled_dataset.zip"
            parts = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.startswith("dataset.zip.part")])
        elif any(f.startswith("checkpoints.zip.part") for f in os.listdir(output_dir)):
            output_file = "data/checkpoints/reassembled_checkpoints.zip"
            parts = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.startswith("checkpoints.zip.part")])
        else:
            continue  # Skip if no relevant parts are found

        # Combine the chunks into the output file
        combine_files(output_file, parts)

if __name__ == "__main__":
    main()
