# ADRSZGR ゼロワン　9軸センサ拡張基板　サンプルPythonスクリプト/ライブラリ取り扱い説明書  

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszgr)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/3rd/ADRSZGR_9-Axis_Gyro/Schematics/rpizero_motion_V101_schematics.pdf)

## サンプルスクリプト ADRSZGR_Sample.pyについて  
このスクリプトは、ADRSZGR ゼロワン9軸センサ拡張基板専用 サンプルプログラムです。  
0.05秒間隔で9軸センサの値と、1ステップの経過時間を表示します。  

## ライブラリ関数

---------------------------------

## get_sense_value()

現在のセンサの値を読み取ります。  

返り値:(加速度X,Y,X,ジャイロX,Y,Z,磁気X,Y,Z)  

---------------------------------

## sensor_calib(time = 10)

ジャイロセンサのキャリブレーションを行います。  
※キャリブレーション中はセンサを動かさないでください。  

time:キャリブレーション用計測秒数  

---------------------------------

## GYRO(ac_conf = 0x03,gr_conf = 0x03)

9軸センサを初期化します。引数で加速度センサとジャイロセンサの計測範囲を指定します。  
初期化が終了すると、read_loop()関数を別スレッドで立ち上げ、計測を開始します。  

ac_conf:加速度計測範囲 ( 0: 2G ,1: 4G ,2: 8G ,3: 16G )  
gr_conf:ジャイロ計測範囲( 0: 250°/s ,1: 500°/s ,2: 1000°/s ,3: 2000°/s , )
