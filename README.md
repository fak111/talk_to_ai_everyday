# Talk to AI Everyday | 与AI日常对话

[English](#english) | [中文](#chinese)

# English

> Daily AI conversations for collective growth

## Vision

Through recording daily conversations with AI, we aim to:
- Cultivate structured thinking abilities
- Share valuable Q&A insights
- Explore best practices for AI-assisted personal growth together

## How to Participate

1. Fork this repository
2. Create your conversation file using the template
3. Submit a PR to share your conversation

## Reward Program

The first 10 contributors to reach 100 points will receive a reward of 100 RMB!
- Daily conversation: +5 points
- See [reward system](./REWARD_SYSTEM.md) for more ways to earn points

## Leaderboard

| Rank | User | Points | Submissions |
|------|------|--------|-------------|
| 1    | user1| 45     | 9          |
| ...  | ...  | ...    | ...        |

[View full leaderboard](./community/leaderboard.md)

## Featured Conversations

- [Career Planning Reflection](./conversations/featured/2025-04-01_user1_zh_career-planning.md) - by @user1
- [Learning Methods Exploration](./conversations/featured/2025-04-02_user2_en_learning-methods.md) - by @user2

## Multi-language Support

We welcome conversation contributions in any language! Currently, we have examples in Chinese and English, and we look forward to adding more languages.

## Project Structure

```
talk_to_ai_everyday/
├── README.md                     # Project introduction and guidelines
├── CONTRIBUTING.md              # Detailed contribution guidelines
├── REWARD_SYSTEM.md            # Reward mechanism details
├── conversations/              # Main conversation directory
│   ├── by_user/                # Organized by username
│   ├── by_topic/               # Organized by topic
│   └── featured/               # Featured conversations
├── resources/                  # Resources folder
│   ├── templates/              # Conversation templates
│   └── guides/                 # Prompt technique guides
└── community/                  # Community folder
    └── leaderboard.md          # Points leaderboard
```

---

# Chinese

> 每日AI对话，共同成长

## 项目愿景

通过记录与AI的日常对话，我们旨在：
- 培养结构化思考能力
- 分享有价值的问答见解
- 共同探索AI辅助个人成长的最佳实践

## 参与方式

1. Fork本仓库
2. 按模板创建您的对话文件
3. 提交PR分享您的对话

## 奖励计划

首批达到100积分的10名贡献者将获得100元人民币奖励！
- 每日对话：+5分
- 更多积分获取方式见[奖励系统](./REWARD_SYSTEM.md)

## 积分排行榜

| 排名 | 用户 | 积分 | 提交次数 |
|-----|------|-----|---------|
| 1   | user1 | 45 | 9 |
| ... | ... | ... | ... |

[查看完整排行榜](./community/leaderboard.md)

## 精选对话

- [职业规划思考](./conversations/featured/2025-04-01_user1_zh_career-planning.md) - by @user1
- [学习方法探索](./conversations/featured/2025-04-02_user2_en_learning-methods.md) - by @user2

## 多语言支持

我们欢迎任何语言的对话贡献！目前已有中文、英文对话示例，期待更多语言的加入。

## 项目结构

```
talk_to_ai_everyday/
├── README.md                     # 项目简介、愿景和参与指南
├── CONTRIBUTING.md              # 贡献详细指南
├── REWARD_SYSTEM.md            # 奖励机制详细说明
├── conversations/              # 对话记录主目录
│   ├── by_user/                # 按用户名组织
│   ├── by_topic/               # 按主题分类
│   └── featured/               # 精选对话
├── resources/                  # 资源文件夹
│   ├── templates/              # 对话模板
│   └── guides/                 # 提示技巧指南
└── community/                  # 社区文件夹
    └── leaderboard.md          # 积分排行榜
```

## 奖励规则与实施方法

### 积分系统

1. **积分获取方式** ：

* 每日提交一次有质量的AI对话记录 一次pr：+5分
* 对话获得社区精选：额外+10分
* 参与每周挑战并完成：+15分
* 为项目提供功能改进或文档优化：+5至+20分（根据贡献大小）

1. **奖励机制** ：

* 首批达到100分的10名贡献者可获得100元人民币奖励
* 在排行榜上实时展示贡献者积分情况
* 每月评选"最有价值对话"，授予特别认可

### 实施方法

1. **积分追踪** ：

* 使用GitHub Actions自动计算并更新 `leaderboard.md`
* 脚本检测新的PR，验证符合要求后自动增加贡献者积分
* 积分排行榜每日更新，置顶展示在项目首页

1. **奖励发放** ：

* 通过Issues系统通知获奖者
* 提供多种奖励领取方式（微信红包、支付宝转账等）
* 公示获奖名单，增强透明度和激励效果

## 对话资源库设计

### 文件命名与组织

1. **命名规范** ：

* `YYYY-MM-DD_username_[lang]_brief-title.md`
* 示例：`2025-04-02_fak111_zh_career-planning.md`
* 语言代码使用ISO 639-1标准（zh、en、es等）

1. **目录组织** ：

* 按用户名组织的主目录结构，便于个人追踪
* 按主题建立软链接，便于内容探索
* 精选目录存放高质量对话，作为新参与者的参考

### 内容标准

1. **必要元素** ：

* YAML前置信息，包含日期、作者、语言、标签、摘要
* 对话目标与背景说明
* 完整对话内容（问答格式）
* 个人反思与收获（可选）

1. **模板示例** ：

```yaml
---
date: 2025-04-02
author: fak111
language: zh
tags: [career, planning, reflection]
summary: "探讨职业发展方向和技能提升策略"
score: 5
---

## 对话目标
探索如何在技术领域拓展个人影响力，同时平衡个人成长与价值创造。

## 对话内容
用户: [问题内容]

AI: [回答内容]

...

## 个人收获
通过这次对话，我意识到...
```

## README优化建议

README.md应简洁明了地传达项目价值并指导参与流程：

```markdown
# Talk to AI Everyday

> 每日AI对话，共同成长 | Daily AI conversations for collective growth

## 项目愿景

通过记录与AI的日常对话，我们旨在：
- 培养结构化思考能力
- 分享有价值的问答见解
- 共同探索AI辅助个人成长的最佳实践

## 参与方式

1. Fork本仓库
2. 按模板创建您的对话文件
3. 提交PR分享您的对话

## 奖励计划

首批达到100积分的10名贡献者将获得100元人民币奖励！
- 每日对话：+5分
- 更多积分获取方式见[奖励系统](./REWARD_SYSTEM.md)

## 积分排行榜

| 排名 | 用户 | 积分 | 提交次数 |
|-----|------|-----|---------|
| 1   | user1 | 45 | 9 |
| ... | ... | ... | ... |

[查看完整排行榜](./community/leaderboard.md)

## 精选对话

- [职业规划思考](./conversations/featured/2025-04-01_user1_zh_career-planning.md) - by @user1
- [学习方法探索](./conversations/featured/2025-04-02_user2_en_learning-methods.md) - by @user2

## 多语言支持

我们欢迎任何语言的对话贡献！目前已有中文、英文对话示例，期待更多语言的加入。
```

## 实施路线图

### 第一阶段（1-2周）：基础建设

1. 完善核心文档（README, CONTRIBUTING, REWARD_SYSTEM）
2. 设置基本目录结构
3. 创建对话模板和示例
4. 设置积分追踪GitHub Action

### 第二阶段（3-4周）：内容建设与社区启动

1. 添加5-10个高质量示例对话（不同主题和语言）
2. 发起首个每周挑战
3. 在相关平台宣传项目（Reddit r/AI、V2EX、掘金等）
4. 完善多语言支持资源

### 第三阶段（5-8周）：社区培育

1. 根据早期贡献调整积分规则
2. 开始评选并展示精选对话
3. 举办在线分享会，讨论有效的AI对话技巧
4. 发放首批奖励，增强项目曝光度

## 额外建议

1. **简易贡献脚本** ：创建命令行工具，帮助贡献者快速格式化和提交对话
2. **对话质量指南** ：明确定义什么是"有质量的对话"（深度、启发性、实用性等）
3. **社区大使计划** ：邀请活跃贡献者担任不同语言/主题的社区大使
4. **成果展示机制** ：鼓励参与者分享通过AI对话获得的实际成果
5. **自动化工具** ：

* PR模板确保提交包含所有必要信息
* 对话质量检查工具（基于简单规则）
* 自动生成每周社区简报

通过这一系列结构化设计和激励机制，您的项目将具备清晰的参与路径和持续发展动力。积分系统和奖励机制将促进早期用户参与，而高质量的内容组织将确保项目的长期价值。建议从核心文档和基础架构开始，循序渐进地实施上述计划。
