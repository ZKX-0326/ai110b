# 人工智慧第十二週筆記
## 反傳遞算法
反傳遞是一種與最優化方法 (如梯度下降法) 結合使用的方法，該方法對網路中所有權重計算損失函數的梯度。這個梯度會反饋給最優化方法，用來更新權值以最小化損失函數。   
反傳遞要求對每個輸入值想得到已知輸出，來計算損失函數梯度。因此它通常被認為是一種監督式學習的方法，可以對每層迭代計算梯度，另外反傳遞要求神經元的啟動函數是可微分的。