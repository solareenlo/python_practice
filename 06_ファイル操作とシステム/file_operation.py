import os # ファイル操作に便利な標準ライブラリ4選
import pathlib
import glob
import shutil

print(os.path.exists('test.md')) # 現在のディレクトリにtest.mdはありますか？ という意味.
print(os.path.isfile('test.md')) # test.mdはファイルですか？ という意味.
print(os.path.isdir('design')) # designはディレクトリですか？ という意味.

# os.rename('test.md', 'renamed.md') # test.mdをrenamed.meに名称変更
# os.symlink('renamed.md', 'symlink.md') # symlinkファイル作成

pathlib.Path('empty.md').touch() # 空のファイルempty.mdを作成
os.remove('empty.md') # empty.mdファイルを削除

# os.mkdir('test_dir') # test_dirディレクトリを作成
# os.mkdir('test_dir/test_dir2') # test_dir2ディレクトリを作成
print(os.listdir('test_dir')) # test_dirディレクトリの中身を表示
pathlib.Path('test_dir/test_dir2/empty.md').touch() # empty.mdファイルを作成
shutil.copy('test_dir/test_dir2/empty.md', 'test_dir/test_dir2/empty2.md') # empty.mdファイルのコピーファイルempty2.mdを作成
print(glob.glob('test_dir/test_dir2/*')) # test_dir2内のファイルを全部表示
# shutil.rmtree('test_dir') # test_dirを全削除. 使用には気を付けて.

print(os.getcwd()) # 現在のディレクトリのパスを表示
