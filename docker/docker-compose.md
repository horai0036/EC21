# Docker-composeのやり方
## Docker-composeのインストール~使えるまで
### Docker-composeのインストール
```
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### Docker-composeのバージョン確認
```
docker-compose --version
```

## Docker-compose起動
.ymlファイルを用いてdocker-composeを行う．
起動コマンドは
```
docker-compose up -d
```
確認は
```
docker-compose ps
```

## Docker-compose.ymlの作り方1(複数イメージを組み合わせる)
```
例
version: '3'
services:

  wordpress:
    image: wordpress
    container_name: some-wordpress
    restart: always
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_PASSWORD: my-secret-pw

  mysql:
    image: mysql:5.7
    container_name: some-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw「
```

* <font color="Green">version</font>  
    docker-composeで使用するバージョン

* <font color="Green">servise</font>  
    アプリケーションを使うための各要素  
    例だとtomcatがserviceとして定義されている．  
    サービス名は何でもいい ここではwordpress,mysqlという名前ｓ

    | 項目        | 意味                                                   | リファレンスリンク                                           | 
    | ----------- | ------------------------------------------------------ | ------------------------------------------------------------ | 
    | restart     | 実行時に再起動するかどうか                             | https://docs.docker.com/compose/compose-file/#restart        | 
    | environment | DBについての環境変数設定                               | https://docs.docker.com/compose/compose-file/#environment    | 
    | ports       | DBのDockerImageを立ち上げる際のポート番号              | https://docs.docker.com/compose/compose-file/#ports          | 
    | volumes     | マウントする設定ファイルのパスを指定                   | https://docs.docker.com/compose/compose-file/#short-syntax-3 | 
    | build       | ComposeFileを実行し、ビルドされるときのpath            | https://docs.docker.com/compose/compose-file/#build          | 
    | depends_on  | Service同士の依存関係                                  | https://docs.docker.com/compose/compose-file/#depends_on     | 
    | entrypoint  | デフォルトのentrypointを上書きする                     | https://docs.docker.com/compose/compose-file/#entrypoint     | 
    | driver      | ボリュームに使用するドライバ(動かすための接続先)の指定 | https://docs.docker.com/compose/compose-file/#driver         | 


* <font color="Green">image</font>  
    使用するimage  
    ローカルになかったらpullされる

* <font color="Green">build</font>  
    dockerfileがあるディレクトリのパス  
    相対パスはymlファイルからの相対パス





## Docker-compose.ymlの作り方2
```
例
version: '3'
services:
  tomcat:
    build: ./tomcat
    image: tomcat-image
    container_name: tomcat1
    ports:
      - 8081:8080
    volumes:
      - ./tomcat/share/logs:/share/logs
```

```
version: '3'←dockerのバージョン
services:
  tomcat:
    build: ./tomcat
    image: tomcat-image
    container_name: tomcat1
    ports:
      - 8081:8080
    volumes:
      - ./tomcat/share/logs:/share/logs
```








