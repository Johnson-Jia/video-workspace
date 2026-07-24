"""导读篇封面 3 版截图:16:9 1920x1080 / 4:3 1440x1080 / 3:4 1080x1440
playwright viewport 匹配各版 data-width/height,retina deviceScaleFactor=2
"""
import os, sys
from playwright.sync_api import sync_playwright

BASE = 'D:/AI-Agent/video-clipforge/workspace/ai-landing-tutorial-series'

# 16:9 已有 HTML,直接用
# 4:3 / 3:4 需要先按变体规则缩放生成 HTML(同 E13 -43/-34 模式)

VERSIONS = [
    # (html, png, viewport_w, viewport_h)
    ('导读-cover.html',      '导读-cover.png',    1920, 1080),
    ('导读-cover-43.html',   '导读-cover-43.png', 1440, 1080),
    ('导读-cover-34.html',   '导读-cover-34.png', 1080, 1440),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for html_name, png_name, vw, vh in VERSIONS:
            html_path = os.path.join(BASE, html_name)
            if not os.path.exists(html_path):
                print(f'SKIP {html_name} (不存在)', flush=True)
                continue
            context = browser.new_context(
                viewport={'width': vw, 'height': vh},
                device_scale_factor=2,  # retina
            )
            page = context.new_page()
            page.goto('file:///' + html_path.replace('\\', '/'))
            page.wait_for_load_state('networkidle')
            # 等字体/渲染稳定
            page.wait_for_timeout(800)
            png_path = os.path.join(BASE, png_name)
            page.screenshot(path=png_path, clip={'x': 0, 'y': 0, 'width': vw, 'height': vh})
            context.close()
            print(f'OK {png_name} @ {vw}x{vh} (retina x2)', flush=True)
        browser.close()


if __name__ == '__main__':
    main()
