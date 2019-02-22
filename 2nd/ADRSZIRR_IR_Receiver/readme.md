# ADRSZIRR ゼロワンシリーズ赤外線受信ボードの使い方

### *製品ページは[こちら](http://bit-trade-one.co.jp/product/module/adrszirr)*

## 1.lircの設定

最初に、Linuxの純正赤外線受信ライブラリ”lirc”をインストールします。  

```sh
sudo apt-get install lirc
```

インストール後、 /etc/lirc/lirc_options.conf を変更します。  
ファイル先頭、コメント文の次に以下の設定があります。  

```:
[lircd]
nodaemon        = False
driver          = devinput
device          = auto
output          = /var/run/lirc/lircd
pidfile         = /var/run/lirc/lircd.pid
plugindir       = /usr/lib/arm-linux-gnueabihf/lirc/plugins
permission      = 666
allow-simulate  = No
repeat-max      = 600
```

この内以下の設定を次の通りに変更します。  

```:
driver          = default
```

```:
device          = /dev/lirc0
```

また、 /boot/config.txt に以下の設定を書き込みます。  
"# Uncomment this to enable the lirc-rpi module"と書かれた行の下に”dtoverlay=lirc-rpi”とあるので、頭の'#'を消して設定を追記しましょう。  

```:
dtoverlay=lirc-rpi
dtparam=gpio_in_pin=4
dtparam=gpio_out_pin=13
dtparam=gpio_in_pull=up
```

再起動するとlircが有効になります。  
以下のコマンドを入力し、赤外線受光モジュールにリモコンを入力してみましょう。  

```sh
sudo systemctl stop lircd.socket
sudo systemctl stop lircd.service #lirc停止
mode2 -d /dev/lirc0               #RAWデータ出力
```

受信した赤外線データが表示されます。  

## 2.リモコンの登録

次のコマンドで赤外線データを記憶させることが出来ます。

```sh
irrecord ｰn -f -d /dev/lirc0
```

手順は以下の通りです。  

0. 最初に注意書きが出た後、Enterを押すと環境光測定を行う
1. リモコン名を登録
2. リモコンの学習させたい全てのボタンを一つずつ押していく。画面上にドットが増えていくので、メッセージが出るまで繰り返す
3. 登録したいボタン名を入力
4. Now hold down button "＜ボタン名＞"と出てきたら、該当するボタンを押す
5. 手順3と4を繰り返し、全てのボタンを記憶させる。
6. 記憶を終了するときは、手順3でボタン名を何も入れずEnterキーを押す
7. カレントディレクトリに" <リモコン名>.lircd.conf "が生成される
8. 生成されたファイルを以下のコマンドでコピーする  
```sudo cp <リモコン名>.lircd.conf /etc/lirc/lircd.conf.d/```

手順が終わったら再起動し、```irw```コマンドを実行してリモコンから赤外線モジュールに送信してみましょう。信号から押されたボタンを読み取ります。

## 3.コマンド設定

/etc/lirc/irexec.lircrc を編集することで、ボタンが押された時にコマンドを実行することが出来ます。

```
begin
	prog   = irexec
	button = ＜ボタン名＞
	config = ＜実行するコマンド＞
end
```

このような形で追記していくことにより、リモコンでRaspberry Piを操作することが出来ます。