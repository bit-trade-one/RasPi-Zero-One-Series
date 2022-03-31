# adrszLD-ゼロワン OLED拡張基板

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszld)*

## ファイルリスト
- Readme.md  ［本文章］
- [Node-RED_Readme.md ［Node-REDを用いた作例です］](Node-RED_Readme.md)
- adrszLD-SSD1306SPI-mqtt.py ［サンプルソフト］
- adrszLD-node-sample.json ［ノードサンプル］


## 動作確認
本動作確認は「Rasbian GNU/Linux 9.6 stretch(2018-06-27-raspbian-stretch.img)」をイントールした後、2022年3月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。  
  
adrszLDは、インターフェイスがadafluitのSSD1306 OLEDモジュールと互換性があります。  
adafruitのライブラリ等をインストールします。 

## adrszLD用のpythonライブラリのインストール

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

## サンプルソフト（adrszLD-SSD1306SPI-mqtt.py）をダウンロード
```sh
    $ git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
    $ cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/
```

## 以下のコマンドでサンプルソフトを実行し、初期文字が表示されることを確認してください。

```sh
    $ python3 adrszLD-SSD1306SPI-mqtt.py
```