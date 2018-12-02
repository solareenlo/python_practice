import tarfile

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir') # test_dirディレクトリをtest.tar.gzとして圧縮する

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar') # test.tar.gzをtest_tarとして展開
    with tr.extractfile('test_dir/test_dir2/empty.md') as f: # tarファイルを解凍ぜずに中身を閲覧する
        print(f.read()) # b'empty\n' と表示
