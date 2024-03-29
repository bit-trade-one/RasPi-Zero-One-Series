# ADRSZUP ゼロワン 電源保持基板　説明書

### *製品ページは[こちら](http://bit-trade-one.co.jp/adrszup/)*

### [回路図](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZUP_Capacitor/Schematics/rpizero_ups_v12_schematics.pdf)

## 本製品について

本製品は、Raspberry Pi ZEROに装着し通常時にキャパシタに電荷を蓄積することで、外部電源切断時にRaspberry Piがシャットダウンするまで電源を保持するための基板です。

## 使い方

Raspberry Pi ZEROのGPIOに接続し、電源保持基板上のUSB端子にのみに給電を行ってください。

（Raspberry Pi ZEROの電源端子には電源を接続しないでください。）

充電状況に応じて、基板上のCHARGEランプの明るさが変化します。満充電時に最大光量となります。 

(キャパシタの残容量によっては満充電になるまでに30分から1時間程度かかる場合があります。) 

シャットダウンの制御は、GPIO06(31番ピン、SHUTDOWNボタンと共通)にて行っています。
外部電源接続時にHi、切断時にLoレベルとなります。
[こちらの記事](http://bit-trade-one.co.jp/blog/201806301/)の「Node-REDの準備」の項の手順を一通り行っていただくか、Raspberry Pi ZEROのconfig.txtを設定していただく[(FAQを参照)](https://github.com/bit-trade-one/RasPi-Zero-One-Series/blob/master/4th/ADRSZUP_Capacitor/FAQ.md)ことにより、外部電源切断時に即座にシャットダウンを行うシステムを構築できます。

## 注意
- 本基板とRaspberry Pi ZEROの両方に電源を接続しないでください。シャットダウンが正常に動作しない場合があります。

- 本基板では、コンセントなどの主電源からの電力供給が途絶えた場合に即座にシャットダウン動作を行い、OSが終了するまで電源を保持することを目的としています。
長時間電源を供給し、作業を続行するような動作は保証いたしかねますことご了承ください。

- 接続するACアダプタは、使用するRaspberry Pi ZEROの推奨電流値の物を使用してください。

- 基板面に電位差を持つ端子が露出している箇所がございます。金属など導電体との接触には十分ご注意ください。
