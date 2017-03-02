# encoding: UTF-8

# 默认空值
EMPTY_STRING = ''
EMPTY_UNICODE = u''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0

# 方向常量
DIRECTION_NONE = u'无方向'
DIRECTION_LONG = u'多'
DIRECTION_SHORT = u'空'
DIRECTION_UNKNOWN = u'未知'
DIRECTION_NET = u'净'
DIRECTION_SELL = u'卖出'      # IB接口

# 开平常量
OFFSET_NONE = u'无开平'
OFFSET_OPEN = u'开仓'
OFFSET_CLOSE = u'平仓'
OFFSET_CLOSETODAY = u'平今'
OFFSET_CLOSEYESTERDAY = u'平昨'
OFFSET_UNKNOWN = u'未知'

# 状态常量
STATUS_NOTTRADED = u'未成交'
STATUS_PARTTRADED = u'部分成交'
STATUS_ALLTRADED = u'全部成交'
STATUS_CANCELLED = u'已撤销'
STATUS_UNKNOWN = u'未知'

# 合约类型常量
PRODUCT_EQUITY = u'股票'
PRODUCT_FUTURES = u'期货'
PRODUCT_OPTION = u'期权'
PRODUCT_INDEX = u'指数'
PRODUCT_COMBINATION = u'组合'
PRODUCT_FOREX = u'外汇'
PRODUCT_UNKNOWN = u'未知'
PRODUCT_SPOT = u'现货'
PRODUCT_DEFER = u'延期'
PRODUCT_NONE = ''

# 价格类型常量
PRICETYPE_LIMITPRICE = u'限价'
PRICETYPE_MARKETPRICE = u'市价'
PRICETYPE_FAK = u'FAK'
PRICETYPE_FOK = u'FOK'

# 期权类型
OPTION_CALL = u'看涨期权'
OPTION_PUT = u'看跌期权'

# 交易所类型
EXCHANGE_SSE = 'SSE'       # 上交所
EXCHANGE_SZSE = 'SZSE'     # 深交所
EXCHANGE_CFFEX = 'CFFEX'   # 中金所
EXCHANGE_SHFE = 'SHFE'     # 上期所
EXCHANGE_CZCE = 'CZCE'     # 郑商所
EXCHANGE_DCE = 'DCE'       # 大商所
EXCHANGE_SGE = 'SGE'       # 上金所
EXCHANGE_UNKNOWN = 'UNKNOWN'# 未知交易所
EXCHANGE_NONE = ''          # 空交易所
EXCHANGE_HKEX = 'HKEX'      # 港交所
EXCHANGE_HKFE = 'HKFE'      # 香港期货交易所

EXCHANGE_SMART = 'SMART'       # IB智能路由（股票、期权）
EXCHANGE_NYMEX = 'NYMEX'       # IB 期货
EXCHANGE_GLOBEX = 'GLOBEX'     # CME电子交易平台
EXCHANGE_IDEALPRO = 'IDEALPRO' # IB外汇ECN

EXCHANGE_CME = 'CME'           # CME交易所
EXCHANGE_ICE = 'ICE'           # ICE交易所

EXCHANGE_OANDA = 'OANDA'       # OANDA外汇做市商
EXCHANGE_OKCOIN = 'OKCOIN'     # OKCOIN比特币交易所

# 货币类型
CURRENCY_USD = 'USD'            # 美元
CURRENCY_CNY = 'CNY'            # 人民币
CURRENCY_HKD = 'HKD'            # 港币
CURRENCY_UNKNOWN = 'UNKNOWN'    # 未知货币
CURRENCY_NONE = ''              # 空货币

#合约年份，郑商所不一样
CONTRACT_YEAR_ZS = ("6","7","8","9")
CONTRACT_YEAR = ("16","17","18","19")
# 数据库
#合约月份
#郑商所所有合约、大连所有合约、上海橡胶、螺纹、热卷、镍
CONTRACT_MONTH_159 = ("01","05","09") 
#沪金、沪银、沥青
CONTRACT_MONTH_612 = ("06","12") 
#中金所所有合约、上海金属铜、铝、锌、铅
CONTRACT_MONTH_ALL = ("01","02","03","04","05","06","07",
                      "08","09","10","11","12") 
LOG_DB_NAME = 'VnTrader_Log_Db'
#合约代码
#郑商所所有
CONTRACT_CODE_ZS = ("CF","FG","MA","OI","RM","SR","TA","ZC")

#大商所所有
CONTRACT_CODE_DS = ("p","l","j","v","c","y","a",
                    "m","jm","i","jd","pp","cs")
#上海
CONTRACT_CODE_SHALL = ("cu","al","zn","pb")
CONTRACT_CODE_SH159 = ("ru","rb","hc","ni")
CONTRACT_CODE_SH612 = ("au","ag","bu")

#中金所
CONTRACT_CODE_ZJALL = ("IF","IH","IC","TF")

CURRENT_ACTIVE_YEAR_ZS = "7"
CURRENT_ACTIVE_YEAR_DS = "17"
CURRENT_ACTIVE_YEAR_SHALL = "17"
CURRENT_ACTIVE_YEAR_SH159 = "17"
CURRENT_ACTIVE_YEAR_SH612 = "17"

CURRENT_ACTIVE_MONTH_159 = ("05","09")
CURRENT_ACTIVE_MONTH_612 = ("06","12")
CURRENT_ACTIVE_MONTH_ALL = ("02","03")