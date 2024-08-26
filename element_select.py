#!/usr/bin/env python3

import argparse

# ASCII图像
ascii_art = """
 _____  _____  _____  _      _        _    
|  __ \|  _  |/  __ \| |    (_)      | |   
| |  \/| | | || /  \/| |__   _   ___ | | __
| | __ | | | || |    | '_ \ | | / __|| |/ /
| |_\ \\ \_/ /| \__/\| | | || || (__ |   < 
 \____/ \___/  \____/|_| |_||_| \___||_|\_\                                                                                                    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣁⣤⣴⣶⣶⣶⣦⣤⣉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⠂⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣧⣶⣼⣿⠟⠻⣿⣧⣴⣬⣿⣿⣿⣿⡿⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠆⠻⣿⣿⡟⣱⣾⣷⡌⢿⣿⣿⣿⣿⣿⠟⢁⡘⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⡟⣨⣙⠀⠻⠿⠿⠿⢂⡿⠿⠟⣋⣡⣄⠻⣕⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣏⠠⣾⠏⣰⣿⣿⣿⣦⣄⣠⣶⣶⣶⣾⣿⣿⣿⣿⡆⠹⢡⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡈⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠀⠉⠙⠛⠛⠛⠛⠛⠉⠁⢤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠂⣴⡀⣿⣿⣿⣿⣇⣤⣴⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""

# 定义不同功能类型对应的GO编号集合
go_data = {
    'ph': {
        'GO_term': {"GO:0009987", "GO:0050896", "GO:0006950", "GO:0042221", "GO:0009628",  "GO:0009268", "GO:0010447"}
    },
    'ox': {
        'GO_term': {'GO:0050896', 'GO:0009987', 'GO:0009628', 'GO:0006950', 'GO:0042221', 'GO:1901700', 'GO:0006979', 'GO:0033554', 'GO:0070887'}
    },
    'tp': {
        'GO_term': {'GO:0050896', 'GO:0009987', 'GO:0009628', 'GO:0006950', 'GO:0009266', 'GO:0009408'}
    },
    'unresponse': {
        'GO_term': {"GO:0050896"}
    }
}

# 读取基因与GO编号数据
def load_gene_go_data(filepath):
    gene_to_go = {}
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            gene_name, go_term = parts[0], parts[1]
            if gene_name not in gene_to_go:
                gene_to_go[gene_name] = set()
            gene_to_go[gene_name].add(go_term)
    return gene_to_go

# 根据GO编号筛选基因
def filter_genes(gene_to_go, go_terms_set):
    return [gene for gene, go_terms in gene_to_go.items() if go_terms_set.issubset(go_terms)]

# 主函数
def main():
    print(ascii_art)  # 显示ASCII图像

    parser = argparse.ArgumentParser(description='Filter genes based on GO terms.')
    parser.add_argument('-i', '--input', required=True, help='Input file path.')
    parser.add_argument('-o', '--output', required=True, help='Output file path.')
    parser.add_argument('-f', '--function', choices=['ph', 'tp', 'ox', 'unresponse'], required=True, help='Function type to filter by (ph, tp, ox, unresponse).')

    args = parser.parse_args()
    input_filepath = args.input
    output_filepath = args.output
    function = args.function

    # 载入数据
    gene_to_go = load_gene_go_data(input_filepath)

    # 根据功能选择过滤基因
    if function in go_data:
        filtered_genes = filter_genes(gene_to_go, go_data[function]['GO_term'])
    else:
        filtered_genes = []

    # 将结果写入文件
    with open(output_filepath, 'w') as file:
        file.write(f'{"="*20}{function.upper()}{"="*20}\n')
        for gene in filtered_genes:
            file.write(f'{gene}\n')

    print("结果已保存到", output_filepath)

if __name__ == "__main__":
    main()






