# ADRSZOD　動作環境インストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszod/)*

ADRSZOD基板は、臭気センサが実装され、ラズパイzeroとは、GPIOシリアルで接続されています。

Python,またNode-RED上での出力について、Ch1が臭気センサからの出力となります。  
また、搭載する臭気センサにつきまして、各物質ごとの濃度は測定できません。ご了承くださいませ。  

下記に、基本的なインストール手順を示します。

## 1.os関係のインストール確認
　ＯＳは、下記で動作確認、日本語環境、I2C/SPI/serialインターフェイス許可  
　　　　2018-10-09-raspbian-stretch.zip  
　2018年10月時点で、最新版にして、基本モジュールをインストール  
``` sh
    sudo apt-get update  
    sudo apt-get install python-pip python3-pip  
    #raspberry Pi の設定＞インターフェイスで下記を設定
    #Serial Port 有効
    #Serial Console 無効
```

## 2.node-redの最新版をインストール

```sh
    bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)  
    #node-redを自動起動  
    sudo systemctl enable nodered.service  
    sudo reboot  
    #node-redにMQTTブローカをインストール  
    ＃パレットの管理→ノードを追加→moscaを検索→ノードを追加  
    sudo reboot  
```

## 3.サンプルソフト（adrszOD-sample.py）をダウンロード
サンプルソフトの仕様は下記

```sh
#　　　入力：ガスセンサー（TP-401T）の電圧値を、ＡＤコンバータ（mcp3424）で入力  
#　　　出力：ガスセンサー（TP-401T）の測定値を電圧値で表示  
#   必要により権限を付加  
    sudo chmod 777 *  
#   サンプルソフトを実行、初期表示文字が表示されることを確認、停止はCtrl+C  
    sudo python3 adrszAR-sample.py  
```

## 4．サンプルソフト（adrszOD_sample.json）をnode-redに張り付け


サンプルソフトの仕様は下記

```sh
#　　　入力：ガスセンサー（TP401-T）の電圧値
#　　　処理：立ち上げ時30秒の間10回測定し、平均値を求める
#　　　　　　上記、平均値より、ある程度大きく（設定可）なったら、下記を出力
#　　　出力：もし多くなったら・・・メッセージを出力
```
