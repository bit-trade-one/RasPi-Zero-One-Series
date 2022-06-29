# よくある質問

## Q: シャットダウンシーケンスは自動的に実行されますか

### A: Raspberry Pi ZEROのconfig.txtの設定や、Node_REDを使用することにより、シャットダウンシーケンスを自動的に実行することが可能です。<br>

* config.txtの設定<BR>
config.txtを設定することでGPIOピンによるシャットダウンシーケンスの起動を設定することが可能です。<BR>

```sh
#config.txtに以下の設定を追加してください。
$ sudo vi /boot/config.txt
dtoverlay=gpio-shutdown,gpio_pin=6
```

* Node-RRDの設定<BR>
Node_REDを使用することでシャットダウンシーケンスを起動させることが可能です。詳細は下記の使い方を参照してください。<BR>
https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZUP_Capacitor
<BR>
----

## Q: 他のゼロワンシリーズと併用できますか

### A: GPIOの使用番号一覧を作成いたしました。番号が被らないものであれば併用可能です。
https://github.com/bit-trade-one/RasPi-Zero-One-Series
