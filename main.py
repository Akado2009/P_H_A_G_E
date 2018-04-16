import argparse
import sys
import subprocess
import os
from Bio import SeqIO

from lib.parsers import GBKParser, FastaParser
import lib.system as system
from lib.logo import LogoGenerator
import lib.helpers as helpers

import pandas as pd
import matplotlib.pyplot as plt


class SequenceFileNotFoundError(Exception):
    pass


class DatabaseNotFoundError(Exception):
    pass


class SequenceObject(object):

    def __init__(self, id, sequence):

        self.id = id
        self.sequence = sequence

class AlignmentObject(object):

    def __init__(self, filename):

        data = self.parse_fasta(filename)
        self.ids = data['ids']
        self.sequences = data['seqs']

    def parse_fasta(self, filename):

        ids = []
        seqs = []

        for seq_record in SeqIO.parse(filename, "fasta"):
            ids.append(seq_record.id)
            seqs.append(repr(seq_record.seq))

        return {
            'ids': ids,
            'seqs': seqs
        }

def add_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input" , help="Input file with phage sequence", required=True)

    parser.add_argument("--genbank", action="store_const", const='Y', help="Indicate the you use GenBank format. Fasta is default")

    parser.add_argument("-d", "--database", help="Provide database pathway. Default pathway is database/", default="database/")

    parser.add_argument("-a", "--alignment", help="Specify alignment software. Options are: Mauve (M), Lagan (L). Default is Mauve", default="M")

    parser.add_argument("-t", "--threshold", help="Specify a threshold for BLAST. Default value is 90.", default=90)

    return parser

def check_arguments(arguments):

    if not os.path.isfile(arguments.input):
        raise SequenceFileNotFoundError("There is no such file: {}".format(arguments.input))

    if not os.path.exists(arguments.database):
        raise DatabaseNotFoundError("There is no such database folder: {}".format(arguments.database))

def parse_genbank(gbk_file):

    content = GBKParser(fasta_file)
    sequence_object = SequenceObject(content.id, content.seq)

    return SequenceObject

def parse_fasta(fasta_file):

    content = FastaParser(fasta_file)
    sequence_object = SequenceObject(content.id, content.seq)

    return SequenceObject

def perform_search(sequence_object):

    print('SEARCHING')

def create_profile(sequence_object, new=True):

    df = pd.read_csv('sp500.csv')

    positions = [i for i in range(1, 124)]
    df['date'] = positions

    x = positions
    y = df['price']

    plt.bar(x, y, width=1.0)
    plt.show()

def perform_search_using_profile(profile):
    print('SEARCH WITH PROFILE')

def perform_search_with_gene_order(sequence_object):
    print('SEARCH WITH ORDER')

def align(software):
    print('ALIGNING')

def display(alignment_object):
    print('CALLING DISPLAY')

def create_logo(alignment_object):

    logo = LogoGenerator('test_alignment.fasta')
    logo.generate_logo()


def create_consensus(filename):

    alignment = AlignmentObject('test_alignment.fasta')

    consensus_sequence = ''

    for i in range(len(alignment.sequences[0])):
        position_list = [seq[i] for seq in alignment.sequences]
        consensus_sequence += helpers.most_common(position_list)

    return consensus_sequence


if __name__ == "__main__":

    arguments = add_parser().parse_args()

    print(create_consensus(''))
