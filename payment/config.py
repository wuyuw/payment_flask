from alipay import AliPay
from payment.constants import ALIPAY_APPID, BASI_DIR
import os

alipay_client = AliPay(
    appid=ALIPAY_APPID,
    app_notify_url=None,  # 默认回调url
    app_private_key_path=os.path.join(BASI_DIR, 'app_private_key.pem'),
    alipay_public_key_path=os.path.join(BASI_DIR, 'alipay_public_key.pem'),
    sign_type="RSA2",
    debug=True
)

