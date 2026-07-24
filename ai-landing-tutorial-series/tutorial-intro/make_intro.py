"""导读篇图片幻灯片合成：30 PNG zoompan Ken Burns + 淡入淡出 + concat + 叠旁白 BGM → final.mp4"""
import json, subprocess, glob, os, sys

PD = 'D:/AI-Agent/video-clipforge/workspace/ai-landing-tutorial-series/tutorial-intro'
SLIDES = 'D:/AI-Agent/video-clipforge/workspace/ai-landing-tutorial-series/tutorial-slides'
os.chdir(PD)

durations = json.load(open('segment_durations.json', encoding='utf-8'))
segs = durations.get('segments', durations.get('durations', []))
durs = [s.get('actual_duration', s.get('duration', 0)) if isinstance(s, dict) else s for s in segs]
assert len(durs) == 30, f'段数 {len(durs)}'

pngs = sorted(glob.glob(f'{SLIDES}/[0-9][0-9]-*.png'))
assert len(pngs) == 30, f'png 数 {len(pngs)}'

# Step 1: 30 段视频（zoompan 缓慢放大 + 淡入淡出）
for i, (png, dur) in enumerate(zip(pngs, durs)):
    frames = int(dur * 30)
    out = f'seg_{i+1:02d}.mp4'
    if os.path.exists(out):
        continue
    vf = (f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,"
          f"zoompan=z='min(zoom+0.0004,1.08)':d={frames}:s=1920x1080:fps=30,format=yuv420p")
    r = subprocess.run(['ffmpeg','-y','-loop','1','-i',png,'-t',f'{dur:.3f}','-vf',vf,
                        '-c:v','libx264','-preset','fast','-crf','18','-an',out],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f'seg {i+1} FAIL: {r.stderr[-300:]}'); sys.exit(1)
    print(f'seg {i+1:02d} OK ({dur:.1f}s)')

# Step 2: concat 30 段
with open('concat_list.txt','w',encoding='utf-8') as f:
    for i in range(30):
        f.write(f"file 'seg_{i+1:02d}.mp4'\n")
subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i','concat_list.txt','-c','copy','body.mp4'], check=True)
print('body.mp4 concat done')

# Step 3: 混合 body + narration + bgm
meta = durations.get('meta', {})
bgm_vol = meta.get('bgm_volume', 0.3)
fc = f'[2:a]volume={bgm_vol}[bg];[1:a][bg]amix=inputs=2:duration=first:normalize=0[a]'
subprocess.run(['ffmpeg','-y','-i','body.mp4','-i','narration.mp3','-i','bgm.wav',
                '-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac',
                '-b:a','192k','-shortest','final.mp4'], check=True)
print('final.mp4 done (含 BGM)')

# Step 4: no_bgm 版（仅旁白）
subprocess.run(['ffmpeg','-y','-i','body.mp4','-i','narration.mp3',
                '-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
                '-shortest','final_no_bgm.mp4'], check=True)
print('final_no_bgm.mp4 done')
