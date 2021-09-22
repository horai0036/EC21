# NVIDIA Docker環境の作り方
## インストールまで
1. NVIIDIAドライバのインストール  
鯖缶が各サーバに入れてくれている，もしくは標準のDriverが存在する  
以下のコマンドで確認可能  
```linux:nvidia-smi
nvidia-smi
```

2. Dockerのインストール  
以下の公式サイトの通りに導入する  
[LinuxへのDocker Engine導入ガイド](http://docs.docker.jp/linux/index.html)

3. NVIDIA Container Toolkitのインストール  
**CentosやRHELではインストール方法が違うので各自で調べてください**  
Ubuntuにnvidia-docker2パッケージをインストールするときは以下のコマンド脳死コピペで基本OK  
`distribution=$(. /etc/os-release;echo $ID$VERSION_ID)`
`curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -`
`curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list`
`sudo apt-get update`
`sudo apt-get install -y nvidia-docker2`
`sudo systemctl restart docker`  
以上でインストールは完了  
以下のサイトにこれらのコマンドについて詳しく書いてあるので，何か問題があったらこのサイトを見てほしい．  
[NVIDIA Docker って今どうなってるの？ (20.09 版)](https://medium.com/nvidiajapan/nvidia-docker-%E3%81%A3%E3%81%A6%E4%BB%8A%E3%81%A9%E3%81%86%E3%81%AA%E3%81%A3%E3%81%A6%E3%82%8B%E3%81%AE-20-09-%E7%89%88-558fae883f44)

## GPU付きコンテナの起動方法
CUDA10.0&Ubuntu16.04をインストールしたときの確認方法  
以下のコマンドのどれかを実行するとnvidia/cuda:10.0-cudnn7-devel-ubuntu16.04がインストールされる
```
# すべての GPU を使用
* docker run --gpus all --rm nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 nvidia-smi
# 2 つの GPU を使用(※ GPU ID 0 から順番に選択される)
* docker run --gpus 2 --rm nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 nvidia-smi
# GPU ID または UUID を指定して使用 (クォートが冗長に見えるけど必要)
* docker run --gpus '"device=0,1"' --rm nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 nvidia-smi
* docker run --gpus '"device=UUID-ABCDEF,1"' --rm nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 nvidia-smi
```


バージョン名について
- base: 最小構成
- runtime: baseを拡張したもの
- devel: runtimeを拡張したもの  

実行
* コンテナ実行例  
sudo docker run -it --gpus all --name sig4cuda10 -v /home/kojima:/workspace nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

* コンテナ実行テンプレ  
sudo docker run -it --gpus all --name (コンテナの名前) -v (マウントしたいローカル側の場所):(docker側の場所) nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

* 解説  
--gpus : gpuの使用枚数
--name : コンテナの名前
-v xxx:yyy : xxx=ホスト側のディレクトリ，yyy=コンテナ側のディレクトリ(/workspaceで良い)
nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04 : コンテナの環境