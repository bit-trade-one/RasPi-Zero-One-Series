# ADRSZGP 動作環境インストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszgp/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZGP_GPS/Schematics/ADRSZGP_v11_schematics.pdf)

adrszGP基板は、GPSモジュールが実装され、ラズハ゜イｚｅｒｏとは、ＧＰＩＯ　シリアルで接続されています。  


下記に、基本的なインストール手順を示します。  

## 1. os関係のインストール確認
　ＯＳは、下記で動作確認、日本語環境、Ｉ２Ｃ、ＳＰＩ、ｓｅｒｉａｌインターフェイス許可  
　　　　2018-10-09-raspbian-stretch.zip  
　2018年10月時点で、最新版にして、基本モジュールをインストール  
```sh
    sudo apt-get update  
    sudo apt-get install python-pip python3-pip  
    #raspberry Pi の設定＞インターフェイスで下記を設定  
    Serial Port 有効  
    Serial Console 無効  
```

## 2. node-redの最新版をインストール

```sh
    bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)  
    #node-redを自動起動  
    sudo systemctl enable nodered.service  
    sudo reboot  
    #node-redにMQTTブローカをインストール  
    #パレットの管理→ノードを追加→moscaを検索→ノードを追加  
    sudo reboot  
```

## 3. ＮＯＤＥ－ＲＥＤのサンプルソフト（node-red-gps-serial-sample.json）を、ＮＯＤＥ－０ＲＥＤにコピー
サンプルソフトの仕様は下記  
#　　　入力：gpsモジュールから、シリアルでＧＰＳデータを入力  
#　　　出力：１分おきにＧＰＳデータをＣＳＶファイルに出力  

## EX. ＣＳＶファイルは、google　mapに張り付けることができます。  
　　参考ＵＲＬ：　https://www.google.com/mymaps/
