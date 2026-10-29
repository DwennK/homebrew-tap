# chattymin/homebrew-tap

chattymin의 macOS 앱 Homebrew tap.

## PokeTokenBar

오늘 사용한 AI 코딩 토큰량을 macOS 메뉴바에 표시하고, 그 사용량을 자라나는 포켓몬으로 바꿔주는 앱.

```bash
brew install --cask chattymin/tap/poke-token-bar
```

요구사항: `ccusage` CLI (`npm install -g ccusage`). 소스: https://github.com/chattymin/poke-token-bar

## Bobber

MacBook 노치 위에 고양이가 앉아 낚시를 한다. 무엇이 잡히는지는 지금 바깥 날씨가 정한다.

```bash
brew install --cask chattymin/tap/bobber
```

요구사항: macOS 14 이상. 소스는 아직 비공개다.

## Tasks

A local-first macOS task manager with notes, reminders, CLI and MCP.

```sh
brew install --cask dwennk/tap/tasks
```

Supports macOS 12+ on Apple Silicon and Intel. Downloads the universal app from [DwennK/Tasks releases](https://github.com/DwennK/Tasks/releases). The app can update itself; an explicit Homebrew update is also available:

```sh
brew upgrade --cask --greedy dwennk/tap/tasks
```

Current Tasks builds are ad hoc signed, not notarized by Apple. macOS may require normal Privacy & Security approval on first launch. This cask does not disable Gatekeeper or remove quarantine. Uninstalling does not delete the Tasks database.

The Tasks workflow checks for new public releases daily and can be run manually. It changes only `Casks/tasks.rb`, calculates the DMG's SHA-256 checksum and checks GitHub's asset digest when supplied. The other casks retain their original upstream sources.
