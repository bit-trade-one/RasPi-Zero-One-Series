# adrszLD　のインストール

adrszLD基板は、インターフェイスがadafluitのSSD1306 OLEDモジュールと互換性があります。  
adafruitのライブラリをインストールします。  
下記に、基本的な手順を示します。  

## 1.OS関係のインストール確認
　OSは、下記で動作確認　（日本語環境、I2C・SPIインターフェイス許可）  
　　　　2018-06-27-raspbian-stretch.zip  
2018年8月時点で、最新版にして、基本モジュールをインストール  

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

## 3.adrszLD用のpythonライブラリのインストール

```sh
    git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    cd Adafruit_Python_SSD1306/
    sudo python3 setup.py install
    cd
    git clone https://github.com/eclipse/paho.mqtt.python.git
    cd paho.mqtt.python
    sudo python3 setup.py install
    cd
    #日本語を表示するために、下記”takaoフォント”をインストール
    sudo apt-get install fonts-takao
```

## 4．サンプルソフト（adrszLD-SSD1306SPI-mqtt.py）をダウンロード
```sh
    git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
    cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/
```

サンプルソフトの仕様は下記  
 - 入力：localhostのMQTTブローカから、TOPIC：adrszLDで文字列入力  
 - 出力：MQTTで入力した文字列を、自動スクロール４行で表示  
サンプルソフトを実行、初期表示文字が表示されることを確認、停止はCtrl+C  
    ```python3 adrszLD-SSD1306SPI-mqtt.py```  

## 5．Node-REDのサンプルソフト（adrszLD-node-sample.json）を、Node-REDにコピー

サンプルソフトの仕様は下記  
 - 入力：localhostのMQTTブローカTOPIC：adrszLDで文字列入力しＯＬＥＤに表示  
 - 出力：１分おきに時刻をＯＬＥＤに表示  


