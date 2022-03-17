# 表作成スクリプト使い方メモ
## このフォルダに含まれるファイル
- kento-kai.py
	- 検討会用の表作成スクリプト（python）
	- 検討会だけでなく、色々な場面で使える可能性
- mkmtggrid-multi.py
	- 津邑研ミーティング資料ページの表を作成するスクリプト
	- mkmtggrid.plを内部で複数回動かしている
- mkmtggrid.pl
	- 津邑研ミーティング資料ページの表一行分を作成するスクリプト（perl）
	- 津邑先生からいただいた
	- その年に合わせてアカウント名を設定しないといけない
		- ファイルを編集して設定（見るとわかると思う） 

## 各ファイルの使い方
### kento-kai.py
- 使い方: ./kento-kai.py 10 7 1 1 20200324 20200630
	- 第1引数: 表の列の数（研究室のメンバーの数に合わせる）
	- 第2引数: 日にちの間隔（１週間おきなら７）
	- 第3引数: 曜日を付加するか (Yes=>1, No=>other)
	- 第4引数: 土日を色付けするか  (Yes=>1, No=>other)
	- 第5引数: 開始日（20200304というフォーマットで）
	- 第6引数: 終了日 (20200304というフォーマットで。なくてもいい。その場合は30行分出力される)

### mkmtggrid-multi.py
- 使い方: ./mkmtggrid-multi.py 20200324
	- 第1引数: 開始日（20200304というフォーマットで。なくてもいいがその場合はスクリプトを動かした日が設定される）
	- スクリプト中のMAX変数が出力する行数になっているので、必要ならここを変更してください

### mkmtggrid.pl
-  使い方は mkmtggrid-multi.py と同じだが、一行分しか出力されない
