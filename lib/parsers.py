from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO


class GBKParser(object):

    def __init__(self, file):

        parsed_content = self.parse(file)

        self.id = parsed_content["id"]
        self.sequence = parsed_content["sequence"]

    def parse(self, filename):

        records = [record for record in SeqIO.parse(filename, "genbank")]

        return {
            "id": records[0].id,
            "sequence": records[0].seq
        }




class FastaParser(object):

    def __init__(self, file):

        parsed_content = self.parse(file)

        self.id = parsed_content["id"]
        self.sequence = parsed_content["sequence"]

    def parse(self, filename):

        record = SeqIO.read(filename, "fasta")

        return {
            "id": record.id,
            "sequence": record.seq
        }
