import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    #z.write('test_dir') # test_dir だけzip化
    #z.write('text_dir/test.md') # test.md だけzip化
    for f in glob.glob('test_dir/**', recursive=True): # test_dir 以下のファイル全てをzip化
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz') # test.zip をzzzとして解凍
    with z.open('test_dir/test_dir2/empty.md') as f:
        print(f.read()) # test.zipの中のtest_dir/test_dir2/empty.mdだけを表示
