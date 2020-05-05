import pypdb
import requests

pdb_list = ['3FY7','2BN3']
string = '_diffrn_detector.pdbx_collection_date'

results = {}

def get_pdb(ID):
    pdb_data = pypdb.get_pdb_file(ID, filetype='cif', compression=False)
    return pdb_data


def lines_that_contain(string, fp):
    return [line for line in fp.splitlines() if string in line]


def collection_date(pdb_data):
    result = lines_that_contain(string, pdb_data)
    result = result[0].split("   ")[1]
    return(result)


for ID in pdb_list:
    pdb_string = get_pdb(ID)
    date = collection_date(pdb_string)
    results[ID]=date
    print(f"For PDB {ID} the collection date was {date}")

