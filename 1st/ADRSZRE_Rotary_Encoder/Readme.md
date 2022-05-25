# ADRSZRE ロータリーエンコーダ拡張基板 サンプルPythonスクリプト取り扱い説明書  

### *製品ページは[こちら](http://bit-trade-one.co.jp/product/module/adrszre)*

### *回路図は[こちら](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/1st/ADRSZRE_Rotary_Encoder/Schematics/rpizero_encoder_v11_schematics.pdf)*

## サンプルスクリプト ADRSZRE_Sample.pyについて  

このスクリプトは、ADRSZRE ゼロワンエンコーダ拡張基板専用 エンコーダ値読み取りサンプルプログラムです。  
コマンドを受け付け、エンコーダ値の読み取りとリセットを行います。  

|操作|コマンド|値など|
|:-:|:-:|:-|
|エンコーダ値読み取り|v|エンコーダカウント数(符号あり2バイト、-32768~32767)|
|エンコーダ値リセット|r|エンコーダカウント数を0にセット|
|スクリプト終了|q|ターミナルに戻る|  
||||

## 関数

--------------------------

### Get_encoder_value()

現在のエンコーダカウント数を読み取ります。  
返り値:エンコーダカウント数(符号あり2バイト、-32768~32767)

--------------------------

### Encoder_Reset()

エンコーダカウント数を0にリセットします。

## 基板ファームウェア RasPiZero_EncoderFirmware_20180511.zip について

このファームウェアは以下の環境で開発しています。  

 - MPLAB IDE v8.92
 - MPLIB Librarian v5.00
 - MPLAB C18 Compiler v3.47
 - MPLINK Object Linker v5.00
 - MPASM Assembler v5.54
