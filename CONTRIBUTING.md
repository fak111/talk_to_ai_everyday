# Contributing Guidelines | 贡献指南

[English](#english) | [中文](#chinese)

# English

## How to Contribute

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/talk_to_ai_everyday.git
   cd talk_to_ai_everyday
   ```

2. **Create New Branch**
   ```bash
   git checkout -b feature/your-conversation-name
   ```

3. **Add Your Conversation**
   - Use the template from `resources/templates/conversation_template.md`
   - Place your file in `conversations/by_user/YOUR-USERNAME/`
   - Follow the naming convention: `YYYY-MM-DD_username_lang_brief-title.md`

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add conversation: brief description"
   git push origin feature/your-conversation-name
   ```

5. **Create Pull Request**
   - Go to GitHub and create a new PR
   - Fill in the PR template
   - Wait for review and approval

## Quality Standards

1. **Content Requirements**
   - Original conversations only
   - Clear learning objectives
   - Meaningful insights
   - Proper formatting

2. **File Structure**
   - Valid YAML front matter
   - Proper markdown formatting
   - Correct file naming
   - Appropriate tags

## Best Practices
- Focus on one main topic
- Include context and background
- Show problem-solving process
- Share personal insights
- Follow the template
- Add meaningful summaries

## Need Help?
- Review example conversations in `conversations/featured/`
- Open an issue for questions
- Join our community discussions

---

# 中文

## 如何贡献

1. **Fork并克隆**
   ```bash
   git clone https://github.com/YOUR-USERNAME/talk_to_ai_everyday.git
   cd talk_to_ai_everyday
   ```

2. **创建新分支**
   ```bash
   git checkout -b feature/your-conversation-name
   ```

3. **添加对话**
   - 使用`resources/templates/conversation_template.md`中的模板
   - 将文件放在`conversations/by_user/YOUR-USERNAME/`目录下
   - 遵循命名规范：`YYYY-MM-DD_username_lang_brief-title.md`

4. **提交更改**
   ```bash
   git add .
   git commit -m "Add conversation: brief description"
   git push origin feature/your-conversation-name
   ```

5. **创建Pull Request**
   - 前往GitHub创建新的PR
   - 填写PR模板
   - 等待审核和批准

## 质量标准

1. **内容要求**
   - 仅限原创对话
   - 明确的学习目标
   - 有价值的见解
   - 正确的格式

2. **文件结构**
   - 有效的YAML前置信息
   - 正确的markdown格式
   - 正确的文件命名
   - 适当的标签

## 最佳实践
- 专注于一个主要话题
- 包含上下文和背景
- 展示问题解决过程
- 分享个人见解
- 遵循模板
- 添加有意义的摘要

## 需要帮助？
- 查看`conversations/featured/`中的示例对话
- 有问题请开issue
- 加入社区讨论

再次感谢您的贡献！
