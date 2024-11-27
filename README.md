# おもちゃ貸出システム

松山市内の児童館に渡したシステム。
すべてPythonで作成しています。

高校3年生の頃に独学で制作したもののため、コードが汚いです。
また、メインPCのHDDの奥深くから引き出してきたものになるため、今の環境では実行できないorそもそもコードミスが存在しているかもしれません。
追記:今考えるともうちょいマシなコード書けたろ


Main_System.py
-
いわゆる「おもちゃ貸出システム」です。
単純に特定のQRコードのデータを読み取り、そのデータと日付をCSVファイルに書き出しています。
ついでにGUIで、おもちゃの名前と、児童に「たいせつにあつかってね！」と呼びかけるようにしています。

Sub_System.py - 捜索中...
-
上記の「おもちゃ貸出システム」とは別に、「どのおもちゃがどれだけ貸し出されているか」の目安のために作成したプログラムです。
このプログラムは、上記のおもちゃ貸出システムで生成したCSVファイルを読み取り、どのおもちゃがどれだけ貸し出されたかを、貸し出された回数が多い順に別のCSVファイルに書き出しています。
これにより、児童にとって今人気のおもちゃを把握し、それの予備を買い足すなどといった指標にもなります。



このプログラムは、僕一人の力では作りきることが確実にできなかったです。この場を借りてお礼を申し上げます。
YとWとMくん、ありがとう！愛媛帰ったら酒飲もうな！

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

### Permissions
- **Commercial use**: You can use this project for commercial purposes.
- **Modification**: You can modify the code as you wish.
- **Distribution**: You can share this project freely.
- **Private use**: You can use this project in private.

### Limitations
- **Liability**: The author is not responsible for any damages caused by using this project.
- **Warranty**: This project is provided "as-is," without any warranty of any kind.
