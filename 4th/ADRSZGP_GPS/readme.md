# ADRSZGP ゼロワン GPS拡張基板 取り扱い説明書

## 本製品について

本製品はGPSモジュールを搭載するRaspberry Pi Zero用pHAT基板です。

## 使い方

本製品を利用するためにはRaspberry Pi ZeroのGPIO上にあるUART通信端子の有効化が必要です。

### GUI（デスクトップ環境）の場合

スタートメニュー->「設定」->「Raspberry Piの設定」を開き、
「インターフェイス」のタブから

- Serial Port: 有効
- Serial Console: 無効

としてください。

### CUI（コンソール環境）の場合

```sh
sudo raspi-config 
```

より、```5 Interfacing Options```ｰ>```P6 Serial```を選択し、```Would you like a login shell ~~~```と表示されたら "いいえ" を選択してください。  
次に```Would you like the serial port ~~~```と表示されたら "はい" を選択してください。

## サンプル：Node-REDによる情報処理

![](Node-RED.png)  
[サンプルはこちら](Node-RED.json)  
GPSモジュールより送られてくる情報は```NMEAフォーマット```の文字列で送られてきます。  
このサンプルではNode-REDを使い、"$GPGGA"より始まる文字列を解析し緯度・経度を取り出します。  
一番右側のdebugノードに[ "緯度","経度" ]の配列で位置情報が出力されます。  
※NMEAフォーマットについては関連する情報をご参照ください。