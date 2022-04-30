# 習題 1 -- 請寫一個程式可以做線性回歸
* 參考陳鍾誠老師的[regression.py](https://gitlab.com/ccc110/ai/-/blob/master/_homework/01-regression/regression.py)為基礎，並以[實作：二維爬山演算法](https://kinmen6.com/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-optimize/01-hillclimbing/03-var2/%E5%AF%A6%E4%BD%9C%EF%BC%9A%E4%BA%8C%E7%B6%AD%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95.md)中的隨機調整法進行改寫
* 以下為修改的部分

<pre><code>def optimize():
    fail = 0
    p = [0.0, 0.0]
    h = 0.01
    while fail < 3000:
        fail += 1
        dx = random.uniform(-h, h)
        dy = random.uniform(-h, h)
        pxy = [p[0]+dx, p[1]+dy]
        if loss(pxy) == 0:
            p = pxy
            break
        elif loss(pxy) < loss(p): p = pxy
        else: continue
        
    # 請修改這個函數，自動找出讓 loss 最小的 p
    # p = [2,1] 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    return p

p = optimize()</code></pre>

* 當資料為 x = [0, 1, 2, 3, 4] 且 y = [2, 3, 4, 5, 6] 時，結果如下
![picture](https://github.com/ZKX-0326/ai110b/blob/master/homework1/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-04-30%20192545.png)
![picture](https://github.com/ZKX-0326/ai110b/blob/master/homework1/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-04-30%20192522.png)

* 當資料為 x = [0, 1, 2, 3, 4] 且 y = [1.9, 3.1, 3.9, 5.0, 6.2] 時，結果如下
![picture](https://github.com/ZKX-0326/ai110b/blob/master/homework1/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-04-30%20192445.png)
![picture](https://github.com/ZKX-0326/ai110b/blob/master/homework1/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-04-30%20192418.png)