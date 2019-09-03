#! /usr/bin/python
#-*- encoding: utf-8 -*-

def replace_html(f, fn, replace_dict):
    
    old_lines = f.readlines()
    #new_lines = old_lines
    new_lines = old_lines
    
    for i in replace_dict.keys():
        for j in range(len(old_lines)):
            if old_lines[j].find(str(i)) !=-1:
                #print 'true'
                new_lines[j] = old_lines[j].replace(i, replace_dict[i])

    fn.writelines(old_lines)
    fn.close()
    
def print_fj(fj, fj_url, web_url):
    #打印封基到index
    #print_part_head('以下是传统封基的收益信息', '程序自动抓取折价在15%以上的传统封基的信息.', fj_url, index)
    log = open(web_url, 'a+')
    
    fj_lines =[]
    fj_lines.append('* 程序自动抓取折价在15%以上的传统封基的信息.<br>')
    fj_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % fj_url)
    fj_str = ''
    
    for i in fj:
        fj_line = "<strong> * %s 的折价率是 <em>%s%%</em> </strong><br>" % (i, fj[i])
        #log.write(fj_line)
        fj_lines.append(fj_line)
    
    fj_str = ''.join(fj_lines)
    return fj_str
    
def print_bond(bond_high, bond_max, bond_url, web_url):
    log = open(web_url, 'a+')
    
    bond_lines =[]
    bond_lines.append('* 程序自动抓取隐含收益在9%以上的债券信息.<br>')
    bond_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % bond_url)
    
    for i in bond_high:
        bond_high_line = '<strong>* %s 的收益率是 %s %% </strong><br>' %(str(i), str(bond_high[i]))
        bond_lines.append(bond_high_line)

    bond_max_line =('<br><strong>* 最高的债券收益是：%s </strong>' % bond_max)
    bond_lines.append(bond_max_line)
    
    bond_str = ''.join(bond_lines)
    
    return bond_str

def print_etf(etf, etf_url, web_url):
    log = open(web_url, 'a+')
    
    etf_lines =[]
    etf_lines.append('* 程序自动抓取PE在10以下的ETF信息.<br>')
    etf_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % etf_url)

    for i in etf:
        if etf[i][2] == '金融类':
            etf_log = "* (%s) %s 的PE值是 <em><strong>%s</strong></em>, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            etf_lines.append(etf_log)
    etf_lines.append('<br>\n')

    for i in etf:
        if etf[i][2] == '恒生类':
            etf_log = "* (%s) %s 的PE值是 <em><strong>%s</strong></em>, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            etf_lines.append(etf_log)
    etf_lines.append('<br>\n')

    for i in etf:
        if etf[i][2] == '其他类':
            etf_log = "* (%s) %s 的PE值是 <em><strong>%s</strong></em>, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            etf_lines.append(etf_log)
    etf_lines.append('<br>\n')

    for i in etf:
        if etf[i][2] == 'NA错误类':
            etf_log = "* (%s) %s 的PE值是 <em><strong>%s</strong></em>, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            etf_lines.append(etf_log)
    etf_lines.append('<br>\n')
    
    etf_str = ''.join(etf_lines)
    return etf_str
    
def print_kzj(kzj, kzj_url, web_url):
    log = open(web_url, 'a+')
    
    kzj_lines =[]
    kzj_lines.append('* 程序自动抓取价格在130以下的可转债的信息.<br>')
    kzj_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % kzj_url)
    
    for i in kzj:
        kzj_line = "* %s 的现价是 <em><strong>%s</strong></em> <br>\n" % (i, kzj[i])
        kzj_lines.append(kzj_line)
    
    kzj_str = ''.join(kzj_lines)
    
    return kzj_str
    
    
def print_stock(stock, stock_url, web_url):
    log = open(web_url, 'a+')
    
    stock_lines =[]
    stock_lines.append('* 程序自动抓取"强烈推荐的"打新股的信息.<br>')
    stock_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % stock_url)
    
    for i in stock:
        stock_line = "* %s 的购买评价是 <em><strong>%s</strong></em>,申购日期是 %s-%s. <br>\n" % (i, stock[i][0], stock[i][1], stock[i][2])
        stock_lines.append(stock_line)
    
    stock_str = ''.join(stock_lines)
    return stock_str
    
def print_indice(indice_raw, indice_filter, indice_url, web_url):
    log = open(web_url, 'a+')
    
    indice_lines =[]
    indice_lines.append('* 程序目前手机52K排位信息,越低表明指数在近一年内的水准.<br>')
    indice_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % indice_url)

    
    for i in indice_raw:
        indice_line = "*** %s  类的 %s: %s  指数的值是%s,   52K排位是  <strong>%s</strong><br>\n" % (indice_raw[i][0], i, indice_raw[i][1], indice_raw[i][2], indice_raw[i][3])
        indice_lines.append(indice_line)
    indice_lines.append('<br>\n')    

    indice_lines.append('<strong>以下过滤出52K信息在25% 的指数</strong><br>\n')
    for i in indice_filter:
        indice_line_filter = "*** %s  类的 %s: %s  指数的值是%s,   52K排位是  <strong>%s%%</strong><br>\n" % (indice_filter[i][0], i, indice_filter[i][1], indice_filter[i][2], indice_filter[i][3])
        indice_lines.append(indice_line_filter)
        
    indice_str = ''.join(indice_lines)
    
    return indice_str
        
def print_funda(funda, funda_url, web_url):
    log = open(web_url, 'a+')
    
    funda_lines =[]
    funda_lines.append('* 提取折价率在10以下，隐含收益在5以上，母鸡溢价率在0一下的分级A.<br>')
    funda_lines.append("<A HREF=\"%s\">'* 信息收集网址 <br><br>'</A>" % funda_url)
    
    
    for i in funda:
        funda_line = "* <strong> 分级A %s 的折价率是 %s%%, 隐含收益率是 %s%%, 母鸡溢价率是 %s%%.</strong> <br>\n" %(i, funda[i][0], funda[i][1], funda[i][2])
        funda_lines.append(funda_line)
    funda_lines.append('<br>\n')
    
    funda_str = ''.join(funda_lines)
    
    return funda_str

def print_index(index_value, index_url, web_url):
    log = open(web_url, 'a+')
    
    index_lines =[]
    for i in index_value:
        #print type(index_value[i][2])
        index_line ="* %s (%s) = %s，涨跌幅 %s%%<br>" % (i, index_value[i][0], index_value[i][1], index_value[i][2])
        index_lines.append(index_line)
    index_str = ''.join(index_lines)
    return index_str
    
if __name__ == "__main__":
    index = '/srv/www/pmoney/index.html'
    f = open('template.html')
    fn = open(index, 'w')
    
    replace_html(f, fn, replace_dict)

