# ADRSZIRS-赤外線リモコン拡張基板のインストール

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszirs)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/3rd/ADRSZIRS_IR_Sender/Schematics/rpizero_irremote_v2_schematics.pdf)

## ファイルリスト
- Readme.md             ［本文書］
- 3_2adrszIRS-sample.py  [python3用サンプルプログラム バージョン：2018/7/27 v1.0]

## 前提条件
本動作確認は「RaspberryPI OS 32bit Bullseye 2022-04-04 Release」をイントールした後、2022年5月時点で最新版にupgradeした状態で実行しております。  
I2C・SPIインタフェースは、あらかじめraspi-configで許可した状態です。 

## 実行方法
### 赤外線コード読み取り
sample-data：ソニー	デジタルテレビ１	電源ボタン
```
    ./3_2adrszIRS-sample.py r
```  
受信結果：5B0018002E001800180018002E001800170018002E00190017001800170018002E00180018001800170018001700180017004F03

### 赤外線コード書き込み　
```
    ./3_2adrszIRS-sample.py w 5B0018002E001800180018002E001800170018002E00190017001800170018002E00180018001800170018001700180017004F03
```

### I2C関係内部コマンド

|コマンド名|番号|機能|
|:-|:-:|:-:|
|R1_log_start|0x15|赤外線記録 開始|
|R2_log_stop|0x25|赤外線記録 停止|
|R3_data_num_read|0x35|赤外線コード長 読み取り|
|R4_data_read|0x45|赤外線コード 読み取り|
|W1_data_num_write|0x19|赤外線コード長 書き込み|
|W2_data_write|0x29|赤外線コード 書き込み|
|W3_trans_req|0x39|赤外線送信 指令|
