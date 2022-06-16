# 人工智慧第七週筆記
## 電腦下棋
以五子棋為例，電腦下棋是以加權分數判斷要下哪裡，因此每當電腦要下下一顆棋時，會將所有沒被下過的位置進行計算，並下在分數最高的位置，此即為最簡單的下棋程式。

## MinMax演算法
以自己為正對方為負，將兩邊分數加總，並計算所有可能性，最後尋找最糟情況下失分最少的路，但由於計算量過大因此沒辦法計算太多層。

## Alpha-Beta修剪法
將已確定不可能的選項剪掉，以減少分支數量，增加搜尋空間。