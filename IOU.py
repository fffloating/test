def iou(box1, box2):
    """
    计算两个矩形框的 IOU
    :param box1: 矩形框1，格式为 [xmin, ymin, xmax, ymax]
    :param box2: 矩形框2，格式为 [xmin, ymin, xmax, ymax]
    :return: IOU 值
    """
    # 计算交集面积
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    if x1 >= x2 or y1 >= y2:
        overlap_area = 0
    else:
        overlap_area = (x2 - x1) * (y2 - y1)
    # 计算并集面积
    union_area = (box1[2] - box1[0]) * (box1[3] - box1[1]) + (box2[2] - box2[0]) * (box2[3] - box2[1]) - overlap_area
    # 计算 IOU
    iou = overlap_area / union_area
    return iou
# OKKK 这个比代码随想录简单多了  哈哈哈
# test