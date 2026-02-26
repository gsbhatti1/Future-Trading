> Name

Minimum Trading Volume on OKEx Spot

> Author

leviyuan



> Source (javascript)

```javascript
// Data source: https://github.com/okcoin-okex/API-docs-OKEx.com/blob/master/%E5%B8%81%E5%B8%81%E6%9C%80%E5%B0%8F%E4%BA%A4%E6%98%93%E9%87%8F(min_trade_size%20for%20spot).mda_btc
// Last updated: 2018-4-25 13:37
function main() {
    Log(exchange.GetCurrency(), $.GetMinTradeSize(0))
}

var min_trade_size = {}

min_trade_size.bch_btc = 0.001
min_trade_size.ltc_btc = 0.001
min_trade_size.eth_btc = 0.001
min_trade_size.etc_btc = 0.01
min_trade_size.eth_usdt = 0.001
min_trade_size.btc_usdt = 0.001
min_trade_size.bt2_btc = 0.01
min_trade_size.etc_eth = 0.01
min_trade_size.btg_btc = 0.01
min_trade_size.ltc_usdt = 0.001
min_trade_size.etc_usdt = 0.01
min_trade_size.bch_usdt = 0.001
min_trade_size.qtum_btc = 0.01
min_trade_size.qtum_usdt = 0.01
min_trade_size/qtum_eth = 0.01
min_trade_size.neo_btc = 0.01
min_trade_size.gas_btc = 0.01
min_trade_size.hsr_btc = 0.1
min_trade_size.neo_eth = 0.01
min_trade_size.gas_eth = 0.01
min_trade_size.hsr_eth = 0.1
min_trade_size.neo_usdt = 0.01
min_trade_size.gas_usdt = 0.01
min_trade_size.hsr_usdt = 0.1
min_trade_size.dash_btc = 0.001
min_trade_size.xrp_btc = 1
min_trade_size.zec_btc = 0.001
min_trade_size.dash_eth = 0.001
min_trade_size.xrp_eth = 1
min_trade_size.zec_eth = 0.001
min_trade_size.dash_usdt = 0.001
min_trade_size.xrp_usdt = 1
min_trade_size.zec_usdt = 0.001
min_trade_size.iota_btc = 1
min_trade_size.xuc_btc = 0.1
min_trade_size.iota_eth = 1
min_trade_size.xuc_eth = 0.1
min_trade_size.iota_usdt = 1
min_trade_size.xuc_usdt = 0.1
min_trade_size.eos_btc = 0.1
min_trade_size.omg_btc = 0.1
min_trade_size.eos_eth = 0.1
min_trade_size.omg_eth = 0.1
min_trade_size.eos_usdt = 0.1
min_trade_size.omg_usdt = 0.1
min_trade_size.act_btc = 1
min_trade_size.btm_btc = 1
min_trade_size.act_eth = 1
min_trade_size.btm_eth = 1
min_trade_size.act_usdt = 1
min_trade_size.btm_usdt = 1
min_trade_size.bcd_btc = 0.1
min_trade_size.bcd_usdt = 0.1
min_trade_size.storj_btc = 1
min_trade_size.snt_btc = 10
min_trade_size.storj_eth = 1
min_trade_size.snt_eth = 10
min_trade_size.storj_usdt = 1
min_trade_size.snt_usdt = 10
min_trade_size.pay_btc = 1
min_trade_size.dgd_btc = 0.001
min_trade_size.gnt_btc = 1
min_trade_size.pay_eth = 1
min_trade_size.dgd_eth = 0.001
min_trade_size.gnt_eth = 1
min_trade_size.pay_usdt = 1
min_trade_size.dgd_usdt = 0.001
min_trade_size.gnt_usdt = 1
min_trade_size.lrc_btc = 1
min_trade_size.nuls_btc = 0.1
min_trade_size.mco_btc = 0.1
min_trade_size.lrc_eth = 1
min_trade_size.nuls_eth = 0.1
min_trade_size.mco_eth = 0.1
min_trade_size.lrc_usdt = 1
min_trade_size.nuls_usdt = 0.1
min_trade_size.mco_usdt = 0.1
min_trade_size.btg_usdt = 0.01
min_trade_size.cmt_btc = 10
min_trade_size.itc_btc = 1
min_trade_size.cmt_eth = 10
min_trade_size.itc_eth = 1
min_trade_size.cmt_usdt = 10
min_trade_size.itc_usdt = 1
min_trade_size.sbtc_btc = 0.1
min_trade_size.pra_btc = 1
min_trade_size.san_btc = 1
min_trade_size.edo_btc = 0.1
min_trade_size.avt_btc = 1
min_trade_size.pra_eth = 1
min_trade_size.san_eth = 1
min_trade_size.edo_eth = 0.1
min_trade_size.avt_eth = 1
min_trade_size.pra_usdt = 1
min_trade_size.san_usdt = 1
min_trade_size.edo_usdt = 1
min_trade_size.avt_usdt = 1
min_trade_size.ltc_bch = 0.001
min_trade_size.ltc_eth = 0.001
min_trade_size.etc_bch = 0.01
min_trade_size.btg_bch = 0.01
min_trade_size.avt_bch = 1
min_trade_size.act_bch = 1
min_trade_size.cmt_bch = 10
min_trade_size.dgd_bch = 0.001
min_trade_size.dash_bch = 0.001
min_trade_size.eos_bch = 0.1
min_trade_size.edo_bch = 0.1
min_trade_size.ctr_btc = 1
min_trade_size.link_btc = 1
min_trade_size.salt_btc = 0.1
min_trade_size['1st_btc'] = 1
min_trade_size.wtc_btc = 0.1
min_trade_size.sngls_btc = 10
min_trade_size.sngls_eth = 10
min_trade_size.sngls_usdt = 10
min_trade_size.dat_btc = 10
min_trade_size.dat_eth = 10
min_trade_size.dat_usdt = 10
min_trade_size.gnx_btc = 1
min_trade_size.gnx_eth = 1
min_trade_size.gnx_usdt = 1
min_trade_size.icx_btc = 0.1
min_trade_size.icx_eth = 0.1
min_trade_size.icx_usdt = 0.1
min_trade_size.ark_btc = 0.1
min_trade_size.ark_eth = 0.1
min_trade_size.ark_usdt = 0.1
min_trade_size.yoyo_btc = 10
min_trade_size.yoyo_eth = 10
min_trade_size.yoyo_usdt = 10
min_trade_size.qvt_btc = 1
min_trade_size.qvt_eth = 1
min_trade_size.qvt_usdt = 1
min_trade_size.elf_eth = 1
min_trade_size.elf_btc = 1
min_trade_size.elf_usdt = 1
min_trade_size.ast_btc = 1
min_trade_size.ast_eth = 1
min_trade_size.ast_usdt = 1
min_trade_size.sub_btc = 1
min_trade_size.sub_eth = 1
min_trade_size.sub_usdt = 1
min_trade_size.dnt_btc = 10
min_trade_size.dnt_eth = 10
min_trade_size.dnt_usdt = 10
min_trade_size.fun_btc = 10
min_trade_size.fun_eth = 10
min_trade_size.fun_usdt = 10
```

Note: The last line `min_trade_` seems to be incomplete, so it has been terminated appropriately. If there are further details or corrections needed for this script, please let me know!