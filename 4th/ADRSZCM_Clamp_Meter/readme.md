# adrszCM　のインストール

本基板は、インターフェイスがadafluitのAdafruit_Python_ADS1x15モジュールと互換性があります。  
adafruitのライブラリをインストールします。  
下記に、基本的な手順を示します。  

## 1.OS関係のインストール確認

　OSは、下記で動作確認　（日本語環境、I2C・SPIインターフェイス許可）  
　　　　2018-11-13-raspbian-stretch-full.zip（1.98GB）  
2018年12月時点で、最新版にして、基本モジュールをインストール  

```sh
    sudo apt-get update
    sudo apt-get install python-pip python3-pip
```

## 2．node-redの最新版をインストール

```sh
    bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
    #node-redを自動起動
    sudo systemctl enable nodered.service 
    sudo reboot
    #node-redにMQTTブローカをインストール
    #パレットの管理→ノードを追加→moscaを検索→ノードを追加
    sudo reboot
```

## 3.pythonライブラリのインストール

```sh
    git clone https://github.com/adafruit/Adafruit_Python_ADS1x15

    cd Adafruit_Python_ADS1x15/

    sudo python3 setup.py install
    cd

```

## 4．btoからサンプルソフトをダウンロード

adrszCM-ads1115diffch0.py　：ｃｈ０を500回サンプリングし二乗平均値を出力　Ｗレベル用  
adrszCM-ads1115diffch2.py　：ｃｈ２を500回サンプリングし二乗平均値を出力　Ｗレベル用  
adrszCM-ads1115diffch2_G16.py  
　：ｃｈ２をゲイン１６倍で、500回サンプリングし二乗平均値を出力　ｍＷレベル用  

サンプルソフトの仕様は下記

- 入力：ｃｈ０、ｃｈ２より、電流を５００回入力  
- 出力：500回分を二乗平均し、数字で表示  

必要により権限を付加  
    ```sudo chmod 777 *```  
サンプルソフトを実行、初期表示文字が表示されることを確認、停止はCtrl+C  
    ```sudo python3 adrszCM-ads1115diffch0.py```  

## 5．Node-REDのサンプルソフト（adrszLD-node-sample.json）を、Node-REDにコピー  

必要なnodeをパレットの管理→ノードを追加から追加インストール  
　dashboard：[https://flows.nodered.org/node/node-red-dashboard](https://flows.nodered.org/node/node-red-dashboard)  
サンプルソフトの仕様は下記

- 入力：上記pythonのサンプルソフトを順番に呼び出し電流値を入力  
- 出力：rangeノードで消費電力値に校正して、表示  
尚、起動は最初のinjectノードからトリガ  


