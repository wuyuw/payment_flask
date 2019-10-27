from payment.config import alipay_client
from payment.constants import ALIPAY_URL
import time


# 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
def alipay_pay(order_id, total_amount, subject="标题", return_url=None, notify_url=None):
    order_string = alipay_client.api_alipay_trade_page_pay(
        subject=subject,
        out_trade_no=order_id,
        total_amount=str(total_amount),
        return_url=return_url,
        notify_url=notify_url  # 可选，不填则使用默认配置中的notify_url
    )
    alipay_url = ALIPAY_URL + "?" + order_string
    return alipay_url


def alipay_query(order_id):
    for i in range(10):
        pay_result = alipay_client.api_alipay_trade_query(out_trade_no=str(order_id))
        code = pay_result.get("code", "")
        if "10000" == code:
            # 订单生成成功
            trade_status = pay_result.get("trade_status")
            if trade_status is None:
                time.sleep(5)
                continue
            elif "TRADE_SUCCESS" == trade_status:
                return {"result": 1, "message": "支付成功", "status": trade_status}
            elif "WAIT_BUYER_PAY" == trade_status:
                time.sleep(5)
                continue
            else:
                return {"result": 0, "message": "支付失败", "status": trade_status}
        elif "40004" == code:
            time.sleep(10)
            continue
        else:
            return {"result": 0, "message": "支付失败", "code": code}


if __name__ == '__main__':
    order_id = "201711231217515"
    total_amount = "0.01"
    subject = "515测试订单03"
    pay_url = alipay_pay(order_id=order_id, total_amount=total_amount, subject=subject)
    print(pay_url)
    time.sleep(20)
    res = alipay_query(order_id=order_id)
    print(res)

