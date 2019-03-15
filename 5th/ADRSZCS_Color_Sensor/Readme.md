# ゼロワンシリーズ　ADRSZCS カラーセンサ仕様手順書

この基板の仕様は以下のとおりです。  
|||  
|-|-|  
|カラーセンサ|ZC-CLS381RGB|  
|測定データ|Red、Green、Blue、IR|  
|分解能|16　to　20　bit|  
|測定モード|ALS：周囲光、CS：カラー|  
|使用GPIO|2(SDA),3(SCL),6(SHUTDOWN),</br>18(LED),23(INT)|  

下記に、基本的な手順を示します。  

## 1.os関係のインストール確認

　ＯＳは、下記で動作確認、日本語環境、Ｉ２Ｃ、ＳＰＩインターフェイス許可  
　　　　2018-11-18-raspbian-stretch.zip  
　2018年12月時点で、最新版にして、基本モジュールをインストール  

```sh
　  sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python-pip python3-pip
```

## 2.node-redの最新版をインストール

```sh
    bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
    #node-redを自動起動
    sudo systemctl enable nodered.service 
    sudo reboot
    #node-redにMQTTブローカをインストール
    ＃パレットの管理→ノードを追加→moscaを検索→ノードを追加
    sudo reboot
```

## 3.pythonライブラリのインストール

```sh
#open CV をpython2でインストールします（現時点でpython3はうまくインストールできませんでした）
#ラズハ゜イ　ＺＥＲＯにインストールするにはかなり時間がかかります。
sudo apt-get update
sudo apt-get upgrade
#Python2でのapt-getで入るPythonライブラリ
#Numpy、PIL、Pandas、Matplotlibは、それぞれ以下のコマンドの上から順に対応しています。
$ sudo apt-get install python-numpy
$ sudo apt-get install python-imaging
$ sudo apt-get install python-pandas
$ sudo apt-get install python-matplotlib
#Open CVは、以下2行です。
$ sudo apt-get install libopencv-dev
$ sudo apt-get install python-opencv
```

## 4.pythonのサンプルソフトをダウンロード

サンプルソフトは、下記ディレクトリに置くことを前提にサンプルソフトは動きます。  
異なるディレクトリに置くときは、適切に読み替え願います。  
　　　　```/home/pi/zeroone/5_1adrszCS/```

### １）周囲光測定　adrszCS_ALSmode_sample.pyの仕様は下記

```sh
sudo python /home/pi/zeroone/5_1adrszCS/adrszCS_ALSmode_sample.py
#　　　入力：ALSモードで、周囲光を測定
#　　　出力：周囲光
```

### ２）ＲＧＢ測定　adrszCS_CSmode_sample.pyの仕様は下記

```sh
sudo python /home/pi/zeroone/5_1adrszCS/adrszCS_CSmode_sample.py
#　　　入力：ＣＳモードで、周囲光を測定
#　　　出力：測定データ　　Red、Green、Blue、IR
```

### ３）ＨＳＶ（ＲＧＢよりopenCVで変換）測定　adrszCS_CSmodeHSV_sample.pyの仕様は下記

```sh
sudo python /home/pi/zeroone/5_1adrszCS/adrszCS_CSmode_sample.py
#　　　入力：1行目文字列（FONT_SIZE = 22）　2行目文字列（FONT_SIZE = 56）で文字列入力
#　　　出力：ＨＳＶ値
```

## 5.ＮＯＤＥ－ＲＥＤのサンプルソフト（adrszCS_sample****.json）を、ＮＯＤＥ－０ＲＥＤにコピー

サンプルソフトの仕様は下記

- 上記3種のpythonのサンプルソフトを、ＮＯＤＥ－ＲＥＤから起動
- dashboardにグラフ表示
