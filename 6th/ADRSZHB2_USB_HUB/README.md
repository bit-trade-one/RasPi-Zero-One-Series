# ADRSZHB2 - USB拡張ハブボードの使い方

### *製品ページは[こちら](http://bit-trade-one.co.jp/ad/adrszhb2)*

本基板は、USB2.0 USB HUBと互換性があります。  

下記に、基本的な使い方を示します。  

## コネクタの接続
### アップストリームUSB端子の接続
USBアップストリーム端子（USB Micro-Bタイプメス）をRaspberry Pi ZeroシリーズのUSB端子（USB Micro-Bタイプメス）に、付属のブリッジコネクタ（USB Micro-Bタイプオス⇒USB Micro-Bタイプオス）で接続します。

### ダウンストリームUSB端子の接続
ダウンストリーム端子（USB Aタイプメス）をお使いのUSB機器に接続します。

## USB-UARTシリアルインターフェイスの使い方
Raspberry Pi Zeroシリーズのシリアルインターフェース（GPIO14: TXDとGPIO15: RXD）を、CP2102 USB-UARTブリッジを使用してUSBケーブル（USB Micro-Bタイプオス⇒USB Aタイプオス等）でPCと接続できます。  
PCのターミナルソフトウェアを使用して、Raspberry Piのコンソール操作やシリアルモニタリングが可能です。  
このポートを使用する際は、PCにCP2102のデバイスドライバがインストールされている必要があります。インストールされていない場合は、[Silicon Labsのサイト](https://jp.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)からダウンロードしてインストールしてください。

## 注意事項
接続されるUSB機器の電源は、Raspberry Pi ZeroシリーズのGPIOコネクタ（5V）から供給されます。接続されるUSB機器の消費電力に応じて、Raspberry Pi Zeroシリーズの電源容量に注意してください。

