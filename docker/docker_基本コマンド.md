# Docker基本コマンド(ぐぐれ)  
## イメージ関連
* イメージのダウンロード  
docker pull [オプション] イメージ名[:タグ名]  
(例) docker pull nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

* イメージの一覧表示  
docker images [オプション] [リポジトリ名]  
(例) docker images

* イメージの検索  
docker search [オプション] 検索キーワード  
(例) docker search cuda10.0

* イメージの削除  
docker rmi [オプション] イメージID or イメージ名  
(例) docker rmi nginx

* イメージのアップロード  
docker push イメージ名[:タグ名]  
docker rmi nginx

* イメージの検索  
docker search [オプション] 検索キーワード  
(例) docker search cuda10.0
docker push kojima/webserver:1.0

## コンテナ関連
* コンテナの生成/起動  
docker run [オプション] イメージ名[:タグ名] [引数]  
(例) docker run -it --name cuda10sig4 nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

* コンテナの一覧表示  
docker ps [オプション]  
(例) docker ps -a

* コンテナの起動  
docker start [オプション] コンテナID [コンテナID]  
(例) docker start ed998b3cfd76

* コンテナの停止  
docker stop [オプション] コンテナID [コンテナID]  
(例) docker stop ed998b3cfd76

* コンテナの再起動  
docker restart [オプション] コンテナID [コンテナID]  
(例) docker restart ed998b3cfd76

* コンテナの削除  
docker rm [オプション] コンテナID [コンテナID]  
(例) docker rm ed998b3cfd76


## その他
* Dockerのバージョン確認  
docker version

* コンテナからイメージの作成  
docker commit [オプション] コンテナID [イメージ名[:タグ名]]  

* Dockerfileからイメージを作成
docker build -t [生成するイメージ名]:[タグ名] [Dockerfileの場所]  
(例) docker build -t sig4cuda10 .


メモ
#/var/lib/docker/overlay2/bba21eeaf06ce8bafcc58c5befba1d4e862396c18c6499e04db87dcb1e5446de/diff/hello
