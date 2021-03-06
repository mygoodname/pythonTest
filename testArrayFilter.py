import ArraryFilter
import numpy as np
yaya = [[['\n\n\n\n\n\n\n\n\n'], ['PER']], [['\n\n\n\n\n', '内容', '简介', '\n\n', '当前', '中国', '超过', '80%', '的', '网络', '购买', '行为', '发生', '在', '手机端', '，', '但',
          '电子商务', '行业', '的', '视觉', '设计',
          '整体', '上', '还', '基于', '传统', 'PC端', '的', '审美', '准则', '，', '对于', '手机', '用户', '来说', '存在', '着', '阅读', '不便', '的',
          '问题', '，', '使得', '手机端', '内容',
          '传达', '效率低', '下', '，', '白白', '浪费', '了', '宝贵', '的', '用户', '流量', '。', '竖', '屏', '思维', '是', '陈柱子', '专门', '针对',
          '手机', '屏幕', '特点', '和', '手机',
          '用户', '习惯', '总结', '提炼', '的', '知识', '成果', '，', '可以', '帮助', '商家', '大幅度', '提升', '手机端', '转化率', '。', '\n', '本书',
          '首先', '引领', '读者', '突破', '“',
          '沿用', 'PC', '设计', '思维', '也', '能', '做好', '手机端', '图片', '”', '的', '思维', '惯性', '，', '树立', '必须', '专门', '针对', '手机屏',
          '、', '手机', '用户', '制作', '独立',
          '的', '“', '手机端', '原生', '内容', '”', '的', '正确', '理念', '；', '然后', '用', '大量', '案例', '阐述', '“', '如何', '做到', '”',
          '的', '具体', '方法', '；', '最后', '点',
          '破', '竖屏', '思维', '能', '大幅度', '提升', '手机端', '转化率', '的', '内在', '逻辑', '。', '本书', '所', '讲', '的', '方法', '经过', '实际',
          '验证', '，', '已经', '帮助', '许多', '不同',
          '类目', '的', '商家', '实现', '手机端', '转化率', '提升', '20%', '、', '50%', '，', '甚至', '一倍', '以上', '。', '\n', '本书', '适合',
          '所有', '希望', '通过', '图片', '在', '手机', '上',
          '卖货', '、', '传递', '商业', '信息', '的', '电商', '、', '微商', '、', '新媒体', '人', '阅读', '。', '\n', '未经许可', '，', '不得以', '任何',
          '方式', '复制', '或', '抄袭', '本书', '之',
          '部分', '或', '全部', '内容', '。', '\n版权所有', '，', '侵权', '必究', '。', '\n\n', '图书', '在', '版', '编目', '（', 'CIP', '）',
          '数据', '\n\n', '竖屏', '思维', '：', '大幅度', '提升',
          '手机端', '转化率', '的', '逻辑', '和', '方法', '/', '陈柱子', '著', '.', '—', '北京', '：', '电子工业出版社', '，', ' ', '2018',
          '.1\nISBN 978-7-121-32805-3\n', 'Ⅰ', '.', '①', '竖',
          '…', 'Ⅱ', '.', '①陈', '…', 'Ⅲ', '.', '①', '电子商务', 'Ⅳ', '.①F713.36\n中国版本图书馆', 'CIP', '数据', '核', '字', '(',
          '2017', ')', '第242591号', '\n', '责任编辑', '：', '林瑞',
          '和', '\n印刷', '：', '北京画中画印刷有限公司\n', '装订', '：', '北京画中画印刷有限公司\n出版发行：电子工业出版社', '\n', '北京市', '海淀区', '万寿路', '173',
          '信箱', ' ', '邮编', '：',
          '100036\n', '开本', '：', '720', '×', '1000', ' ', '1', '/', '16', ' ', '印张', '：', '14.5', ' ', '字数', '：',
          '213千', '字', '\n', '版次', '：', '2018年', '1月', '第1', '版\n',
          '印次', '：', '2018年', '1月', '第1次', '印刷', '\n', '定价', '：', '69.00元', '\n凡', '所', '购买', '电子工业', '出版社', '图书', '有',
          '缺损', '问题', '，', '请', '向', '购买', '书店',
          '调换', '。', '若', '书店', '售缺', '，', '请', '与', '本社', '发行部', '联系', '，', '联系', '及', '邮购', '电话', '：', '（', '010',
          '）', '88254888', '，', '88258888', '。', '\n',
          '质量', '投诉', '请', '发邮件', '至', 'zlts@phei.com.cn', '，', '盗版', '侵权', '举报', '请', '发邮件', '至',
          'dbqq@phei.com.cn。\n本书咨询', '联系', '方式', '：', '010', '-',
          '51260888', '-', '819', '，', 'faq@phei.com.cn。\n\n\n'],
         ['PER', 'n', 'n', 'PER', 'TIME', 'LOC', 'v', 'm', 'u', 'n', 'vn', 'n', 'v', 'p', 'n', 'w', 'c', 'n', 'n', 'u',
          'n', 'vn', 'n', 'f', 'd', 'p', 'n', 'n', 'u', 'vn', 'n', 'w',
          'p', 'n', 'n', 'v', 'v', 'u', 'vn', 'a', 'u', 'n', 'w', 'v', 'n', 'n', 'v', 'n', 'f', 'w', 'd', 'v', 'u', 'a',
          'u', 'n', 'n', 'w', 'a', 'n', 'n', 'v', 'PER', 'd', 'p', 'n',
          'n', 'n', 'c', 'n', 'n', 'n', 'v', 'v', 'u', 'n', 'n', 'w', 'v', 'v', 'n', 'd', 'v', 'n', 'n', 'w', 'v', 'r',
          'd', 'v', 'n', 'v', 'w', 'v', 'n', 'vn', 'n', 'd', 'v', 'v',
          'n', 'n', 'w', 'u', 'n', 'n', 'w', 'v', 'd', 'd', 'v', 'nz', 'w', 'n', 'n', 'v', 'a', 'u', 'w', 'n', 'a', 'n',
          'w', 'u', 'a', 'n', 'w', 'c', 'p', 'a', 'n', 'v', 'w', 'r',
          'v', 'w', 'u', 'a', 'n', 'w', 'a', 'q', 'a', 'n', 'n', 'v', 'd', 'v', 'n', 'n', 'u', 'a', 'n', 'w', 'r', 'u',
          'v', 'u', 'n', 'p', 'a', 'vn', 'w', 'd', 'v', 'm', 'a', 'n',
          'u', 'n', 'v', 'n', 'n', 'v', 'm', 'w', 'm', 'w', 'd', 'm', 'f', 'w', 'v', 'r', 'v', 'r', 'v', 'p', 'n', 'p',
          'n', 'f', 'v', 'w', 'v', 'n', 'n', 'u', 'n', 'w', 'n', 'w',
          'n', 'n', 'v', 'w', 'n', 'v', 'w', 'd', 'r', 'n', 'v', 'c', 'v', 'r', 'u', 'n', 'c', 'n', 'n', 'w', 'v', 'w',
          'vn', 'v', 'w', 'nz', 'n', 'p', 'n', 'vn', 'w', 'nz', 'w',
          'n', 'v', 'n', 'n', 'w', 'd', 'v', 'n', 'n', 'u', 'n', 'c', 'n', 'w', 'PER', 'u', 'w', 'w', 'LOC', 'w', 'ORG',
          'w', 'w', 'm', 'w', 'w', 'w', 'm', 'n', 'w', 'w', 'w', 'm',
          'w', 'w', 'w', 'm', 'n', 'w', 'ORG', 'nz', 'n', 'n', 'n', 'w', 'm', 'w', 'm', 'n', 'n', 'w', 'PER', 'c', 'vn',
          'w', 'ORG', 'v', 'w', 'ORG', 'v', 'LOC', 'LOC', 'LOC', 'm',
          'n', 'w', 'n', 'w', 'm', 'vn', 'w', 'm', 'w', 'm', 'w', 'm', 'w', 'q', 'w', 'LOC', 'w', 'm', 'w', 'n', 'w',
          'm', 'n', 'v', 'n', 'w', 'TIME', 'TIME', 'm', 'n', 'n', 'w',
          'TIME', 'TIME', 'm', 'vn', 'n', 'n', 'w', 'm', 'PER', 'u', 'v', 'n', 'n', 'n', 'v', 'vn', 'n', 'w', 'v', 'p',
          'v', 'n', 'vn', 'w', 'c', 'n', 'v', 'w', 'v', 'p', 'n', 'n',
          'v', 'w', 'vn', 'c', 'vn', 'n', 'w', 'w', 'm', 'w', 'm', 'w', 'm', 'w', 'n', 'n', 'v', 'v', 'v', 'v', 'nz',
          'w', 'n', 'vn', 'vn', 'v', 'v', 'v', 'nw', 'vn', 'n', 'w', 'm',
          'w', 'm', 'w', 'm', 'w', 'ORG']],[['\n\n\n\n', '开卷', '之', '前', '\n↘', ' ', '本书', '目标', '：', '帮', '你', '把', '现有', '手机端', '转化率', '提升',
          '50%\n第一次', '看到', '这个', '目标', '，', '也许', '你', '内心', '充满', '怀疑', '，', '觉得', '不可思议', '。', '希望', '读完', '本书', '之后', '，', '你',
         '觉得', '这个', '目标', '完全', '可以', '实现', '，', '并没有', '什么', '了不起', '。', '\n↘', ' ', '本书', '特点', '：', '不', '讲', '平台', '运营', '、',
         '不', '讲', '内容', '构成', '、', '不', '讲', '设计', '美学', '\n', '竖', '屏', '思维', '从', '信息', '传播', '的', '角度', '探讨', '电商', '手机端', '转化率',
        '，', '关注', '点', '不是', '设计', '美学', '、', '营销心理学', '、', '平台', '运营', '技巧', '等', '。', '书', '中', '案例', '的', '目的', '，', '是', '为了',
        '帮助', '读者', '理解', '信息', '沟通', '难易度', '和', '信息', '传播', '效果', '，', '这些', '案例', '不是', '内容', '范例', '，', '也', '不是', '设计', '范例',
        '。', '阅读', '时', '请', '留心', '体会', '此', '点', '。', '\n↘ ', '本书', '适合', '对象', '：', '通过', '图片', '在', '手机', '上', '卖货', '、', '传递',
        '商业', '信息', '的', '电商', '、', '微商', '、', '新媒体', '人', '\n', '不限', '平台', '：', '适合', '淘宝', '、', '天猫', '、', '京东', '、', '唯品会', '、',
        '跨境电商', '、', '海淘', '、', '自营', 'B2C', '、', 'APP', '商城', '、', '微博', '、', '微信朋友圈', '、', '公众', '号', '、', '头条号', '、', 'QQ空间', '等',
       '平台', '。', '\n', '不限', '类目', '：', '适合', '化妆品', '、', '食品', '、', '家电', '、', '数码', '、', '男女装', '、', '鞋', '靴', '、', '童装', '、',
        '箱包', '、', '家具', '、', '日用品', '、', '灯饰', '、', '厨具', '、', '玩具', '、', '卫浴', '、', '情趣', '用品', '、', '运动户', '外', '、', '宠物', '用品',
        '、', '车载', '、', '工业品', '等', '各类', '商品', '。', '\n不限职位', '：', '适合', '老板', '、', '运营', '经理', '、', '设计师', '、', '文案师', '、', '摄影师',
        '、', '产品', '经理', '等', '人群', '阅读', '。', '\n↘', ' ', '温馨', '提示', '\n', '竖', '屏', '思维', '因', '电商', '而', '起', '，', '因此', '本书', '主要',
        '围绕', '电商', '来', '组织', '语言', '。', '书', '中', '探讨', '的', '手机端', '内容', '，', '多', '指', '电商', '行业', '里', '的', '“', '手机端', '详情',
        '图', '”', '。', '如果', '你', '从事', '的', '是', '微商', '、', '新媒体', '、', '短', '视频', '、', '营销', '策划', '等', '行业', '，', '请', '用', '你们',
        '行业', '具体', '的', '手机端', '名称', '（', '比如', '微博', '配图', '、', '朋友圈', '配图', '、', '活动', '海报', '等', '）', '替换', '文中', '“', '手机端',
        '详情', '图', '”', '，', '然后', '阅读', '和', '思考', '。', '\nTa', '（', 'target', ' ', 'audiences', '，', '目标受众', '）', '同时', '也是', '汉语',
        '“', '他', '/', '她', '”', '的', '拼音', '，', '在', '本文', '中', '使用', '“', 'Ta', '”', '是', '一语', '双关', '。', '\n', '截至', '本书', '完成',
        '的', '2017年', '11月', '，', '绝大多数', '智能', '手机', '配置', '的', '仍是', '9', '∶', '16', '竖', '屏', '。', '因为', 'iPhone', ' ', 'X', '刚刚',
        '上市', '，', '9∶18', '竖', '屏', '尚', '处于', '推广', '初期', '，', '市场', '份额', '还', '可以', '忽略', '不计', '。', '至于', '9', '∶', '18', '竖屏', '将来',
        '能否', '取代', '9', '∶', '16', '竖屏', '成为', '市场', '主流', '，', '还', '有待', '时间', '的', '考验', '。', '本书', '从', '满足', '主流', '用户', '使用', '体验', '的',
        '角度', '出发', '，', '暂', '以', '9', '∶', '16', '竖屏', '作为', '智能', '手机', '的', '典型', '屏幕', '进行', '阐述', '。', '注意', '，', '无论', '屏幕', '比例', '是', '9', '∶',
        '16', '还是', '9', '∶', '18', '，', '竖', '屏', '思维', '的', '基本', '逻辑', '和', '改善', '方法', '是', '一样', '的', '。', '\n\n\n'],
        ['PER', 'v', 'u', 'f', 'nz', 'w', 'r', 'n', 'w', 'v', 'r', 'p', 'v', 'n', 'n', 'v', 'm', 'v', 'r', 'n', 'w', 'd', 'r', 'n', 'v', 'vn', 'w', 'v', 'an', 'w', 'v', 'v',
         'r', 'f', 'w', 'r', 'v', 'r', 'n', 'd', 'v', 'v', 'w', 'v', 'r', 'an', 'w', 'nz', 'w', 'r', 'n', 'w', 'd', 'v', 'n', 'v', 'w', 'd', 'v', 'n', 'v', 'w', 'd', 'v', 'v',
         'n', 'n', 'a', 'n', 'n', 'p', 'n', 'vn', 'u', 'n', 'v', 'n', 'n', 'n', 'w', 'vn', 'n', 'v', 'v', 'n', 'w', 'nz', 'w', 'n', 'vn', 'n', 'u', 'w', 'n', 'f', 'n', 'u', 'n',
         'w', 'v', 'p', 'v', 'n', 'v', 'n', 'vn', 'n', 'c', 'n', 'vn', 'n', 'w', 'r', 'n', 'v', 'n', 'n', 'w', 'd', 'v', 'vn', 'n', 'w', 'v', 'n', 'v', 'v', 'v', 'r', 'q', 'w',
         'PER', 'r', 'v', 'n', 'w', 'p', 'n', 'p', 'n', 'f', 'v', 'w', 'v', 'n', 'n', 'u', 'n', 'w', 'n', 'w', 'n', 'n', 'v', 'a', 'n', 'w', 'v', 'nz', 'w', 'nz', 'w', 'ORG',
         'w', 'nz', 'w', 'nz', 'w', 'nz', 'w', 'v', 'nz', 'w', 'nz', 'n', 'w', 'nz', 'w', 'nz', 'w', 'n', 'n', 'w', 'nz', 'w', 'nz', 'u', 'n', 'w', 'n', 'v', 'n', 'w', 'v', 'n',
         'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'n', 'w', 'n', 'f',
         'w', 'n', 'n', 'w', 'vn', 'w', 'n', 'u', 'r', 'n', 'w', 'nz', 'w', 'v', 'n', 'w', 'vn', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'w', 'n', 'n', 'u', 'n', 'v', 'w', 'nz', 'w',
         'a', 'vn', 'n', 'a', 'n', 'n', 'p', 'n', 'c', 'v', 'w', 'c', 'r', 'ad', 'v', 'n', 'v', 'v', 'n', 'w', 'n', 'f', 'v', 'u', 'n', 'n', 'w', 'ad', 'v', 'n', 'n', 'f', 'u',
         'w', 'n', 'n', 'n', 'w', 'w', 'c', 'r', 'v', 'u', 'v', 'n', 'w', 'n', 'w', 'a', 'n', 'w', 'vn', 'vn', 'u', 'n', 'w', 'v', 'p', 'r', 'n', 'a', 'u', 'n', 'n', 'w', 'v',
         'n', 'vn', 'w', 'n', 'vn', 'w', 'n', 'n', 'u', 'w', 'v', 's', 'w', 'n', 'n', 'n', 'w', 'w', 'c', 'v', 'c', 'v', 'w', 'nz', 'w', 'nz', 'w', 'nz', 'w', 'n', 'w', 'c',
         'v', 'nz', 'w', 'r', 'w', 'r', 'w', 'u', 'n', 'w', 'p', 'n', 'f', 'v', 'w', 'xc', 'w', 'v', 'n', 'n', 'w', 'v', 'p', 'r', 'v', 'u', 'TIME', 'TIME', 'w', 'm', 'n', 'n',
         'vn', 'u', 'v', 'm', 'w', 'm', 'a', 'n', 'w', 'p', 'nz', 'w', 'xc', 'd', 'v', 'w', 'TIME', 'a', 'n', 'd', 'v', 'vn', 'TIME', 'w', 'n', 'n', 'd', 'v', 'v', 'v', 'w',
         'p', 'm', 'w', 'm', 'n', 'TIME', 'v', 'v', 'm', 'w', 'm', 'n', 'v', 'n', 'n', 'w', 'd', 'v', 'n', 'u', 'vn', 'w', 'r', 'p', 'v', 'n', 'n', 'vn', 'vn', 'u', 'n', 'v',
         'w', 'd', 'p', 'm', 'w', 'm', 'n', 'v', 'n', 'n', 'u', 'a', 'n', 'v', 'vn', 'w', 'v', 'w', 'c', 'n', 'n', 'v', 'm', 'w', 'm', 'v', 'm', 'w', 'm', 'w', 'a', 'n', 'n',
         'u', 'a', 'n', 'c', 'vn', 'n', 'v', 'a', 'u', 'w', 'PER']]]


