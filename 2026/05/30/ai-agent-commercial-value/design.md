# Visual Design — AI Agent 商业价值深度调研

## Meta

- **immersion_mode**: mega-update
- **narrative_style**: mystery-box
- **total_scenes**: 15
- **target_duration**: ~530s (~8.9min)

## Color Direction

```css
:root {
  --bg-primary: #0a0a1a;
  --bg-secondary: #1a1a2e;
  --accent-gold: #f0c040;
  --accent-red: #e74c3c;
  --accent-green: #2ecc71;
  --text-primary: #f0f0f0;
  --text-secondary: #a0a0b0;
  --text-dim: #606070;
}
```

## Typography

- **Hero**: "Noto Sans SC" 900 weight, clamp(48px, 8vw, 96px)
- **Data**: "JetBrains Mono" / "Source Code Pro" for numbers
- **Body**: "Noto Sans SC" 400 weight, 28-36px
- **Caption**: "Noto Sans SC" 300 weight, 20-24px, --text-secondary

## Emotion Curve

```json
[0.7, 0.5, 0.8, 0.9, 0.7, 0.5, 0.6, 0.6, 0.4, 0.8, 0.9, 0.7, 0.5, 0.8, 0.7]
```

## Storyboard

### S1 — Hook (emotion: 0.7)
- **visual_type**: hero
- **bg**: 暗色径向渐变，中央光晕
- **fx**: 粒子从四周汇聚到中心
- **content**: 超大标题"谁在真正赚钱？" + 副标题"AI Agent 商业价值深度调研"

### S2 — 英伟达 (emotion: 0.5)
- **visual_type**: data-hero
- **bg**: 深蓝渐变 + 网格线
- **fx**: 数据瀑布效果，数字从上方流下
- **content**: $2159亿、65%、71-75% 大号数据卡 + $17亿→$370亿 对比箭头

### S3 — 模型亏损 (emotion: 0.8)
- **visual_type**: compare
- **bg**: 深红到深紫渐变
- **fx**: 循环箭头动画（供应商融资）
- **content**: 营收$43亿 vs 烧$25亿 对比图 + $1000亿循环融资标注

### S4 — 核心提问 (emotion: 0.9)
- **visual_type**: hero
- **bg**: 冷暖分割（左蓝右橙）
- **fx**: 闪电分割线
- **content**: 巨大问号"Agent有价值吗？" + "答案取决于你在哪"

### S5 — 悲观面 (emotion: 0.7)
- **visual_type**: data-alert
- **bg**: 暗红渐变 + 警告纹理
- **fx**: 数字下沉效果
- **content**: 95% 零ROI 超大红字 + MIT/BCG 数据卡 + $100/8月惨状

### S6 — 乐观面 (emotion: 0.5)
- **visual_type**: data-hope
- **bg**: 暗绿到亮青渐变
- **fx**: 数字上升浮动
- **content**: 74% 首年ROI 绿色大字 + Cursor $5亿ARR 数据卡

### S7 — 第一梯队 (emotion: 0.6)
- **visual_type**: tier-list
- **bg**: 金色底色 + 微光粒子
- **fx**: 金色粒子飘浮
- **content**: 三块数据横排（编程$40亿 / 客服降本10-50x / 安全-70%风险）

### S8 — 第二梯队 (emotion: 0.6)
- **visual_type**: compare-row
- **bg**: 银蓝商务渐变
- **fx**: 进度条增长动画
- **content**: BPO支出对比 + 营销效率 +32%/+46% + 法律AI $8000 vs $12万

### S9 — 第三梯队 (emotion: 0.4)
- **visual_type**: dim-list
- **bg**: 灰色低饱和度
- **fx**: 淡出消散效果
- **content**: 灰暗列表 + "不是没价值，是变现太难"

### S10 — 路径一 (emotion: 0.8)
- **visual_type**: path-highlight
- **bg**: 深绿增长渐变
- **fx**: 向上箭头粒子
- **content**: 垂直替代逻辑图 + YC 300个独角兽 + $199-799 license 模型

### S11 — 路径二 (emotion: 0.9)
- **visual_type**: data-explosion
- **bg**: 深紫到金爆炸渐变
- **fx**: 爆炸扩散粒子
- **content**: Mercor 人均$450万对比柱状图 + 利润率 15-25%→50-65%

### S12 — 路径三 (emotion: 0.7)
- **visual_type**: code-data
- **bg**: 深色代码风格背景
- **fx**: 代码雨效果
- **content**: $40亿市场 +600%增速 + Cursor $5亿 ARR 数据块

### S13 — 四大坑 (emotion: 0.5)
- **visual_type**: warning-list
- **bg**: 暗红警告渐变
- **fx**: 裂缝破碎效果
- **content**: 四个X标记红色列表（薄Wrapper/通用聊天/卖工具/卖铲子）

### S14 — 终极判断 (emotion: 0.8)
- **visual_type**: verdict
- **bg**: 金色到深蓝渐变
- **fx**: 金色光点汇聚
- **content**: 验证表格（卖token/硬件/电力/Agent 各行对错）+ 金句大标题

### S15 — CTA (emotion: 0.7)
- **visual_type**: cta
- **bg**: 温暖金色渐变
- **fx**: 柔和光晕
- **content**: 三个问题列表 + 关注CTA
