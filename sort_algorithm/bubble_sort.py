# coding=utf-8


def bubble_sort(num_list):
    """
    バブルソートの関数
    :param num_list: ソートする数列
    :return: ソートされた結果
    """
    # 数列の個数分ループ
    # バブルソートでは、左の数値(ここではi)から順番に並べ替えが完了する
    for i in range(len(num_list)):
        # range(始まりの数値, 終わりの数値, 増加する量)
        for j in range(len(num_list) - 1, i, -1):
            if num_list[j-1] > num_list[j]:
                # 左の数値の方が大きかったら、入れ替える
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

                # デバッグ表示
                print(num_list)
    return num_list


if __name__ == "__main__":
    nl = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    sorted_nl = bubble_sort(nl)
    print(sorted_nl)
