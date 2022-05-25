# ADRSZCM-クランプメータ拡張基板のインストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszcm/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZCM_Clamp_Meter/Schematics/rpizero_clamp_v11_schematics.pdf)

## ファイルリスト
- Readme.md  ［本文書］
- adrszCM-ads1115diff_IN0.py    [IN0をゲイン1倍で500回サンプリングし二乗平均値をアンペア単位で出力 Wオーダー測定用］
- adrszCM-ads1115diff_IN1.py    [IN1をゲイン1倍で500回サンプリングし二乗平均値をアンペア単位で出力 Wオーダー測定用］
- adrszCM-ads1115diff_IN1_G16.py[IN1をゲイン16倍で500回サンプリングし二乗平均値をアンペア単位で出力 mWオーダー測定用］
- old_samples                   [旧サンプルプログラム（非推奨）]



本基板のインターフェイスは、AdafluitのAdafruit_Python_ADS1x15モジュールと互換性があります。  
Adafruitのライブラリをインストールします。  
下記に、基本的な手順を示します。  

## 1.前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年5月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。 

## 2.サンプルソフトをダウンロード

```sh
    git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
```


## 3.pythonライブラリのインストール

```sh
    sudo pip3 install adafruit-circuitpython-ads1x15
```

## 4．サンプルソフトの実行

```sh
    cd RasPi-Zero-One-Series/4th/ADRSZCM_Clamp_Meter
    chmod +x *.py
    python3 adrszCM-ads1115diff_IN0.py
    # 計測結果はA（アンペア）単位で表示されます      
```
