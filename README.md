# Milestone2
dna_dict = {'Rosalind_0498': 'AAATAAA',
            'Rosalind_2391': 'AAATTTT', 
            'Rosalind_2323': 'TTTTCCC', 
            'Rosalind_0442': 'AAATCCC', 
            'Rosalind_5013': 'GGGTGGG'}
def get_edges(dna_dict):
    adjacency_list = []
    for edge1, dna_string1 in dna_dict.items():
        for edge2, dna_string2 in dna_dict.items():
            if edge1 != edge2 and dna_string1[-3:] == dna_string2[:3]:
                adjacency_list.append((edge1, edge2))
    return adjacency_list
    
