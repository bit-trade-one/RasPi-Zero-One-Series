# Raspberry Pi Zero 専用拡張ボード　ラズパイ”ゼロワン”シリーズ　サンプルプログラム/ライブラリ公開リポジトリ

このリポジトリでは、Bit Trade Oneが発売している拡張ボードシリーズ”ゼロワン”用のサンプルプログラム・ライブラリ・説明書などを公開しています。  
[「ゼロワン」シリーズ　TOPページはこちら](http://bit-trade-one.co.jp/product/module/zeroone01top/)  

## ラインナップ一覧

|||||||
|-|-|-|-|-|-|
|第1弾</br>(18/7/6 発売)|[ADRSZBM</br>温湿度・気圧センサ]|[ADRSZPY</br>焦電型赤外線センサ]|[ADRSZRE</br>ロータリーエンコーダ]|[ADRSZSB</br>サーボ]|[ADRSZSN</br>ソレノイド]|
|第2弾</br>(18/8/24 発売)|[ADRSZIRR</br>赤外線受信]|[ADRSZLX</br>明るさセンサ]|[ADRSZRU</br>リレー回路]|[ADRSZSW</br>照光スイッチ]||
|第3弾</br>(18/9/21 発売)|[ADRSZGR</br>9軸センサ]|[ADRSZIRS</br>赤外線リモコン]|[ADRSZLD</br>OLED]|[ADRSZDAC</br>ハイレゾDAC]||
|第4弾</br>(18/12/21 発売)|[ADRSZHB</br>USBハブ]|[ADRSZGP</br>GPSモジュール]|[ADRSZUP</br>電源保持基板]|[ADRSZCM</br>クランプメータ]||
|第5弾</br>(19/2/22 発売)|[ADRSZOD</br>臭気センサ]|[ADRSZEI</br>電子ペーパーモジュール]|[ADRSZCS</br>カラーセンサ]|||

<!-- 01-1 参照一覧-->
[ADRSZBM</br>温湿度・気圧センサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZBM_Enviroment_Sensor)
[ADRSZPY</br>焦電型赤外線センサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZPY_Pyroelectric_Sensor)
[ADRSZRE</br>ロータリーエンコーダ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZRE_Rotary_Encoder)
[ADRSZSB</br>サーボ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZSB_Servo_Motor)
[ADRSZSN</br>ソレノイド]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZSN_Solenoid)
[ADRSZSW</br>照光スイッチ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZSW_Illuminated_Switch)

<!-- 01-2 参照一覧-->
[ADRSZIRR</br>赤外線受信]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZIRR_IR_Receiver)
[ADRSZLX</br>明るさセンサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZLX_Luminance_Sensor)
[ADRSZRU</br>リレー回路]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZRU_Relay_Unit)

<!-- 01-3 参照一覧-->
[ADRSZGR</br>9軸センサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZGR_9-Axis_Gyro)
[ADRSZIRS</br>赤外線リモコン]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZIRS_IR_Sender)
[ADRSZLD</br>OLED]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZLD_OLED_Display)
[ADRSZDAC</br>ハイレゾDAC]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZDAC_Hi-Rez_DAC)

<!-- 01-4 参照一覧-->
[ADRSZHB</br>USBハブ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZHB_USB_HUB)
[ADRSZGP</br>GPSモジュール]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZGP_GPS)
[ADRSZUP</br>電源保持基板]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZUP_Capacitor)
[ADRSZCM</br>クランプメータ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZCM_Clamp_Meter)

<!-- 01-5 参照一覧-->
[ADRSZOD</br>臭気センサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZOD_Odd_Sensor)
[ADRSZEI</br>電子ペーパーモジュール]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZEI_Electric_Paper)
[ADRSZCS</br>カラーセンサ]:(https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZCS_Color_Sensor)|||

![GPIO対応表](http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/07/image-2.png)


## シャットダウンボタンについて
ZeroOneシリーズ共通の「シャットダウンスイッチ」を動作させるには、各シリーズのNode-REDサンプル記載の方法と、下記の設定による方法があります。
```
sudo vi /boot/config.txt
dtoverlay=gpio-shutdown,gpio_pin=6
```