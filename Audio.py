#!/usr/bin/env python

# ライブラリの読込
import pyaudio
import wave
import numpy as np
from datetime import datetime
from plyer import notification
import time

# 音データフォーマット
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

# 閾値
threshold = 0.3

flag = 0

# 音の取込開始
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
)

cnt = 0
print("Start!!")

while True:
  # # 音データの取得
  data = stream.read(chunk)
  # # ndarrayに変換
  x = np.frombuffer(data, dtype="int16") / 32768.0

  # # 閾値以上の場合は通知
  if x.max() > threshold:
    if flag == 0:
      flag = 1
      print("arrart!!")
      notification.notify(
      title = "警告",
      message="声がでけぇ! 静かにしやがれ!!!",
      timeout=2
      )
      time.sleep(5)
      flag = 0

# stream.close()
# p.terminate()