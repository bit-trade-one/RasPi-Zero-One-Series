# Node-REDを用いた作例
本サンプルソフトの実行には、Node-REDとMQTTの基本知識が必要となります。  
以下に注意点・補足事項を記載します。  

## 1.OS関係のインストール確認
本サンプルソフトは「Rasbian GNU/Linux 9.6 stretch(2018-06-27-raspbian-stretch.img)」をイントールした後、2022年3月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。

```sh
    $ sudo apt-get update
    $ sudo apt-get install python-pip python3-pip
```

## 2．node-redの最新版をインストール

```sh
    $ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
    #node-redを自動起動
    $ sudo systemctl enable nodered.service 
    $ sudo reboot
```


### node-redにMQTTブローカをインストール  
パレットの管理→ノードを追加→moscaを検索→ノードを追加  

<img src="https://bit-trade-one.co.jp/wp/wp-content/uploads/2022/03/node_red.png" width="720px">  


### 再起動
```sh
     $ sudo reboot
```

## 3.adrszLD用のpythonライブラリのインストール

```sh
    $ git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    $ cd Adafruit_Python_SSD1306/
    $ sudo python3 setup.py install
    $ cd 
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
    $ cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/
```

サンプルソフトの仕様は下記  
 - 入力：localhostのMQTTブローカから、TOPIC：adrszLDで文字列入力  
 - 出力：MQTTで入力した文字列を、自動スクロール４行で表示  
サンプルソフトを実行、初期表示文字が表示されることを確認、停止はCtrl+C  
    ```python3 adrszLD-SSD1306SPI-mqtt.py```  

## 5．Node-REDのサンプルソフト（adrszLD-node-sample.json）を、Node-REDにコピー

 

### Mosquitto(MQTT Broker)のインストール  

本サンプルソフトを動作させるには、Publisher（発信者）が必要となります。あらかじめMosquittoをインストールしてください。  
詳細は、http://mosquitto.org/blog/2013/01/mosquitto-debian-repository/を参照してください。

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

```sh
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


