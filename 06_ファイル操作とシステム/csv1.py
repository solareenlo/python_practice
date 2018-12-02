import csv # csvファイルを扱うための標準ライブラリ

with open('test.csv', 'w') as csv_file: # csvファイルに書き込み
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader() # headerのNameとCountを書込み
    writer.writerow({'Name': 'A', 'Count': '1'}) # A 1 を書込み
    writer.writerow({'Name': 'B', 'Count': '1'}) # B 1 を書込み

with open('test.csv', 'r') as csv_file: # csvファイルを読み込み
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count']) # A 1 B 1 と縦に表示
