# ADRSZDAC ラズパイハイレゾDAC説明書

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszdac)*.

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/3rd/ADRSZDAC_Hi-Rez_DAC/Schematics/rpizero_dac_v101_schematics.pdf)

### 初期セットアップ方法

 1. /boot/config.txtに、以下の行を追記します。  
dtparam=i2s=on  
dtoverlay=hifiberry-dacplus,24db_digital_gain  

 2. /boot/config.txtの以下の行をコメントアウト(先頭に#を付ける)します。  
dtparam=audio=on  
↓  
\#dtparam=audio=on  

コマンドラインによる音声再生・音量調節  

### 音声再生(wavのみ)

aplay --device=hw:0,0 ＜音声ファイル名.wav＞  

### 音量調節

amixer set 'Digital' ＜音量:パーセンテージ＞%
