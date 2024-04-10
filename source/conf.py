extensions = ["nbsphinx", "sphinx_favicon"]

templates_path = []
exclude_patterns = []
html_static_path = ["wwwroot"]

project = "YiJingFramework.Nongli"
language = 'zh_CN'

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/YiJingFramework/Nongli.git",
    "use_repository_button": True,
    "extra_footer": "这里是 YiJingFramework.Nongli 的文档。前往 "
                    "<a href=\"https://yjfwk.yueyinqiu.top/\">https://yjfwk.yueyinqiu.top/</a> "
                    "查看更多项目。",
}
# html_logo = "taiji32.png"
html_title = "YiJingFramework. Nongli"
favicons = [
    {
        "href": "taiji.png" 
    },
]

nbsphinx_codecell_lexer = "csharp"
pygments_style = "vs"
nbsphinx_execute = "never"
