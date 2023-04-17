import json

# 解析评论
def parse_comments(markdown, comments, indent=0):
    for comment in comments:
        # 解析评论内容和作者
        comment_content = comment['content']
        comment_author = comment['author']
        # 构造缩进
        indent_str = ' ' * indent
        # 构造Markdown格式的评论
        markdown += f"{indent_str}- {comment_content}  \n{indent_str}  - *{comment_author}*  \n"
        # 如果有回复，递归解析回复
        if 'anchor_comments' in comment:
            anchor_comments = comment['anchor_comments']
            # 解析根评论
            if 'root_comment' in anchor_comments:
                root_comment = anchor_comments['root_comment']
                markdown += f"{indent_str}  - "
                parse_comments(markdown, [root_comment], indent + 2)
            # 解析其他回复
            if 'comments' in anchor_comments:
                reply_comments = anchor_comments['comments']
                parse_comments(markdown, reply_comments, indent + 2)

# 加载json文件
with open('26765290.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 解析文章标题和正文
title = data['question']
content = data['content']
author = data['author']
# 构造Markdown格式的文章
markdown = f"- 作者：{author}\n\n{content}\n\n"
# markdown = f"# {title}\n\n - 作者：{author}\n\n{content}\n\n"

# 解析文章评论并添加到Markdown中
comments = data['featured_comments']
parse_comments(markdown, comments)
markdown += '\n'

# 将Markdown保存到文件中
with open('md\\' + title + '.md', 'w', encoding='utf-8') as f:
    f.write(markdown)

