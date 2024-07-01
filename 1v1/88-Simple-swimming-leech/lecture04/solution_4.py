def main():
    file_path = './data/nyc_jobs.csv'
    entry_level_jobs = {}

    file = open(file_path, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines[1:]:
        columns = line.strip().split(',')
        agency = columns[1].strip().upper()
        career_level = columns[2].strip()
        if career_level == 'Entry-Level':
            if agency not in entry_level_jobs:
                entry_level_jobs[agency] = 0
            entry_level_jobs[agency] += 1

    # 计算每个 agency 的长度并找到最大长度
    max_agency_length = 0
    for agency in entry_level_jobs:
        agency_length = len(agency)
        if agency_length > max_agency_length:
            max_agency_length = agency_length

    # 手动排序 entry_level_jobs 的 items
    sorted_items = []
    for agency in entry_level_jobs:
        sorted_items.append((agency, entry_level_jobs[agency]))

    # 手动排序
    for i in range(len(sorted_items)):
        for j in range(i + 1, len(sorted_items)):
            if sorted_items[i][0] > sorted_items[j][0]:
                sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

    # 输出结果
    # for agency, count in sorted_items:
    #     print(f"{agency.ljust(max_agency_length)} {count:>5}")
    for agency, count in sorted_items:
        formatted_agency = agency + ' ' * (max_agency_length - len(agency))
        print(f"{formatted_agency} {count:>5}")

if __name__ == '__main__':
    main()
