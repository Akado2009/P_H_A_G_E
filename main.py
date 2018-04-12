import argparse
import sys
import subprocess
import os

class SequenceFileNotFoundError(Exception):
    pass


class DatabaseNotFoundError(Exception):
    pass


class SequenceObject(object):

    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence

class AlignmentObject(object):

    def __init__(self, ids, sequences):
        self.ids = ids
        self.sequences = sequences


def add_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input" , help="Input file with phage sequence", required=True)
    parser.add_argument("--genbank", action="store_const", const='Y', help="Indicate the you use GenBank format. Fasta is default")
    parser.add_argument("-d", "--database", help="Provide database pathway. Default pathway is database/", default="database/")
    parser.add_argument("-a", "--alignment", help="Specify alignment software. Options are: Mauve (M), Lagan (L). Default is Mauve", default="M")

    return parser

def check_arguments(arguments):

    if not os.path.isfile(arguments.input):
        raise SequenceFileNotFoundError("There is no such file: {}".format(arguments.input))

    if not os.path.exists(arguments.database):
        raise DatabaseNotFoundError("There is no such database folder: {}".format(arguments.database))

def parse_genbank(gbk_file):
    print('GBK')

def parse_fasta(fasta_file):
    pritn('FASTA')

def perform_search(sequence_object):
    print('SEARCH')

def align(software):
    print('ALIGNING')

def display(alignment_object):
    print('CALLING DISPLAY')

def create_logo(alignment_object):
    print('CREATING LOGO')

def create_consensus(alignment_object):
    print('CRETING CONSENSUS')

if __name__ == "__main__":
    arguments = add_parser().parse_args()
    check_arguments(arguments)
