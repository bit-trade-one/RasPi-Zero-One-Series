# ADRSZDAC-ハイレゾDAC拡張基板のインストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszdac)*.

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/3rd/ADRSZDAC_Hi-Rez_DAC/Schematics/rpizero_dac_v101_schematics.pdf)

## ファイルリスト
- Readme.md             ［本文書］
- FAQ.md                 [FAQ］
- toujyo.wav             [サンプル音源］

## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年5月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。 

※ Raspberry Pi 5を使用される場合は、FAQを参照してください。

## 初期セットアップ方法

 1. /boot/config.txtに、以下の行を追記します。 
```
    dtparam=i2s=on  
    dtoverlay=hifiberry-dacplus,24db_digital_gain  
```

 2. /boot/config.txtの以下の行をコメントアウト(先頭に#を付ける)します。  
```
    dtparam=audio=on  
        ↓  
    #dtparam=audio=on  
```
コマンドラインによる音声再生・音量調節  

## 音声再生(WAVファイルのみ)

aplay --device=hw:x,x ＜音声ファイル名.wav＞  

```
    # カード番号、デバイス番号を確認する
    aplay -l
    # カード番号:1 デバイ番号:0の場合
    aplay --device=hw:1,0 toujyo.wav
    
```

## 音量調節
```
    # 必要に応じてカード番号を指定する
    amixer -c1 set 'Digital' ＜音量:パーセンテージ＞%
```