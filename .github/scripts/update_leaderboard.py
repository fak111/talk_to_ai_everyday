#!/usr/bin/env python3
import os
import glob
import frontmatter
from datetime import datetime
import pytz
from collections import defaultdict
import yaml

class LeaderboardUpdater:
    def __init__(self):
        self.users = defaultdict(lambda: {
            'score': 0,
            'dialogues': 0,
            'featured': 0,
            'level': '新手'
        })
        self.current_month = datetime.now(pytz.UTC).strftime('%Y-%m')
        self.monthly_stars = []

    def calculate_level(self, score):
        if score >= 200:
            return '大师'
        elif score >= 100:
            return '专家'
        elif score >= 50:
            return '进阶者'
        return '新手'

    def process_dialogue(self, file_path):
        try:
            post = frontmatter.load(file_path)
            author = post.get('author')
            if not author:
                return

            # 基础分：每个对话 +5 分
            self.users[author]['score'] += 5
            self.users[author]['dialogues'] += 1

            # 精选对话额外 +10 分
            if 'featured' in file_path:
                self.users[author]['score'] += 10
                self.users[author]['featured'] += 1

            # 检查是否是本月的对话
            date_str = post.get('date')
            if date_str:
                dialogue_date = datetime.strptime(str(date_str), '%Y-%m-%d')
                if dialogue_date.strftime('%Y-%m') == self.current_month:
                    self.monthly_stars.append((author, self.users[author]['score']))

            # 更新用户等级
            self.users[author]['level'] = self.calculate_level(self.users[author]['score'])

        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    def generate_leaderboard(self):
        # 生成排行榜内容
        now = datetime.now(pytz.UTC)
        content = [
            "# 社区积分排行榜",
            "",
            f"> 最后更新时间：{now.strftime('%Y-%m-%d %H:%M:%S')} UTC",
            "",
            "## 本月之星 🌟",
            "",
        ]

        # 添加本月之星
        monthly_stars = sorted(self.monthly_stars, key=lambda x: (-x[1], x[0]))[:3]
        if monthly_stars:
            for i, (user, score) in enumerate(monthly_stars, 1):
                content.extend([
                    f"{i}. **{user}** - {score}分",
                    ""
                ])
        else:
            content.extend(["暂无数据", ""])

        # 添加总积分排行
        content.extend([
            "## 总积分排行 🏆",
            "",
            "| 排名 | 用户 | 积分 | 对话数 | 精选数 | 等级 |",
            "|-----|------|-----|--------|--------|------|",
        ])

        # 按积分排序用户
        sorted_users = sorted(
            self.users.items(),
            key=lambda x: (-x[1]['score'], x[0])
        )

        for i, (user, data) in enumerate(sorted_users, 1):
            content.append(
                f"| {i} | {user} | {data['score']} | {data['dialogues']} | {data['featured']} | {data['level']} |"
            )

        # 添加等级分布
        content.extend([
            "",
            "## 贡献者等级分布",
            "",
        ])

        level_counts = defaultdict(int)
        for user_data in self.users.values():
            level_counts[user_data['level']] += 1

        for level, min_score in [
            ('大师', '200+'),
            ('专家', '100-199'),
            ('进阶者', '50-99'),
            ('新手', '0-49')
        ]:
            content.append(f"- {level} ({min_score}): {level_counts[level]} 人")

        # 添加里程碑达成者
        content.extend([
            "",
            "## 里程碑达成者",
            "",
            "### 首批 100 积分达成者",
        ])

        pioneers = [user for user, data in sorted_users if data['score'] >= 100][:10]
        if pioneers:
            for user in pioneers:
                content.append(f"- {user}")
        else:
            content.append("暂无数据")

        content.extend([
            "",
            "### 精选对话作者",
        ])

        featured_authors = [
            user for user, data in sorted_users
            if data['featured'] > 0
        ]
        if featured_authors:
            for user in featured_authors:
                content.append(f"- {user}")
        else:
            content.append("暂无数据")

        # 添加说明
        content.extend([
            "",
            "## 说明",
            "",
            "- 积分更新频率：每日自动更新",
            "- 精选内容评选：每月一次",
            "- 详细规则请参考 [奖励系统说明](../REWARD_SYSTEM.md)",
            ""
        ])

        return "\n".join(content)

    def update(self):
        # 处理所有对话文件
        for dialogue_path in glob.glob("conversations/**/*.md", recursive=True):
            self.process_dialogue(dialogue_path)

        # 生成并保存排行榜
        leaderboard_content = self.generate_leaderboard()
        with open("community/leaderboard.md", "w", encoding="utf-8") as f:
            f.write(leaderboard_content)

if __name__ == "__main__":
    updater = LeaderboardUpdater()
    updater.update()
