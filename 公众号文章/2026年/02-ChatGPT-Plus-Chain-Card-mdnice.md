---
title: 01-不用代充、不买虚拟卡！用自己的国内银行卡订阅 ChatGPT Plus
icon: blog
date: 2026-07-17 19:49:24
author: AI悦创
isOriginal: true
sticky: false
star: false
article: true
timeline: true
image: false
navbar: true
sidebarIcon: true
comment: true
lastUpdated: true
editLink: true
backToTop: true
toc: true
---

![用国内银行卡订阅 ChatGPT Plus](https://files.mdnice.com/user/128820/04520de6-b512-4a41-a657-bc7cdc08bcdc.jpg)

你好，我是悦创。

**如果你实在看教程不会，可以找我付费操作！费用视你准备的情况而定！**

这篇教程解决的就是：**人在 ChatGPT 不能直接完成开通的地区，如何用自己的账号和国内银行卡，把 Plus 真正订阅成功。**

想用自己的账号、自己的手机和国内银行发行的银行卡开通 ChatGPT Plus，可以走下面这条路径：**国内银行卡 → Google 付款中心 → Google Play → ChatGPT Android 客户端 → Plus**。

它和在 ChatGPT 网页端直接填卡不是一回事。网页端会根据银行卡的 BIN 码识别发卡地区，国内银行发行的卡即使是 Visa 或 Mastercard 单标卡，也会被直接拒绝；Google Play 对可添加的卡种相对宽松，因此可以由 Google Play 完成 Android 应用内订阅。

Google Play 在这里相当于中间付款渠道。本次实测没有额外的平台手续费；除 Plus 月费外，新增成本只有办理招行万事达人民币 IC 借记卡时支付的 5 元工本费。

这套流程最关键的不是某一个按钮，而是同时准备好四样东西：

1. 能解锁 ChatGPT 的美国网络节点；（联系我新上市的书《**编程启蒙：思维与代码**》➕好评：就**送全球上网一年**，其它平台购买无法赠送一年，只能赠送 1 个月。）
2. 美区 Google Play 和对应的 Google Payments 付款资料；
3. Google Play 可以接受的 Visa/Mastercard 单标卡；
4. 已安装官方 ChatGPT 应用的 Android 手机。

![国内银行卡通过 Google Play 订阅 ChatGPT Plus 的付款链路](https://files.mdnice.com/user/128820/1fd5ca64-6c52-45b1-a822-824c4ff864ec.jpg)

*完整链路：国内银行卡 → Google Play → ChatGPT Android 客户端。*

下面按完整顺序操作。

## 一、先准备能正常使用 ChatGPT 的网络环境

能打开 Google，不代表同一个节点一定能正常使用 ChatGPT。ChatGPT 对 IP 质量的要求通常更严格，所以不要只用“Google 能不能打开”作为判断标准。

### 1. 在 Clash Verge 中选择美国节点

打开 Clash Verge，进入代理节点列表，选择一个美国节点，并确保系统代理已经启用。

之所以优先使用美国节点，是因为后续要创建美区 Google Payments 资料、确认 Google Play 美区内容，网络地区和付款资料地区需要保持一致。

![Clash Verge 的 AI 服务解锁测试](https://files.mdnice.com/user/128820/325201cd-1070-4d8a-996b-d2d127522650.png)

*先确认 ChatGPT Web、ChatGPT iOS、Claude 等服务显示可用；失败时更换美国节点再测。*

### 2. 使用 Clash Verge 的 AI 解锁测试

Clash Verge 的相关版本或扩展中通常带有 AI 服务解锁测试，可以一键检查 GPT、Claude 等服务是否可用。

运行测试后重点看 ChatGPT/GPT 项：

- 如果显示可用或解锁成功，再继续；
- 如果显示失败，先更换另一个美国节点；
- 更换后重新测试，直到 ChatGPT 可以正常打开和登录。

这里不要省略测试。后面即使 Google Play 已经变成美区，如果节点不能正常访问 ChatGPT，安装和付款完成后仍然可能无法使用。

## 二、注册或登录自己的 ChatGPT 账号

打开 ChatGPT 官网，点击注册或登录。

常见方式包括：

- 电子邮箱注册；
- 使用 Google 账号继续；
- 使用 Apple 账号继续。

国内的 163 邮箱可以正常接收验证码，不过更推荐直接用自己长期使用的 Google 账号登录：操作更方便，后面在 Android 客户端中也容易保持账号一致。

这里我最推荐的方法，就是选择【谷歌账号】直接登录！

![ChatGPT 登录或注册入口](https://files.mdnice.com/user/128820/d31210ef-e1b0-4949-b4f2-dc56894617d0.png)

*可以使用 Google、Apple、手机号或邮箱登录；购买前务必确认最终要获得 Plus 的账号。*

请牢记当前登录的是哪一个 ChatGPT 账号。Google Play 只负责收款，Plus 权益最终会落在付款时登录的 ChatGPT 账号上。账号选错后，不能靠切换 Google Play 账号把权益自动转过去。

如果还准备使用 Codex，需要单独留意手机号验证：国内手机号无法完成这里的验证，而且以后可能不止验证一次。因此应准备一个自己能长期持有、可反复接收验证码的正规海外手机号，不要依赖一次性接码。这是使用 Codex 的额外准备项，不是 Google Play 购买 Plus 的付款条件。

下一篇文章会写如何在国内，自行配置海外手机卡教程。**欢迎一键三连➕关注！（附带上你的评论哦！评论越多，教程出的越快！）**

## 三、为什么不直接在 ChatGPT 网页端付款

ChatGPT 网页端通常提供银行卡和 PayPal 等付款方式，但国内银行卡在这里会遇到发卡地区识别。

![](https://files.mdnice.com/user/128820/6c8f9fb7-805d-4d4b-9a33-463a0e5e453e.jpg)

银行卡卡号前六位是 BIN 码。支付系统可以通过 BIN 码识别卡组织、发卡银行和发卡地区。因此：

- 不是把卡面换成 Visa 或 Mastercard 标识就一定能通过；
- 国内银行发行的 Visa/Mastercard 单标卡，在网页直付时仍可能被识别为国内发卡；
- PayPal 背后同样要绑定付款方式，国内卡也可能继续被拦截。（**实测过国内的 Paypal 可以绑定，但是美区的 Paypal 没试过。**）

![ChatGPT 网页端付款方式验证失败](https://files.mdnice.com/user/128820/5107ca51-eb9b-47fb-a5d0-162503f2d336.jpg)



*这里展示的是网页直付失败；后文改走 Google Play，不是说所有国内单标卡都不能订阅。*

所以本文不走“ChatGPT 网页端直接填国内卡”这条路，而是把 Google Play 作为应用内订阅的付款渠道：

1. 先把银行卡添加到 Google 付款中心（也常被简称为 Google Pay 绑卡）；
2. 从 Google Play 安装 ChatGPT；
3. 在 ChatGPT Android 客户端里发起 Plus 订阅；
4. 由 Google Play 向银行卡扣款。

## 四、创建美区 Google Payments 付款资料

![中国区是看不见 GPT 这类软件的](https://files.mdnice.com/user/128820/84fa3a30-44e4-4664-bbf3-e420a22bb6c0.jpg)

Google Play 和 Apple App Store 类似，也区分国家和地区。不同地区能看到的应用和订阅项目可能不同。要在 Google Play 找到 ChatGPT，先把当前 Google 账号对应的商店环境准备成美区。

决定 Google Play 地区的因素主要有两个：

- 当前 IP 所在地区；
- Google Payments 付款资料的国家/地区。

美国节点是必要条件，真正起决定作用的是 Google 付款资料。

### 1. 打开 Google 付款中心

在浏览器中登录准备在手机上使用的同一个 Google 账号，然后打开 [Google 付款中心](https://payments.google.com/)。

进入：**设置 → 付款资料 / 国家或地区**

<img src="https://files.mdnice.com/user/128820/33675cae-6190-4d45-8216-1427c99ffaec.jpg" style="zoom:25%;" />

如果这个账号从未建立过付款资料，这里可能还是空的；如果已经有其他国家或地区的付款资料，会显示现有资料。

![Google Play 美区由 IP 和支付资料共同决定](https://files.mdnice.com/user/128820/cb65af1e-104b-4c1b-b93d-621fa61a6ad9.jpg)

*美国 IP 是必要条件，Google Payments 付款资料中的国家/地区起决定作用。*

### 2. 新建美国付款资料

已有付款资料的国家/地区通常不能直接改成另一个国家。点击国家/地区旁边的编辑图标，然后选择：**新建个人资料 / 创建新的付款资料**。

![Google Payments 中新建美国付款资料](https://files.mdnice.com/user/128820/e73140bf-de6e-48e9-b0fd-4d1f3b31ca17.jpg)

*已有资料的国家/地区不能直接改时，选择“新建个人资料”，国家/地区选美国（US）。*

在国家或地区下拉菜单中选择：**美国（US）**。

![](https://files.mdnice.com/user/128820/ffe12d2f-bd28-4d7c-a8ee-e4d74af7ff12.png)

![](https://files.mdnice.com/user/128820/68774c01-db83-418d-8e44-e5b90551ba83.png)





### 3. 填写美国联系地址

![](https://files.mdnice.com/user/128820/8607b67d-7142-42eb-b11a-2ad57d9bd577.jpg)

接下来填写姓名和美国地址。付款资料名称可以自定义；地址可以借助地址生成工具准备一份美国免税州地址，再把各字段对应复制到表单。需要填写：

- 姓名；
- 街道门牌；
- 城市；
- 州；
- ZIP Code；
- 联系方式（页面要求时填写）。

街道、城市、州和 ZIP Code 必须互相对应，不能把不同地址的字段拼在一起。后面绑卡时，账单地址继续使用这一份资料。使用免税州地址的这次付款没有额外收税，但结账页面仍会显示“税费另计”，最终金额以实际订单为准。

填写完成并保存后，在付款中心确认当前已经存在一份国家/地区为美国的付款资料。

![](https://files.mdnice.com/user/128820/8d825141-41f9-4320-9cc3-4437bdd51e97.jpg)

- 美国地址生成器：[https://www.meiguodizhi.com/](https://www.meiguodizhi.com/)，也可以选择 GPT 直接生成一个地址。
- 美国免税地址：[https://usaddressgen.com/tax-free-address/](https://usaddressgen.com/tax-free-address/)

## 五、确认 Google Play 已经切换到美区

手机保持连接前面测试通过的美国节点，然后打开 Google Play。

依次进入：**右上角头像 → 设置 → 常规 → 账号和设备偏好设置 → 国家和个人资料**。

![](https://files.mdnice.com/user/128820/083adda4-fcb3-412a-a8e8-e28e5c9dd4c4.jpg)

![](https://files.mdnice.com/user/128820/e95cbd77-17da-4006-a955-3e7e3bc85114.png)

![](https://files.mdnice.com/user/128820/37fd9e1a-5bf7-4a8d-a5a1-c033cdf58d19.png)

![](https://files.mdnice.com/user/128820/9e204811-b1f2-4ddd-8c99-6a3dd9da1ecc.png)

![](https://files.mdnice.com/user/128820/8e709320-d47f-4bbb-a876-82a19e8046fe.png)



如果页面显示“美国”，说明当前 Google Play 已经按美区资料工作。

![Google Play 美区方案示意](https://files.mdnice.com/user/128820/d6ba3361-b7dc-45b6-a73a-9b4ecdc68142.jpg)

*确认美国节点和美国付款资料都已生效，再继续绑卡。*

如果仍然显示其他地区，依次检查：

1. 手机 Google Play 登录的账号，是否就是刚才新建付款资料的账号；
2. 美国节点是否仍然连接；
3. Google 付款中心是否已经保存美国资料；
4. 完全退出 Google Play 后重新打开，再检查一次。

确认商店地区后，再进入下一步绑卡。

## 六、先选对银行卡：62 开头银联卡不能直接用

![](https://files.mdnice.com/user/128820/92ab4f0b-d2b5-494a-8912-58bb7f4ff944.jpg)

进入 Google 付款中心：**支付方式 → 添加支付方式 → 添加信用卡或借记卡**。

![](https://files.mdnice.com/user/128820/6d982db3-14d9-4e7a-8c19-d9f142f7f874.png)



![Google Payments 添加信用卡或借记卡](https://files.mdnice.com/user/128820/25d22d7a-772d-4124-b4ff-e1a8a06a88ce.jpg)

*路径：支付方式 → 添加支付方式 → 添加信用卡或借记卡。*

这里不能随便拿一张国内银行卡填写，先把三类卡在两个付款渠道中的区别看清楚：

| 卡片类型 | ChatGPT 网页端直付 | 美区 Google Play |
| --- | --- | --- |
| 62 开头的普通银联卡 | 不走本文路线 | 无法添加 |
| 国内银行发行的 Visa/Mastercard 单标信用卡 | 会按 BIN 识别为国内发行，直付失败 | 可以尝试；本流程实测可用 |
| 招商银行万事达人民币 IC 借记卡（普卡） | 不走网页直付 | 本流程主推荐，实测可用 |

![Google Play 对国际卡和 62 银联卡的兼容性对比](https://files.mdnice.com/user/128820/6c119e34-08b4-43ff-94f2-f07a006a4a4d.jpg)

*Google Play 可以识别 Visa/Mastercard 国际卡通道，62 开头的普通银联卡不走这条链路。*

也就是说，关键结论不是“国内卡都不行”，而是：**国内卡在 ChatGPT 网页端直付会被拦截，但指定的国内 Visa/Mastercard 单标卡可以通过 Google Play 完成订阅。**

### 1. 不能用的卡

国内常见的 **62 开头银联卡**，即使是储蓄卡，也不能按本文这条路径直接添加为美区 Google Play 的国际卡付款方式。

![国内可尝试的 Visa 或 Mastercard 单标信用卡&招商银行万事达人民币 IC 借记卡普卡](https://files.mdnice.com/user/128820/46a955c2-47b8-406b-9375-fc4b43646e2e.jpg)

### 2. 第一类可尝试的卡：Visa/Mastercard 单标信用卡

第一类是国内银行发行、卡面只有 Visa 或 Mastercard 标识、不带银联标识的单标信用卡。

例如：

- 招商银行全币种 Visa 信用卡（卡面产品名为“全币种国际芯片卡”）；
- 工商银行星座 Visa 信用卡；
- 其他国内银行发行的 Visa/Mastercard 单标信用卡。

*关键是单标：卡面只有 Visa 或 Mastercard 标识，不带银联标识。*

这类信用卡可以尝试添加到 Google Play，但申请信用卡有审核门槛，从申请到拿卡也需要时间。

### 3. 主推荐：招商银行万事达人民币 IC 借记卡（普卡）

如果不想办信用卡，可以优先询问招商银行网点是否能办理：**招商银行万事达人民币 IC 借记卡（普卡）**。

它是人民币储蓄卡，不是信用卡。相较信用卡，办理门槛更低，线下网点可以直接申请。

申请页面可能同时出现“万事达人民币 IC 借记卡（普卡）”和“万事达金葵花卡”等产品。本文用的是前者，不要把两张卡混为一谈。

一次实际办理体验是：

- 已经持有招行普通储蓄卡；
- 到招商银行网点提出办理万事达人民币借记卡；
- 前后约十多分钟现场拿到卡；
- ~~支付了 5 元制卡工本费。~~ 不需要任何工本费，马上办、马上拿。

“十多分钟”是一次办理体验，不同城市、网点、客户身份和当期收费标准可能不同。出发前可以先致电网点，确认是否有卡板、需要哪些证件以及当前工本费。（不知道其它地方是否需要工本费，欢迎评论区分享！）

ChatGPT Plus 本身仍要按月支付约 20 美元；**这套路径省掉的是代充费、虚拟卡费和共享账号成本**。

![招商银行万事达人民币 IC 借记卡普卡](https://files.mdnice.com/user/128820/5d4e4327-e33b-4bbe-9db1-064288e0a5f1.jpg)

*选择“万事达人民币 IC 借记卡（普卡）”，不要与“万事达金葵花卡”混淆。*

## 七、在招行 App 开通“万事达卡跨境线上支付”

卡办好后不能马上默认用于境外应用内订阅。招商银行万事达人民币借记卡的跨境线上支付功能通常默认关闭，需要主动开通。

可以在办卡柜台直接让工作人员协助开通，也可以回去后在招商银行 App 中操作。

### App 操作路径

1. 打开招商银行 App；
2. 在首页搜索框输入 **快捷支付**；
3. 进入快捷支付相关功能；
4. 找到 **万事达卡跨境线上支付**；
5. 阅读协议，按页面完成开通。

![](https://files.mdnice.com/user/128820/48a9511f-15a5-4773-a427-af92085688c1.png)

如果名下有多张招行储蓄卡，页面可能默认选中了普通银联卡。此时要先切换到新办的万事达人民币借记卡，“万事达卡跨境线上支付”选项才会出现。

<img src="https://files.mdnice.com/user/128820/0768b47d-7f85-4dcd-b900-686742b2b767.png" alt="招商银行 App 切换到目标万事达借记卡" style="zoom:25%;" />

*名下有多张储蓄卡时，先切到新办的万事达人民币借记卡。*

![招商银行 App 中的万事达卡跨境线上支付入口](https://files.mdnice.com/user/128820/d0ac31cb-fc12-483b-b95d-32e18561d83c.png)

*在“快捷支付”中找到“万事达卡跨境线上支付”，按页面完成开通。*



### 提前转入足够人民币余额

这张卡是借记卡，Google Play 扣款时会直接从人民币账户余额中结算。

因此，绑卡和订阅前先向这张卡转入足够余额。余额至少要覆盖当月 ChatGPT Plus 订阅费，并为汇率换算和页面可能显示的税费留出余量。余额不足会导致订阅扣款失败。

## 八、把银行卡添加到 Google 付款中心

回到 Google 付款中心的添加银行卡页面，准备卡片背面的信息：

- 卡号；
- 有效期；
- CVC/CVV 安全码；
- 姓名；
- 账单地址。

![Google Payments 银行卡信息填写表单](https://files.mdnice.com/user/128820/aea1a3b2-961f-488a-8248-f4a8836154e9.jpg)

*依次填写卡号、有效期、CVC/CVV、姓名和前面准备的美国账单地址。*

按下面顺序填写：

1. 输入招商银行万事达人民币借记卡的卡号；
2. 输入卡片有效期；
3. 输入卡背面的 CVC/CVV；
4. 填写姓名；这一步按本流程填写即可，页面不会核对持卡人中文姓名；
5. 账单地址选择或填写前面创建的美国付款资料地址；
6. 提交保存。

卡号、有效期、CVC/CVV、验证码和完整地址都属于敏感信息，不要截图公开，也不要发给代充人员。

添加成功后，“支付方式”页面会显示这张 Mastercard。此时银行卡已经可以被 Google Play 调用。

![Google 付款方式中已经出现 Mastercard](https://files.mdnice.com/user/128820/7e726e32-3725-4962-b18c-964b67fd40e1.jpg)

*看到 Mastercard 出现在付款方式列表，才算完成 Google Play 绑卡。*

如果添加失败，按以下顺序检查：

1. 是否误用了 62 开头的银联卡；
2. 是否确实是 Visa/Mastercard 单标卡；
3. 招行 App 中是否开通“万事达卡跨境线上支付”；
4. 是否切换到了正确的万事达借记卡；
5. 卡内人民币余额是否足够；
6. 卡号、有效期和 CVC/CVV 是否输入正确；
7. Google Payments 付款资料是否已经选择美国。

## 九、从 Google Play 安装官方 ChatGPT

手机继续保持美国节点，打开 Google Play，搜索：

**ChatGPT**

进入应用详情页后，确认发布者是 **OpenAI**，再点击安装。不要安装名称相似的第三方客户端。

![Google Play 中由 OpenAI 发布的 ChatGPT 应用](https://files.mdnice.com/user/128820/354c84e0-ce57-46eb-b528-0834b7ff4d90.png)

*核对应用名和发布者 OpenAI 后再安装。*

安装完成后打开 ChatGPT，使用前面准备好的 ChatGPT 账号登录。推荐继续使用同一个 Google 账号一键登录，避免误入另一个账号。

<img src="https://files.mdnice.com/user/128820/8ebbd677-ef91-4699-a115-87d855ff4035.jpg" alt="ChatGPT Android 登录页" style="zoom:25%;" />

*用准备好的目标 ChatGPT 账号登录；Plus 权益会落在这个账号上。*

## 十、在 ChatGPT Android 客户端开通 Plus

进入 ChatGPT 主界面后，找到并点击：**获取 Plus / Get Plus**。

然后选择：**升级至 Plus**。

![ChatGPT 主界面的获取 Plus 入口](https://files.mdnice.com/user/128820/dc4de1d4-5eaf-4b96-8e5a-6d199166b9e7.png)

*进入 App 后点击左上方“获取 Plus”。*

![ChatGPT Plus 套餐页](https://files.mdnice.com/user/128820/69b922a8-93fe-4dbb-ac39-c550d3716e6d.jpg)

*切到 Plus，查看权益后点击“升级至 Plus”。*

系统随后会弹出 Google Play 订阅确认页。核对：

- 商品是 ChatGPT Plus；
- 付款 Google 账号正确；
- 付款卡是刚才添加的 Mastercard；
- 计费周期是每月；
- 自动续费时间和金额已经看清。

一次实际付款页面显示的是 **US$19.99/月**。页面还提示：Google Play 最多可能在续订日前两天发起预授权，这不等于提前两天完成续费。当次招商银行 App 显示一笔 **¥135.06 的境外消费预授权**。这两个金额只代表当次支付示例，实际人民币金额会随汇率、Google Play 定价和税费变化。 

![Google Play ChatGPT Plus 订阅确认页](https://files.mdnice.com/user/128820/f339d343-7341-42e9-b9f9-02d91acd50df.png)

*本次页面显示 US$19.99/月，并写明税费和续订日前预授权说明。*

![招商银行 135.06 元境外消费预授权](https://files.mdnice.com/user/128820/c5c11d12-55f2-4eeb-b678-6db2ec88a312.jpg)

*当次银行端显示 ¥135.06 的冻结/预授权；这不是固定人民币月费。*

确认无误后点击 **订阅**，按手机要求完成密码、指纹或银行验证。出现“订阅成功”提示后，Google Play 扣款流程就完成了。

## 十一、从 App、网页和 Codex 三处验证 Plus

付款成功后，可以从三个位置交叉确认。

### 1. ChatGPT Android App

回到 ChatGPT 主界面，打开模型选择器或设置中的订阅详情：

- 模型选择器会出现更多模型或思考强度选项；
- 账户订阅详情会显示当前为 Plus；
- 套餐页面会显示后续续费信息。

<img src="https://files.mdnice.com/user/128820/ec5563c7-7fdd-4329-8076-996a50358acb.png" alt="ChatGPT App 付款后的模型与思考强度选择器" style="zoom:25%;" />

*模型名称会更新，重点是账号已经出现 Plus 对应的模型与思考强度选项。*

![ChatGPT App 中 Plus 显示为当前套餐](https://files.mdnice.com/user/128820/dfeed79e-d7dc-409d-b456-020fed5b0f72.jpg)

*“Plus / 当前的套餐”是移动端最直接的生效证据。*

### 2. ChatGPT 网页端

在浏览器中登录同一个 ChatGPT 账号：

- 主界面的模型选择器应同步显示 Plus 对应选项；
- 设置或账单页面会显示当前套餐为 Plus；
- 可以看到下一次自动续订日期。

![ChatGPT 网页端模型选择器](https://files.mdnice.com/user/128820/8088a617-109a-4a26-96a4-65ab936db86a.png)

*回到网页端，用同一个账号核对模型和思考强度。*

![ChatGPT 网页端账单显示 Plus 和自动续订日期](https://files.mdnice.com/user/128820/b7c1a91b-12af-4348-bfa9-8e3d797c7cca.png)



*网页端账单同步显示 ChatGPT Plus 和下一次自动续订日期。*

### 3. Codex

用同一个 ChatGPT 账号打开 Codex：

- 对话框中可以查看当前可用的模型和思考强度；
- 在“使用详情和计费”中确认账号套餐显示为 Plus。

![Codex 模型与思考强度选择器](https://files.mdnice.com/user/128820/094f4680-c38a-48f2-9b91-c2e2e2e7d3fb.jpg)

*Codex 中可查看当前开放的模型与思考强度。*

![Codex 使用情况和计费显示 Plus](https://files.mdnice.com/user/128820/6f7a9927-c09b-4b26-afb7-6d108dd77587.png)

*在“使用情况和计费”中确认当前套餐为 Plus。*

不同时间开放的模型名称和额度可能变化，所以判断订阅是否成功时，以账号中的 **Plus 套餐状态** 和 Google Play 订阅记录为准，不要只盯住某一个具体模型名称。

如果银行卡已经扣款，但 App 仍显示免费版，先检查：

1. 当前 ChatGPT 账号是不是付款时登录的账号；
2. Google Play 是否显示 ChatGPT 订阅有效；
3. 完全退出 ChatGPT 后重新打开；
4. 在 App 设置中尝试“恢复购买”；
5. 再到网页端确认是否已经同步。

## 十二、续费、取消和余额管理

这份 Plus 是通过 Google Play 购买的，所以后续订阅管理也要回到 Google Play，不能只在 ChatGPT 网页端或桌面端寻找取消入口。

手机上进入：**Google Play → 右上角头像 → 付款和订阅 → 订阅 → ChatGPT**

在这里可以查看：

- 当前套餐；
- 下次续费日期；
- 付款方式；
- 取消订阅入口；
- Google Play 提供的其他管理选项。

![ChatGPT 订阅需要在 Google Play 中管理](https://files.mdnice.com/user/128820/e8f38ebc-6d94-4c28-8f20-1ba741cd4e84.jpg)

*因为购买来源是 Google Play，网页端会提示回 Google Play 更改或取消。*

需要取消时，在下次续费扣款前点击 **取消订阅**，并按页面确认。删除 ChatGPT App 不等于取消订阅。

如果继续使用招商银行万事达人民币借记卡自动续费，要在下次扣款前保证卡内有足够人民币余额。借记卡余额不足时，Google Play 自动续费会失败。

## 常见问题

### 1. 为什么 62 开头的银联储蓄卡不行？

本文使用的是 Visa/Mastercard 国际卡通道。62 开头的普通银联卡不能直接作为这套美区 Google Play 流程中的国际卡使用。

### 2. 为什么 Visa/Mastercard 单标卡在 ChatGPT 网页端也会失败？

因为网页支付会通过 BIN 码识别发卡行和发卡地区。卡面只有 Visa/Mastercard 标识，不会改变它由国内银行发行的事实。

### 3. 为什么同一张国内单标卡在 Google Play 可能可以添加？

ChatGPT 网页支付与 Google Play 使用的是不同的支付渠道和风控体系。本文正是让 Google Play 管理 Android 应用内订阅，而不是在 ChatGPT 网页端直接绑卡。

### 4. 招行万事达人民币 IC 借记卡一定能现场拿到吗？

不一定。是否有卡板、办理条件、工本费和所需时间取决于当地网点。5 元工本费和十多分钟拿卡是一次实际办理体验，出发前应先向网点确认。

### 5. 绑卡时最容易漏掉哪一步？

最容易漏掉的是在招行 App 中开通 **万事达卡跨境线上支付**，以及名下多卡时没有切换到正确的万事达借记卡。

### 6. ¥135.06 是固定月费吗？

不是。一次支付页面显示 US$19.99，当次人民币扣款为 ¥135.06；未来扣款会随汇率、Google Play 定价和税费变化。

### 7. 可以用同一张卡订阅其他 Android 应用吗？

卡片成功添加到 Google Play 后，技术上可以作为其他应用内购买的付款方式，但每个应用都有自己的地区、账号和订阅规则，应分别确认，不能因为 ChatGPT 支付成功就默认其他服务一定可用。

## 最后提醒

Google Play 菜单、银行卡风控、订阅价格和账号验证要求都可能更新，以操作时页面实际显示为准。不要向任何人泄露 Google 或 ChatGPT 密码、完整卡号、CVC/CVV、短信验证码和订单号。

::: details 公众号：AI悦创【二维码】

![](https://files.mdnice.com/user/128820/9874bcab-0687-4374-abda-79a86076579c.jpg)

:::

::: info AI悦创·编程一对一

AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++ 辅导班、java 辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发、Web、Linux」，招收学员面向国内外，国外占 80%。全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。当然，还有线下线上摄影课程、Photoshop、Premiere 一对一教学、QQ、微信在线，随时响应！微信：Jiabcdefh

C++ 信息奥赛题解，长期更新！长期招收一对一中小学信息奥赛集训，莆田、厦门地区有机会线下上门，其他地区线上。微信：Jiabcdefh

方法一：[QQ](http://wpa.qq.com/msgrd?v=3&uin=1432803776&site=qq&menu=yes)

方法二：微信：Jiabcdefh

:::

![](https://files.mdnice.com/user/128820/206f4b63-b912-447b-8223-9fb36a3875d8.jpg)
