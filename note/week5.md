# 人工智慧第五週筆記
## 深度優先搜尋法
以先走到終點為主的搜尋法，當走到底且還沒到終點時，會做紀錄，並返回上一個節點，尋找其他路徑。
## 廣度優先搜尋法
將根節點下放入佇列，若沒找到終點，將其子節點放入佇列，並取第一個子節點往下找，繼續往下一輩找，若又失敗就會將其子節點加入佇列，並取下一個子節點重複執行，直到抵達終點。

本週作業:[請寫一個程式可以解以下三題的其中一題--八皇后問題](https://github.com/ZKX-0326/ai110b/tree/master/homework2)