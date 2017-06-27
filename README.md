# lawnbot

This is Slack bot that will display contributions on the GitHub. It works as a plugin on the [python-rtmbot](https://github.com/slackapi/python-rtmbot).

- number of 'emoji' shows contributions of week.
- emoji shows contributions of yesterday.
- default emoji setting
  `[0 1 2 3 4+] : [🍂 🌱 🌿 🌳 🌸]`

GitHubの芝生を観測できるSlack bot。
[python-rtmbot](https://github.com/slackapi/python-rtmbot)のプラグイン。

- 今週のcontributionを絵文字の数で表す
- 昨日のcontributionを絵文字の種類で表す
- デフォルトの絵文字設定
  `[0 1 2 3 4+] : [🍂 🌱 🌿 🌳 🌸]`

## usage

### conf.yml

setting

```
emoji:
  0: ':fallen_leaf:'
  1: ':seedling:'
  2: ':herb:'
  3: ':deciduous_tree:'
  4: ':cherry_blossom:'

level:
  '#eeeeee': 0,
  '#d6e685': 1,
  '#8cc665': 2,
  '#44a340': 3,
  '#1e6823': 4
  ```
