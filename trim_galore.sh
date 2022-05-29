#!/bin/bash
# The adapter sequences included here are for KAPA sequencing library prep kits. 

~/TrimGalore-0.4.3/trim_galore --fastqc --paired -q 20 --path_to_cutadapt ~/.local/bin/cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -a2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT *fastq.gz
