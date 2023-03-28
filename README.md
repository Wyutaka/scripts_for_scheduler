# 表作成スクリプト使い方メモ
検討会、ミーティング発表実績のページ作成時には基本的にkento-kai-handout.pyを使っていれば問題ないと思います
## このフォルダに含まれるファイル
- kento-kai.py
	- 検討会用の表作成スクリプト（python）
	- 検討会だけでなく、色々な場面で使える可能性
- kento-kai-handout.py
	- kento-kai.pyを拡張したもの
	- 研究室のメンバーの名前と何周目に発表するかを入力することでその日の資料のリンクを作成する
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

### kento-kai-handout.py
- 使い方: ./kento-kai-handout.py 7 1 1 20200324 20200630
	- 第1引数: 日にちの間隔（１週間おきなら７）
	- 第2引数: 曜日を付加するか (Yes=>1, No=>other)
	- 第3引数: 土日を色付けするか  (Yes=>1, No=>other)
	- 第4引数: 開始日（20200304というフォーマットで）
	- 第5引数: 終了日 (20200304というフォーマットで。なくてもいい。その場合は30行分出力される)
	
	
	実行例
	```python
	#[("名前"), 何周目]を学年ごとに記入
	lab_menber_list_M2 = [("foo", 1)]
	lab_menber_list_M1 = [("s-shiraki", 1), ("nomura", 2), ("t-yamamoto", 3),("y-watanabe", 3), ("nihonmatu", 1), ("miwagawa", 2)]
	lab_menber_list_B4 = [("hoge", 1), ("bar", 2)]

	./kento-kai.py 7 1 1 20200324 20200630
	||3/24(火) ||[[attachment:foo-ken-20200324.pptx|資料]] ||[[attachment:s-shiraki-ken-20200324.pptx|資料]] || || || ||[[attachment:nihonmatu-ken-20200324.pptx|資料]] || ||[[attachment:hoge-ken-20200324.pptx|資料]] || ||
	||3/31(火) ||[[attachment:foo-ken-20200331.pptx|資料]] || ||[[attachment:nomura-ken-20200331.pptx|資料]] || || || ||[[attachment:miwagawa-ken-20200331.pptx|資料]] || ||[[attachment:bar-ken-20200331.pptx|資料]] ||
	||4/7(火) ||[[attachment:foo-ken-20200407.pptx|資料]] || || ||[[attachment:t-yamamoto-ken-20200407.pptx|資料]] ||[[attachment:y-watanabe-ken-20200407.pptx|資料]] || || ||[[attachment:hoge-ken-20200407.pptx|資料]] || ||
	...略
	```

### mkmtggrid-multi.py
- 使い方: ./mkmtggrid-multi.py 20200324
	- 第1引数: 開始日（20200304というフォーマットで。なくてもいいがその場合はスクリプトを動かした日が設定される）
	- スクリプト中のMAX変数が出力する行数になっているので、必要ならここを変更してください

### mkmtggrid.pl
-  使い方は mkmtggrid-multi.py と同じだが、一行分しか出力されない
