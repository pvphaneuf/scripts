from os import listdir

artifacts = listdir('.')

sample_files = []

for artifact in artifacts:
    if "fastq" in artifact:
        sample_files.append(artifact)

samples = []

for sample_file in sample_files:

    # Get samples
    sample_name_end_idx = sample_file.find('_S')
    sample_name = sample_file[:sample_name_end_idx]

    # Append non-duplicate samples
    if sample_name not in samples:
        samples.append(sample_name)
        print sample_name
