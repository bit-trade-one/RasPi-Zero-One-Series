## Q.別売りシステムクロック(ADRPM1801C)はそのまま挿すだけで使用できますか？

### A.はい、使用できます。
下記画像のとおりに接続してください。追加の設定は不要です。
![接続画像参照](https://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/658326031b180e9a4e18270f9c0332c2.jpg)

## Q.Raspberry Pi 5には対応していますか？

### A.追加の設定が必要になります。

/boot/firmware/config.txtを以下の様に修正し、再起動します。
~~~
# i2sをONにする（コメントアウトされている場合、先頭の＃を削除する）
dtparam=i2s=on

# オーディオ出力をOFFにする（すでに記載されている場合、先頭に#をつけコメントアウトする）
#dtparam=audio=on

# HDMIへのオーディオ出力をOFFにする場合、以下の行を追加する
dtoverlay=vc4-kms-v3d,noaudio

# 搭載するDACに応じてどちらかを記載してください
# ADRSZDACの場合
dtoverlay=hifiberry-dacplus-std,24db_digital_gain

# ADRSZDAC に外部システムクロックボードADRPM1801Cを搭載する場合
dtoverlay=hifiberry-dacplus-pro,24db_digital_gain
~~~

---
