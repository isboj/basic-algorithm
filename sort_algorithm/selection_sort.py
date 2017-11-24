# coding=utf-8


def selection_sort(num_list):
    """
    選択ソートの関数
    :param num_list: ソートする数列
    :return: ソートされた結果
    """
    # 選択ソートでは、一番左の数値と最小値を交換していく
    for i in range(len(num_list) - 1):
        # リストの最小値のインデックスを求める
        mi = num_list[i:].index(min(num_list[i:]))
        # 一番左の数値と、求めたインデックスを入れ替える
        num_list[i], num_list[i+mi] = num_list[i+mi], num_list[i]

        # デバッグ表示
        print(num_list)
    return num_list


if __name__ == "__main__":
    nl = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    sorted_nl = selection_sort(nl)
    print(sorted_nl)
