# ADRSZEI　動作環境インストール

下記に、基本的な手順を示します。  

## 1. os関係のインストール確認
　ＯＳは、下記で動作確認、日本語環境、Ｉ２Ｃ、ＳＰＩインターフェイス許可  
　　　　2018-06-27-raspbian-stretch.zip  
　2018年8月時点で、最新版にして、基本モジュールをインストール  

```sh
　  sudo apt-get update  
    sudo apt-get upgrade  
    sudo apt-get install python-pip python3-pip  
```

## 2. node-redの最新版をインストール

```sh
    bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)  
    #node-redを自動起動  
    sudo systemctl enable nodered.service  
    sudo reboot  
    #node-redにMQTTブローカをインストール  
    ＃パレットの管理→ノードを追加→moscaを検索→ノードを追加  
    sudo reboot  
```

## 3. Pythonライブラリのインストール  

```sh
    #日本語を表示するために、下記”takaoフォント”をインストール
    sudo apt-get install fonts-takao
```

## 4. サンプルソフトをダウンロード
サンプルソフトは、下記ディレクトリに置くことを前提にサンプルソフトは動きます。  
異なるディレクトリに置くときは、適切に読み替え願います。  
　　　　```/home/pi/zeroone/5_2adrszEI/```  
  
### １）画像表示　adrszEI_sample_bmp.pyの仕様は下記

```sh
#     使い方：sudo python3 adrszEI_sample_bmp.py bmpファイル名
#　　　入力：bmpファイル名で画像ファイル入力
#　　　出力：画像表示　WIDTH = 250　HEIGHT = 128　
♯   必要により権限を付加
    sudo chmod 777 *
#   サンプルソフトを実行、初期表示文字が表示されることを確認、停止はコントロールC
    sudo python3 adrszEI_sample_bmp.py ADRSZEI-Displey_250x128.bmp
```

### ２）漢字表示　adrszEI_sample.pyの仕様は下記

```sh
#     使い方：Usage:sudo python3 adrszEI_sample.py  1行目文字列　2行目文字列　3行目文字列　4行目文字列
#　　　入力：1行目文字列　2行目文字列　3行目文字列　4行目文字列で文字列入力
#　　　出力：４行表示　　FONT_SIZE = 28　
♯   必要により権限を付加
    sudo chmod 777 *
#   サンプルソフトを実行、表示されることを確認、停止はコントロールC
    sudo python3 adrszEI_sample.py 123 456 789 012
```

### ３）名札表示　adrszEI_sample_namecard.pyの仕様は下記

```sh
#     使い方：sudo python3 adrszEI_sample_namecard.py  1行目文字列　2行目文字列
#　　　入力：1行目文字列（FONT_SIZE = 22）　2行目文字列（FONT_SIZE = 56）で文字列入力
#　　　出力：2行表示　　
♯   必要により権限を付加
    sudo chmod 777 *
#   サンプルソフトを実行、表示されることを確認、停止はコントロールC
    sudo python3 adrszEI_sample_namecard.py 123 456
```

## 5.ＮＯＤＥ－ＲＥＤのサンプルソフト（adrszEI_node-red_sample.json）を、ＮＯＤＥ－ＲＥＤにコピー

サンプルソフトの仕様は下記  
```sh
#　　　上記pythonのサンプルソフトを、ＮＯＤＥ－ＲＥＤから起動
```