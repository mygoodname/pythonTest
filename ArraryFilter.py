import numpy as np


class ArrayFilter:

    def filterThreeArray(self, arr):
        for i in arr:
            i = self.__filterTwoArray(i)
        return arr

    def __filterTwoArray(self, arr):
        target_arr = []
        useless_arr = []
        if len(arr) > 1:
            for h in arr[len(arr) - 1]:
                if h != 'PER' and h != 'LOC' and h != 'ORG' and h != 'TIME' and h != 'n' and h != 'nz' and h != 's' and h != 'nw':  # 保留 人名、地名、机构名称、时间、普通名称、处所名词、作品名称
                    target_arr.append(False)
                    useless_arr.append(True)
                else:
                    target_arr.append(True)
                    useless_arr.append(False)
            np_arr = np.array(arr[0])
            target_np_arr = np_arr[target_arr]
            useless_np_arr = np_arr[useless_arr]
            arr[0] = target_np_arr.tolist()
            arr[len(arr) - 1] = useless_np_arr.tolist()
        return arr
