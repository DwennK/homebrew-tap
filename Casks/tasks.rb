cask "tasks" do
  version "0.2.0"
  sha256 "833653d7b213c2c5538541a2f852ffe2aa422a96a3c6db4dfcb31314b61c6738"

  url "https://github.com/DwennK/Tasks/releases/download/v#{version}/Tasks_#{version}_universal.dmg"
  name "Tasks"
  desc "Local-first task manager with notes, reminders, CLI and MCP"
  homepage "https://github.com/DwennK/Tasks"

  auto_updates true
  depends_on macos: ">= :monterey"
  app "Tasks.app"
end
