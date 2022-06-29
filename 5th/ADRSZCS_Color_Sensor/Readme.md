# ゼロワンシリーズ　ADRSZCS カラーセンサ使用手順書

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszcs/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/5th/ADRSZCS_Color_Sensor/Schematics/rpizero_color_v21_schematics.pdf)

## ファイルリスト
* Readme.md ［本文書］
* adrszCS_ALSmode_sample.py［サンプルプログラム］
* adrszCS_CSmode_sample.py［サンプルプログラム］
* ZC-CLS381RGB.pdf[カラーセンサデータシート]

## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年6月時点で最新版にupgradeした状態で実行しております。
)
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。

```sh
sudo apt-get update 
sudo apt-get upgrade
sudo pip install --upgrade pip
```


## 基本仕様
本基板の基本的な仕様は以下のとおりです。  

|||  
|:-:|:-|  
|カラーセンサ|ZC-CLS381RGB|  
|測定データ|Red、Green、Blue、IR|  
|分解能|16　to　20　bit|  
|測定モード|ALS：周囲光、CS：カラー|  
|使用GPIO|2(SDA),3(SCL),6(SHUTDOWN),</br>18(LED),23(INT)|  

下記に、基本的な使用方法を示します。  

## サンプルソフトのダウンロード

サンプルソフトは、下記ディレクトリに置くことを前提にサンプルソフトは動きます。  
異なるディレクトリに置くときは、適切に読み替え願います。 

　　　　```/home/pi/zeroone/5_1adrszCS/```

```sh
cd ~
git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
mkdir zeroone
cd zeroone
mkdir 5_1adrszCS
cd 5_1adrszCS
cp -r  ~/RasPi-Zero-One-Series/5th/ADRSZCS_Color_Sensor/* .
```
## １．動作確認  
動作確認用として、以下の2つのスクリプトを提供しています。測定データが表示されることを確認してください。

### １）周囲光測定(adrszCS_ALSmode_sample.py)
```sh
python /home/pi/zeroone/5_1adrszCS/adrszCS_ALSmode_sample.py
#　　　入力：ALSモードで、周囲光を測定
#　　　出力：周囲光
```

### ２）ＲＧＢ測定(adrszCS_CSmode_sample.py)

```sh
python /home/pi/zeroone/5_1adrszCS/adrszCS_CSmode_sample.py
#　　　入力：ＣＳモードで、周囲光を測定
#　　　出力：測定データ　　Red、Green、Blue、IR
```

## ２．測定用白色LEDについて

基板上のLEDは、GPIO18を制御して点灯をコントロールしてください。<BR>
Hiで点灯、Loで消灯、またPWMにて調光制御が可能です。

```sh
# LED ON
raspi-gpio set 18 op dh
# LED OFF
raspi-gpio set 18 op dl
```