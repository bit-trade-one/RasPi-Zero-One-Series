# ADRSZHB - USB拡張基板の使い方

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszhb/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZHB_USB_HUB/Schematics/rpizero_hub_v11_schematics.pdf)

本基板は、USB2.0のHubと互換性があります。  

下記に、基本的な使い方を示します。  

## ケーブルの接続
### アップストリームUSB端子の接続
- USB_US端子(USB Micro Bタイプメス)とRaspberry Pi ZeroのUSB端子(USB Micro Bタイプメス)を付属の変換ケーブル(USB Micor Bタイプオス⇒USB Aタイプメス)と市販のUSBケーブル(USB Micor Bタイプオス⇒USB Aタイプオス)を組合せて接続します。

### ダウンストリームUSB端子の接続

- USB1, 3, 4(Micro Bタイプメス)<BR>
付属の変換ケーブル(USB Micor Bタイプオス⇒USB Aタイプメス)と市販のUSBケーブルを使用して、お使いになるUSB機器と接続します  
- USB2(USB Aタイプメス）<BR>
市販のUSBケーブルを使用して、お使いになるUSB機器と接続します。

## 注意事項
接続されるUSB機器の電源は、Raspberry Pi ZEROのGPIOコネクタ(5V)より供給されます。
接続されるUSB機器の消費電力に応じてRaspberry Pi ZEROの電源には余裕のあるものをご使用ください。

## SHUTDOWNスイッチの使い方

シャットダウンの制御は、GPIO06(31番ピン)にて行っています。
[こちらの記事](http://bit-trade-one.co.jp/blog/201806301/)の「Node-REDの準備」の項の手順を一通り行っていただくか、Raspberry Pi ZEROのconfig.txtを設定していただく[(関連FAQを参照)](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZUP_Capacitor/FAQ.md)ことにより、ボタン押下によるシャットダウンを行うことができます。