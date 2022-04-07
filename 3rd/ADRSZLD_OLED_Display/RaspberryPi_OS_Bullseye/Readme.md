# adrszLD-ゼロワン OLED拡張基板

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszld)*

## ファイルリスト
- Readme.md  ［本文書］
- adrszLD_test.py ［動作確認用サンプルソフト］
- [Node-RED_Readme.md ［Node-REDを用いた作例です］](Node-RED_Readme.md)
- adrszLD-SSD1306SPI-mqtt.py ［Node-REDサンプルソフト］
- adrszLD-node-sample.json ［Node-REDノードサンプル］

## はじめに
adrszLD OLEDではAdafruit Python SSD1306ライブラリの使用を前提としていますが、こちらは現在deprecated（非推奨）となっております。
Adafruitでは、CircuitPyton用のライブラリを推奨とのことですので、OLEDモジュールのサンプルソフトをAdafruit CircuitPythonベースに変更します。

## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-01-28 Release」をイントールした後、2022年4月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。  

## adrszLD用のpythonライブラリのインストール

```sh
    #Adafruit CircuitPython用SSD1306モジュールのインストール
    $ sudo pip3 install adafruit-circuitpython-ssd1306
    #python3にCircuitPythonのAPIを提供するblinkaのインストール
    $ sudo pip3 install adafruit-blinka
    #画像ライブラリのインストール
    $ sudo pip3 install pillow
    #日本語を表示するために、下記”takaoフォント”をインストール
    $ sudo apt-get install fonts-takao
```

## サンプルソフト（adrszLD_test.py）をダウンロード
```sh
    $ git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
    $ cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/RaspberryPi_OS_Bullseye
```

## 以下のコマンドでサンプルソフトを実行し、初期文字が表示されることを確認してください。

```sh
    $ python3 adrszLD_test.py
```