# coding=utf-8


def insert_sort(num_list):
    """
    挿入ソートの関数
    :param num_list: ソートする数列
    :return: ソートされた結果
    """
    for i in range(1, len(num_list)):
        j = i - 1
        # 操作する数字(操作済みの隣)
        ele = num_list[i]
        # 操作済みの数字より、小さければループ(ただし、一番左でないこと)
        # つまり、数字を入れ替える必要があるときは、このループに入る
        while num_list[j] > ele and j >= 0:
            # 入れ替えるので、大きい数字は右にずらす
            num_list[j + 1] = num_list[j]
            # 入れ替えたさらに、左の数字と比較するため、jを1減らす(左にずらす)
            j -= 1

        # 操作し終わった数字を配置
        num_list[j + 1] = ele

    return num_list


if __name__ == "__main__":
    nl = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    sorted_nl = insert_sort(nl)
    print(sorted_nl)
