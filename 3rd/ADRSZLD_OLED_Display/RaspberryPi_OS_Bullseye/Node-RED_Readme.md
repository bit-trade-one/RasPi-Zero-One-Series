# Node-REDを用いた作例 RaspberryPI OS 32bit Bullseye版
本サンプルソフトの実行には、Node-REDとMQTTの基本知識が必要となります。  
以下に注意点・補足事項を記載します。  

## 1.前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-01-28 Release」をイントールした後、2022年4月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。 

## 2．Node-REDのインストール

```sh
    $ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
    #node-redを自動起動する場合は下記を実行してください
    $ sudo systemctl enable nodered.service 
    $ sudo reboot
```

### NODE-Redにnode-red-contrib-mqtt-brokerをインストール  
NODE-Red起動後、ハンバーガーメニューからパレットの管理→ノードを追加→moscaを検索→ノードを追加します。
インストールには長時間かかる場合があります。

<img src="https://bit-trade-one.co.jp/wp/wp-content/uploads/2022/03/node_red.png" width="720px">  


### 再起動
```sh
     $ sudo reboot
```

## 3.adrszLD用のpythonライブラリのインストール

```sh
    #Adafruit CircuitPython用SSD1306モジュールのインストール
    $ sudo pip3 install adafruit-circuitpython-ssd1306
    #python3にCircuitPythonのAPIを提供するblinkaのインストール
    $ sudo pip3 install adafruit-blinka
    #画像ライブラリのインストール
    $ sudo pip3 install pillow
    #MQTTクライアントのインストール
    $ git clone https://github.com/eclipse/paho.mqtt.python.git
    $ cd paho.mqtt.python
    $ sudo python3 setup.py install
    $ cd
    #日本語を表示するために、下記”takaoフォント”をインストール
    $ sudo apt-get install fonts-takao
```

## 4．サンプルソフト（adrszLD-SSD1306SPI-mqtt.py）をダウンロード
```sh
    $ git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
    $ cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/aspberryPi_OS_Bullseye
```

サンプルソフトの仕様は下記  
 - 入力：localhostのMQTTブローカから、TOPIC：adrszLDで文字列入力  
 - 出力：MQTTで入力した文字列を、自動スクロール４行で表示  
サンプルソフトを実行、初期表示文字が表示されることを確認、停止はCtrl+C  
    ```python3 adrszLD-SSD1306SPI-mqtt.py```  

## 5．Node-REDのサンプルソフト（adrszLD-node-sample.json）を、Node-REDにコピー

 

### Mosquitto(MQTT Broker)のインストール  

本サンプルソフトを動作させるには、MQTT BrokerBrokerとPublisher（発信者）が必要となります。あらかじめMosquittoをインストールしてください。  
詳細は、http://mosquitto.org/blog/2013/01/mosquitto-debian-repository/ を参照してください。

### GPG鍵のインストール
```sh
$ sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key 
$ sudo apt-key add mosquitto-repo.gpg.key
```

### mosquitto-jessie.listのインストール

```sh
$ sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list -O /etc/apt/sources.list.d/mosquitto-jessie.list
```

### mosquittoのインストール  

```shs
$ sudo apt-get update
$ sudo apt-get install mosquitto mosquitto-clients
```

### サンプルソフト（adrszLD-node-sample.json）を、Node-REDにコピー

クリップボード経由等で、Node-RED上にサンプルソフトを読み込んでください。

### execノードの編集

およびPythonスクリプトのパスをインストールしたフォルダに合わせて編集してください

### メッセージの発信

以下のコマンドで発信したメッセージがOLEDにスクロール表示されます。

```sh
$ mosquitto_pub -h localhost -t adrszLD -m "メッセージ"
```


