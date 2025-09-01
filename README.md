# bilibili-game-sdk-reverse

## 项目描述

Blibili 游戏登录 sdk 逆向,目前仅对`灰烬战线`进行过测试,并不保证其他游戏能使用。项目仅供学习使用,请勿用于非法用途,不提供具体参数细节

## 环境安装

在代码开发前,需要执行以下代码,让模块安装到当前环境中

```shell
pip install -e .
```

## 修改配置文件

在不同游戏登录时需要对`src/bili_game_sdk/config/sdkConfig.py`文件中的`BSGameSdkConfig`类修改为对应游戏的信息,这一部分信息需要自己根据游戏进行逆向

## 修改设备信息(可选)

在激活`bd_info`这个 cookie 字段时,会用到移动端的设备信息,这里仅仅对`wifi mac`相关的参数进行自动获取填写,其他参数可自行在`src/bili_game_sdk/api.py`中的`client_activate`方法中的`device_info`中进行修改

## 登录流程

使用例子可看`/tests/test_login.py`文件

1. 调用`client_activate`方法获取激活之后的`bd_id`, `bd_id`可多次进行使用,具体能用多少次,未进行测试
2. 调用`external_issue_cipher_v3`方法,获得登录时需要的密钥和 hash 信息
3. 调用`external_login_v3`方法,获得登录信息

### 登录成功返回值示例

```json
{
  "requestId": "1df35631e83f40a5a1abfaa9174769a9",
  "timestamp": "时间戳",
  "code": 0,
  "auth_name": "",
  "realname_verified": 1,
  "remind_status": 0,
  "h5_paid_download": 1,
  "h5_paid_download_sign": "4bf66ef578488b4d179af531ca4badec",
  "access_key": "xxxxxx_sh",
  "uid": 000000000, // Your uid
  "game_open_id": null,
  "game_open_id_enable": false,
  "expires": 1759303442000,
  "face": "",
  "s_face": null,
  "uname": "user_name",
  "server_message": ""
}
```

若出现其他的则为登录失败,若提示需要验证码,则大概率是`bd_id`未注册成功,需要自行抓包测试修改

## 项目打包为模块

```shell
python -m build
```
