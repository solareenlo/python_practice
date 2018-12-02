import subprocess # Python上でターミナルのコマンドが使える標準ライブラリ

subprocess.run(['ls', '-al']) # ターミナルの, ls -al と同じ結果を表示
# subprocess.run('ls -al | grep test', shell=True) # これの使用は推奨されていない. なぜなら, rm -fr を直ぐに付け加えることができるから.

# r = subprocess.run('lsaa', shell=True) # コマンドに無いlsaaを入力すると,
# print(r.returncode) # 127 を表示. 0でないのでエラーと言うこと. 0が正常.

# subprocess.run('lsaaa', shell=True, check=True) # こちらは直接エラーが返ってくる

# subprocess.run(['lsaa', '-al']) # エラーが返ってくる



# subprocess.run('ls -al | grep test' shell=True) のshell=Trueを使わずに同様の機能を実行するには, 以下の4行を行えば良い.
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
