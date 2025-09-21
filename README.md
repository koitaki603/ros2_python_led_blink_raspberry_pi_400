# ros2_python_led_blink_raspberry_pi_400

ROS 2 + Python を使って、Raspberry Pi 400 で LED を点滅させるサンプルプロジェクトです。

---

## 🔍 プロジェクト構成

ros2_python_led_blink_raspberry_pi_400/
└── src/
└── led_controller/
├── led_controller/
│ ├── init.py
│ └── led_blink_node.py ← メインのノード（LED制御）
├── resource/
├── test/
├── package.xml
└── setup.py

---

## 🔧 使用ハードウェア

- Raspberry Pi（Pi 4, Pi 400 など GPIO が使えるモデル）
- LED × 1
- 抵抗（220Ω〜330Ω程度）
- ブレッドボード & ジャンパー線

---

## ⚡ 回路図（簡易）

GPIO18 (ピン12) ──→───[抵抗]───→───|>|───→─── GND (ピン6)
（LED）


- GPIO18（BCM番号）を出力ピンとして使用
- LEDと抵抗を直列に接続し、GNDへ

---

## 🛠 セットアップ手順

以下はこのプロジェクトを始めるための手順です：

```bash
# 1. リポジトリをクローン
git clone https://github.com/koitaki603/ros2_python_led_blink_raspberry_pi_400.git
cd ros2_python_led_blink_raspberry_pi_400

# 2. 依存関係をインストール
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# 3. ワークスペースをビルド
colcon build

# 4. ビルド成果物を環境変数に反映
source install/setup.bash

