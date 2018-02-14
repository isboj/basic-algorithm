# coding=utf-8


def merge_sort(num_list):
    """
    マージソートの関数
    :param num_list: ソートする数列(再帰的に利用)
    :return: ソートされた結果
    """
    # 再帰関数の終了条件
    # リストの大きさが1になったらストップ
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    # ここで、分割を行う(右と左に分ける)
    left = num_list[:mid]
    right = num_list[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが帰ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    """
    再帰処理中で呼び出す、分割された配列を結合する関数
    再帰処理中で呼び出すため、渡される配列はソート済み
    :param left: 左側の配列
    :param right: 右側の配列
    :return: 結合された配列
    """
    merged = []
    l_i, r_i = 0, 0

    # ソート済みの配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            # 左側の配列の要素の方が小さいとき
            # つまり、この時点で並べ替えされてない要素では、
            # この要素が最小である
            merged.append(left[l_i])
            l_i += 1
        else:
            # 右側の配列の要素の方が小さいとき
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになったら終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])

    return merged


if __name__ == "__main__":
    nl = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    sorted_nl = merge_sort(nl)
    print(sorted_nl)
