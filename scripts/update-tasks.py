#!/usr/bin/env python3
"""Update only Tasks from its public GitHub release; preserve other casks."""
import hashlib
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

repo = 'DwennK/Tasks'
request = Request(f'https://api.github.com/repos/{repo}/releases/latest', headers={'Accept':'application/vnd.github+json','User-Agent':'Tasks-Homebrew'})
with urlopen(request, timeout=30) as response:
    release = json.load(response)
version = release['tag_name'].removeprefix('v')
if not re.fullmatch(r'\d+\.\d+\.\d+', version) or release['draft'] or release['prerelease']:
    raise SystemExit('Expected a published stable semantic version')
path = Path(__file__).resolve().parents[1] / 'Casks/tasks.rb'
if path.exists() and f'version "{version}"' in path.read_text():
    print('Tasks cask is already current.')
    raise SystemExit(0)
name = f'Tasks_{version}_universal.dmg'
asset = next(a for a in release['assets'] if a['name'] == name)
url = f'https://github.com/{repo}/releases/download/v{version}/{name}'
if asset['browser_download_url'] != url:
    raise SystemExit('Unexpected download URL')
digest = hashlib.sha256()
with urlopen(url, timeout=60) as response:
    while chunk := response.read(1024*1024):
        digest.update(chunk)
checksum = digest.hexdigest()
if asset.get('digest') and asset['digest'] != f'sha256:{checksum}':
    raise SystemExit('GitHub asset digest does not match the download')
path.write_text(f'''cask "tasks" do
  version "{version}"
  sha256 "{checksum}"

  url "https://github.com/{repo}/releases/download/v#{{version}}/Tasks_#{{version}}_universal.dmg"
  name "Tasks"
  desc "Local-first task manager with notes, reminders, CLI and MCP"
  homepage "https://github.com/{repo}"

  auto_updates true
  depends_on macos: :monterey

  app "Tasks.app"
end
''')
print(f'Updated Tasks cask to {version}.')