def __filterTwoArray(self, arr):
    # 创建一个空列表
    filter_arr = []
    afterFilter = []
    for h in arr[len(arr) - 1]:
        if h != 'PER' and h != 'LOC' and h != 'ORG' and h != 'TIME' and h != 'n' and h != 'nz' and h != 's' and h != 'nw':  # 人名、地名、机构名称、时间、普通
            filter_arr.append(False)
        else:
            filter_arr.append(True)
            afterFilter.append(h)
    # np_arr=np.array(arr[0])
    np_arr = np.asarray(arr[0])
    new_np_arr = np_arr[filter_arr]
    arr[0] = new_np_arr.tolist()
    arr[len(arr) - 1] = afterFilter
    return arr


arraryF=ArraryFilter.ArrayFilter()
print(arraryF.filterThreeArray(yaya))

[[['\n\n\n\n\n\n\n\n\n'], []],
 [['\n\n\n\n\n', '内容', '简介', '\n\n', '当前', '中国', '网络', '行为', '手机端', '电子商务', '行业', '视觉', '整体', '传统', 'PC端', '准则', '手机', '用户', '问题', '手机端', '内容', '效率低', '用户', '流量', '屏', '思维', '陈柱子', '手机', '屏幕', '特点', '手机', '用户', '习惯', '知识', '成果', '商家', '手机端', '转化率', '读者', 'PC', '思维', '手机端', '图片', '思维', '惯性', '手机屏', '手机', '用户', '手机端', '内容', '理念', '案例', '方法', '竖屏', '思维', '手机端', '转化率', '逻辑', '方法', '类目', '商家', '手机端', '转化率', '图片', '手机', '商业', '信息', '电商', '微商', '新媒体', '人', '\n', '方式', '部分', '全部', '内容', '\n\n', '图书', '版', 'CIP', '数据', '竖屏', '思维', '手机端', '转化率', '逻辑', '方法', '陈柱子', '北京', '电子工业出版社', '竖', '电子商务', '.①F713.36\n中国版本图书馆', 'CIP', '数据', '核', '字', '\n', '责任编辑', '林瑞', '北京画中画印刷有限公司\n', '北京画中画印刷有限公司\n出版发行：电子工业出版社', '北京市', '海淀区', '万寿路', '信箱', '邮编', '印张', '字数', '字', '版次', '2018年', '1月', '版\n', '印次', '2018年', '1月', '\n', '定价', '\n凡', '电子工业', '出版社', '图书', '问题', '书店', '书店', '本社', '发行部', '电话', '\n', '质量', 'zlts@phei.com.cn', '盗版', 'dbqq@phei.com.cn。\n本书咨询', '方式', 'faq@phei.com.cn。\n\n\n'],
  ['超过', '80%', '的', '购买', '发生', '在', '，', '但', '的', '设计', '上', '还', '基于', '的', '审美', '，', '对于', '来说', '存在', '着', '阅读', '不便', '的', '，', '使得', '传达', '下', '，', '白白', '浪费', '了', '宝贵', '的', '。', '竖', '是', '专门', '针对', '和', '总结', '提炼', '的', '，', '可以', '帮助', '大幅度', '提升', '。', '\n', '本书', '首先', '引领', '突破', '“', '沿用', '设计', '也', '能', '做好', '”', '的', '，', '树立', '必须', '专门', '针对', '、', '制作', '独立', '的', '“', '原生', '”', '的', '正确', '；', '然后', '用', '大量', '阐述', '“', '如何', '做到', '”', '的', '具体', '；', '最后', '点', '破', '能', '大幅度', '提升', '的', '内在', '。', '本书', '所', '讲', '的', '经过', '实际', '验证', '，', '已经', '帮助', '许多', '不同', '的', '实现', '提升', '20%', '、', '50%', '，', '甚至', '一倍', '以上', '。', '\n', '本书', '适合', '所有', '希望', '通过', '在', '上', '卖货', '、', '传递', '的', '、', '、', '阅读', '。', '未经许可', '，', '不得以', '任何', '复制', '或', '抄袭', '本书', '之', '或', '。', '\n版权所有', '，', '侵权', '必究', '。', '在', '编目', '（', '）', '\n\n', '：', '大幅度', '提升', '的', '和', '/', '著', '.', '—', '：', '，', ' ', '2018', '.1\nISBN 978-7-121-32805-3\n', 'Ⅰ', '.', '①', '…', 'Ⅱ', '.', '①陈', '…', 'Ⅲ', '.', '①', 'Ⅳ', '(', '2017', ')', '第242591号', '：', '和', '\n印刷', '：', '装订', '：', '\n', '173', ' ', '：', '100036\n', '开本', '：', '720', '×', '1000', ' ', '1', '/', '16', ' ', '：', '14.5', ' ', '：', '213千', '\n', '：', '第1', '：', '第1次', '印刷', '：', '69.00元', '所', '购买', '有', '缺损', '，', '请', '向', '购买', '调换', '。', '若', '售缺', '，', '请', '与', '联系', '，', '联系', '及', '邮购', '：', '（', '010', '）', '88254888', '，', '88258888', '。', '投诉', '请', '发邮件', '至', '，', '侵权', '举报', '请', '发邮件', '至', '联系', '：', '010', '-', '51260888', '-', '819', '，']],
 [['\n\n\n\n', '\n↘', '目标', '手机端', '转化率', '目标', '内心', '目标', '\n↘', '特点', '平台', '内容', '美学', '\n', '屏', '思维', '信息', '角度', '电商', '手机端', '转化率', '点', '美学', '营销心理学', '平台', '技巧', '书', '案例', '目的', '读者', '信息', '难易度', '信息', '效果', '案例', '内容', '范例', '范例', '时', '\n↘ ', '对象', '图片', '手机', '商业', '信息', '电商', '微商', '新媒体', '人', '平台', '淘宝', '天猫', '京东', '唯品会', '跨境电商', '海淘', 'B2C', 'APP', '商城', '微博', '微信朋友圈', '公众', '号', '头条号', 'QQ空间', '平台', '\n', '类目', '化妆品', '食品', '家电', '数码', '男女装', '鞋', '靴', '童装', '箱包', '家具', '日用品', '灯饰', '厨具', '玩具', '卫浴', '情趣', '用品', '运动户', '宠物', '用品', '工业品', '商品', '\n不限职位', '老板', '经理', '设计师', '文案师', '摄影师', '产品', '经理', '人群', '\n↘', '\n', '屏', '思维', '电商', '电商', '语言', '书', '手机端', '内容', '电商', '行业', '手机端', '详情', '图', '微商', '新媒体', '视频', '行业', '行业', '手机端', '名称', '微博', '朋友圈', '活动', '海报', '文中', '手机端', '详情', '图', '\nTa', 'target', 'audiences', '目标受众', '汉语', '拼音', '本文', '一语', '双关', '2017年', '11月', '智能', '手机', '屏', 'iPhone', '9∶18', '屏', '初期', '市场', '份额', '竖屏', '将来', '竖屏', '市场', '主流', '时间', '主流', '用户', '角度', '竖屏', '智能', '手机', '屏幕', '屏幕', '比例', '屏', '思维', '逻辑', '方法', '\n\n\n'],
  ['开卷', '之', '前', ' ', '本书', '：', '帮', '你', '把', '现有', '提升', '50%\n第一次', '看到', '这个', '，', '也许', '你', '充满', '怀疑', '，', '觉得', '不可思议', '。', '希望', '读完', '本书', '之后', '，', '你', '觉得', '这个', '完全', '可以', '实现', '，', '并没有', '什么', '了不起', '。', ' ', '本书', '：', '不', '讲', '运营', '、', '不', '讲', '构成', '、', '不', '讲', '设计', '竖', '从', '传播', '的', '探讨', '，', '关注', '不是', '设计', '、', '、', '运营', '等', '。', '中', '的', '，', '是', '为了', '帮助', '理解', '沟通', '和', '传播', '，', '这些', '不是', '，', '也', '不是', '设计', '。', '阅读', '请', '留心', '体会', '此', '点', '。', '本书', '适合', '：', '通过', '在', '上', '卖货', '、', '传递', '的', '、', '、', '\n', '不限', '：', '适合', '、', '、', '、', '、', '、', '、', '自营', '、', '、', '、', '、', '、', '、', '等', '。', '不限', '：', '适合', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '、', '外', '、', '、', '车载', '、', '等', '各类', '。', '：', '适合', '、', '运营', '、', '、', '、', '、', '等', '阅读', '。', ' ', '温馨', '提示', '竖', '因', '而', '起', '，', '因此', '本书', '主要', '围绕', '来', '组织', '。', '中', '探讨', '的', '，', '多', '指', '里', '的', '“', '”', '。', '如果', '你', '从事', '的', '是', '、', '、', '短', '、', '营销', '策划', '等', '，', '请', '用', '你们', '具体', '的', '（', '比如', '配图', '、', '配图', '、', '等', '）', '替换', '“', '”', '，', '然后', '阅读', '和', '思考', '。', '（', ' ', '，', '）', '同时', '也是', '“', '他', '/', '她', '”', '的', '，', '在', '中', '使用', '“', 'Ta', '”', '是', '。', '\n', '截至', '本书', '完成', '的', '，', '绝大多数', '配置', '的', '仍是', '9', '∶', '16', '竖', '。', '因为', ' ', 'X', '刚刚', '上市', '，', '竖', '尚', '处于', '推广', '，', '还', '可以', '忽略', '不计', '。', '至于', '9', '∶', '18', '能否', '取代', '9', '∶', '16', '成为', '，', '还', '有待', '的', '考验', '。', '本书', '从', '满足', '使用', '体验', '的', '出发', '，', '暂', '以', '9', '∶', '16', '作为', '的', '典型', '进行', '阐述', '。', '注意', '，', '无论', '是', '9', '∶', '16', '还是', '9', '∶', '18', '，', '竖', '的', '基本', '和', '改善', '是', '一样', '的', '。']]]