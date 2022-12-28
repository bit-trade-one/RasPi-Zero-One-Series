# ADRSZOD-臭気センサ拡張基板のインストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszod/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/5th/ADRSZOD_Odd_Sensor/Schematics/rpizero_airsens_v1_schematics.pdf)

## ファイルリスト
- Readme.md                    ［本文書］
- adrszOD-sample.py             [サンプルプログラム］
- FAQ.md                        [FAQ］
- old_samples                   [旧サンプルプログラム（非推奨）]


## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年5月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。 

## 概要
ADRSZOD基板は、臭気センサが実装され、ラズパイzeroとはI2Cシリアルで接続されています。
Pythonのサンプルソフトでは、Ch1が臭気センサからの出力となります。  
搭載する臭気センサにつきましては、各物質ごとの濃度は測定できません。ご了承ください。  
下記に、基本的なインストール手順を示します。

## サンプルソフトのダウンロード

```sh
    git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
```

## サンプルソフトの実行

```sh
    cd RasPi-Zero-One-Series/5th/ADRSZOD_Odd_Sensor
    chmod +x *.py
    python3 adrszOD-sample.py      
```
ch1に出力される値が、臭気センサーの出力電圧(V）となります。
センサ付近にアルコールなどを近づけるとこの値が変化します。
