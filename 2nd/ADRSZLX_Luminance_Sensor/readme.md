
# adrszLX_sample.py  

### *製品ページは[こちら](http://bit-trade-one.co.jp/product/module/adrszlx)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/2nd/ADRSZLX_Luminance_Sensor/Schematics/rpizero_light_schematics.pdf)

バージョン：2018/6/8 v1.0  python3用  

ビット・トレード・ワン社提供のzerooneシリーズ 明るさセンサモジュール(型番：ADRSZLX)用の例題プログラム  
著作権者:(C) 2015 ビット・トレード・ワン社  
ライセンス: ADL(Assembly Desk License)  

実行方法： ./adrszLX_sample.py  
実行すると　照度：lumi　近接距離：proxi　を下記のように出力します。  
```実行結果　　{'lumi': 2555 ,'proxi': 2281} ```  
照度[lumi]　は測定光度範囲：10～16383[Lux]  
 - センサから採れる数値は、ambient Light Signal(cts)値です。  
数値は、データシートに両対数グラフで表示されています。  
両対数グラフは、ambient Light Signal(cts)対、Ambient Light Value(lx)です。  

グラフより、lx値を換算し、弊社で実測しましてみました。  
机の上の、蛍光灯をつけると：1500lux、消すと：750lux程度でした。  
 - 近接距離：proxi　測定距離範囲: 1～200 mm　最適な範囲: 10～150 mm（Adafruit調べ）  

弊社にて実測したところ、10ｍｍ～30ｍｍ程度で、値が8000～2500程度変化しました  
数値は、データシートに対数グラフで表示されているので、数値と、距離の換算は困難です  
数値が2500以上なら30ｍｍ以内に、物体がある程度の使用法になると思われます。  

Distributed with a free-will license.  
Use it any way you want, profit or free, provided it fits in the licenses of its associated works.  
VCNL4010  
This code is designed to work with the VCNL4010_I2CS I2C Mini Module available from ControlEverything.com.  
https://www.controleverything.com/content/Light?sku=VCNL4010_I2CS#tabs-0-product_tabset-2  
