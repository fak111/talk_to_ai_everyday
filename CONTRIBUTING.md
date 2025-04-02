# Contributing Guidelines | 贡献指南

## How to Contribute | 如何贡献

1. **Fork & Clone | Fork并克隆**
   ```bash
   git clone https://github.com/YOUR-USERNAME/talk_to_ai_everyday.git
   cd talk_to_ai_everyday
   ```

2. **Create New Branch | 创建新分支**
   ```bash
   git checkout -b feature/your-conversation-name
   ```

3. **Add Your Conversation | 添加对话**
   - Use the template from `resources/templates/conversation_template.md`
   - Place your file in `conversations/by_user/YOUR-USERNAME/`
   - Follow the naming convention: `YYYY-MM-DD_username_lang_brief-title.md`

4. **Commit Changes | 提交更改**
   ```bash
   git add .
   git commit -m "Add conversation: brief description"
   git push origin feature/your-conversation-name
   ```

5. **Create Pull Request | 创建Pull Request**
   - Go to GitHub and create a new PR
   - Fill in the PR template
   - Wait for review and approval

## Quality Standards | 质量标准

1. **Content Requirements | 内容要求**
   - Original conversations only
   - Clear learning objectives
   - Meaningful insights
   - Proper formatting

2. **File Structure | 文件结构**
   - Valid YAML front matter
   - Proper markdown formatting
   - Correct file naming
   - Appropriate tags

3. **Language | 语言要求**
   - Any language welcome
   - Consistent language within conversation
   - Clear and concise writing
   - Proper grammar and spelling

## Best Practices | 最佳实践

1. **Conversation Quality | 对话质量**
   - Focus on one main topic
   - Include context and background
   - Show problem-solving process
   - Share personal insights

2. **Documentation | 文档**
   - Follow the template
   - Include relevant tags
   - Add meaningful summaries
   - Proper section organization

3. **Community Engagement | 社区参与**
   - Respond to feedback
   - Help review others' PRs
   - Share knowledge
   - Be respectful and inclusive

## Need Help? | 需要帮助？

- Check our [conversation guide](./resources/guides/conversation_guide.md)
- Review [example conversations](./conversations/featured/)
- Open an issue for questions
- Join our community discussions

再次感谢您的贡献！
