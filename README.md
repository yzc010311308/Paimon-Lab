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

### Trae IDE（原生支持）
将 `.trae/skills/` 目录复制到你的 Trae IDE 项目根目录，通过 `@技能名` 或 `/skill 技能名` 调用角色。

### 其他 AI Agent / IDE
本项目提供自动转换脚本，一键生成多种平台格式：

```bash
python converters/convert.py prompts    # 纯 Markdown Prompt（通用 Agent）
python converters/convert.py claude     # Claude Projects 格式
python converters/convert.py gpts       # ChatGPT GPTs 配置（JSON）
python converters/convert.py cursor     # Cursor Rules 格式
```

| 目录 | 用途 |
|------|------|
| `prompts/` | 纯 Markdown 角色 Prompt，适合复制到任何 Agent 的 System Prompt |
| `output/claude/` | Claude Projects 可导入格式 |
| `output/gpts/gpts_roles.json` | 109 个角色的 GPTs 配置，可批量导入 ChatGPT |
| `output/cursor_rules/` | Cursor IDE 的 `.cursor/rules/` 格式 |

### 直接使用（所有平台通用）
直接对 AI 说「以钟离的口吻回答」，然后从 `prompts/` 里找到对应角色的内容粘贴即可。

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
