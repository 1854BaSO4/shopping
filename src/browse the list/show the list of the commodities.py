products = [
    {"名称": "冰箱", "价格": 2999, "购买人数": 100},
    {"名称": "洗衣机", "价格": 1999, "购买人数": 50},
    {"名称": "电视机", "价格": 3999, "购买人数": 200},
    {"名称": "空调", "价格": 3499, "购买人数": 75},
    {"名称": "微波炉", "价格": 499, "购买人数": 150},
    {"名称": "电饭煲", "价格": 299, "购买人数": 120},
    {"名称": "电磁炉", "价格": 199, "购买人数": 30},
    {"名称": "吸尘器", "价格": 599, "购买人数": 90},
    {"名称": "烤箱", "价格": 999, "购买人数": 60},
    {"名称": "榨汁机", "价格": 199, "购买人数": 80}
]

for product in products:
    print(f"商品名称: {product['名称']}, 价格: ￥{product['价格']}, 购买人数: {product['购买人数']}人")
