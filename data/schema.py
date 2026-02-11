User = {
    "user_id": int,
    "x": float,
    "y": float,
    "price_sensitivity": float,  # 对价格变化的敏感度
    "patience_time": float       # 最大可等待时间
}
Driver = {
    "driver_id": int,
    "x": float,
    "y": float,
    "vehicle_type": str,
    "available": bool
}
Order = {
    "order_id": int,
    "user_id": int,
    "request_time": int,
    "trip_distance": float,
    "base_price": float,
    "subsidy": float,
    "assigned_driver_id": int | None,
    "accepted": int
}
