# 原神角色 Skill 集合 for Trae IDE

110个《原神》可玩角色的 [Trae IDE Skill](https://docs.trae.com.cn/) 文件集合，让 AI 助手能以角色的身份、语气和性格与你互动。

## 项目结构

```
.trae/skills/
├── paimon/           # 派蒙
├── zhongli/          # 钟离
├── venti/            # 温迪
├── raidenshogun/     # 雷电将军
├── nahida/           # 纳西妲
├── furina/           # 芙宁娜
├── mavuika/          # 玛薇卡
├── ... (共110个角色)
```

每个角色目录下包含一个 `SKILL.md` 文件，定义了该角色的：
- **核心身份**（星级、武器、命之座、CV等数据库级别信息）
- **性格特点**（深度性格分析与内在矛盾）
- **说话语气**（经典台词与不同情景语气）
- **行为准则**（角色扮演时的核心规则）

## 使用方式

### 1. Trae IDE（原生支持）

Trae IDE 直接读取 `.trae/skills/` 目录，无需额外配置：

```
1. 将整个项目（或 .trae/skills/ 目录）复制到你的 Trae IDE 工作目录
2. 在对话中输入 @钟离 或 /skill zhongli
3. 也可以直接说「以派蒙的口吻回答」
```

### 2. ChatGPT / 网页版 / 移动端

**方法 A：粘贴 Prompt（最通用）**

```
1. 打开 prompts/ 目录，找到对应角色文件（如 prompts/zhongli.md）
2. 复制全部内容
3. 在 ChatGPT 对话中粘贴，发送后 AI 将进入角色扮演模式
```

**方法 B：创建 GPTs（一次配置，永久使用）**

```
1. 打开 ChatGPT → 探索 GPTs → 创建
2. Instructions 中粘贴 prompts/zhongli.md 的完整内容
3. Name 填写角色名（如「钟离」）
4. 保存，之后随时通过 @钟离 调用
```

> 提示：`output/gpts/gpts_roles.json` 包含全部 109 个角色的 GPTs 配置，可配合 API 或批量导入工具使用。

### 3. Claude / Claude Projects

**方法 A：直接粘贴**

```
1. 打开 prompts/ 目录，复制对应角色内容
2. 粘贴到 Claude 对话中，AI 将进入角色扮演模式
```

**方法 B：Claude Projects（推荐）**

```
1. 创建 Claude Project
2. 在 Project Knowledge 中上传 output/claude/ 下的文件
3. 在 System Prompt 中写："你是{角色名}，请完全按照 Project Knowledge 中的角色设定说话"
4. 此后在此 Project 中每次对话都是该角色
```

### 4. Cursor IDE

```
1. 将 output/cursor_rules/ 目录重命名为 .cursor/rules/ 并放入项目根目录
2. 或者直接复制整个 output/cursor_rules/ 的内容到你的项目的 .cursor/rules/
3. 在 Cursor 对话中通过 @规则名 或直接说「以钟离的口吻回答」
```

### 5. Cline / Roo Code / VS Code 插件类 Agent

```
1. 打开 prompts/ 目录，找到对应角色文件
2. 复制全部内容到 Agent 的 Custom Instructions / System Prompt 设置中
3. 之后在该 Agent 中对话即进入角色扮演模式
```

### 6. 其他支持 System Prompt 的 Agent

几乎所有 AI Agent 都支持 System Prompt。通用步骤：

```
1. 从 prompts/ 中找到角色文件
2. 粘贴到 System Prompt / Custom Instructions / 角色设定 区域
3. 开始对话
```

### 自动转换

修改 `.trae/skills/` 中的角色定义后，用以下脚本一键同步到所有平台格式：

```bash
python converters/convert.py prompts    # 纯 Markdown（全部 Agent 通用）
python converters/convert.py claude     # Claude Projects
python converters/convert.py gpts       # ChatGPT GPTs 配置
python converters/convert.py cursor     # Cursor IDE Rules
```

| 输出目录 | 适用平台 | 文件数 |
|----------|----------|--------|
| `prompts/` | 全部 Agent（通用） | 109 `.md` |
| `output/claude/` | Claude Projects | 109 `.md` |
| `output/gpts/gpts_roles.json` | ChatGPT GPTs | 1 `.json` |
| `output/cursor_rules/` | Cursor IDE | 109 `.mdc` |

## 角色列表

### 蒙德
安柏、可莉、诺艾尔、菲谢尔、砂糖、雷泽、迪奥娜、芭芭拉、班尼特、罗莎莉亚、丽莎、米卡、琴、迪卢克、凯亚、温迪、优菈、阿贝多、莫娜

### 璃月
香菱、北斗、行秋、重云、凝光、烟绯、辛焱、云堇、瑶瑶、嘉明、蓝砚、刻晴、七七、甘雨、魈、胡桃、申鹤、夜兰、闲云、钟离

### 稻妻
早柚、托马、九条裟罗、久岐忍、鹿野院平藏、五郎、绮良良、神里绫华、神里绫人、枫原万叶、雷电将军、八重神子、荒泷一斗、珊瑚宫心海、宵宫

### 须弥
柯莱、多莉、莱依拉、珐露珊、坎蒂丝、卡维、赛诺、提纳里、妮露、纳西妲、艾尔海森、迪希雅、流浪者、塞索斯

### 枫丹
夏洛蒂、菲米尼、琳妮特、夏沃蕾、艾梅莉埃、芙宁娜、那维莱特、娜维娅、林尼、莱欧斯利、克洛琳德、希格雯、千织、阿蕾奇诺

### 纳塔
卡齐娜、基尼奇、玛拉妮、欧洛伦、伊安珊、恰斯卡、瓦蕾莎、希诺宁、伊法、茜特菈莉、玛薇卡

### 挪德卡莱
爱诺、菲林斯、哥伦比娅、伊涅芙、叶洛亚、莉奈娅、菈乌玛、兹白、雅珂达、奈芙尔

### 其他
埃洛伊、丝柯克、梦见月瑞希、白术、达达利亚

## 许可

本项目为粉丝创作，仅供学习和娱乐使用。所有角色版权归 miHoYo/HoYoverse 所有。
