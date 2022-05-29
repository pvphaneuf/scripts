import glob
import csv


file_search_str = "./**/data/output.gd"
genomediff_path_l = list(glob.iglob(file_search_str, recursive=True))
mut_type_l = ["SNP", "SUB", "DEL", "INS", "MOB", "AMP", "CON", "INV"]
print("sample" + '\t' + ('\t'.join(mut_type_l)))
for f in genomediff_path_l:
    sample_mut_type_count_dict = {mut_type: 0 for mut_type in mut_type_l}
    with open(f) as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            if row[0] in sample_mut_type_count_dict.keys():
                sample_mut_type_count_dict[row[0]] += 1

    sample_name = f.split('/')[1]
    output_row_str = sample_name + '\t'
    for mut_type in mut_type_l:
        output_row_str += str(sample_mut_type_count_dict[mut_type]) + '\t'
    print(output_row_str)
