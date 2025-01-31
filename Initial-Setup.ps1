# Check if the script is running as Administrator
$CurrentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
$Principal = New-Object Security.Principal.WindowsPrincipal($CurrentUser)
$AdminRole = [Security.Principal.WindowsBuiltInRole]::Administrator

if (-not $Principal.IsInRole($AdminRole)) {
    Write-Host "Restarting script as Administrator..."
    Start-Process powershell -ArgumentList "-File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Download the Winget installer
curl -L -o Microsoft.DesktopAppInstaller.msixbundle "https://github.com/microsoft/winget-cli/releases/download/v1.9.25200/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"

# Install the Winget package
Add-AppxPackage -Path Microsoft.DesktopAppInstaller.msixbundle

# Install applications using Winget
winget install --id=Microsoft.Teams -e
winget install --id=Microsoft.VisualStudioCode -e
winget install --id=Python.Python.3.11 -e
winget install --id=Spotify.Spotify -v "1.2.56.502.ga68d2d4f" -e
winget install --id=VideoLAN.VLC -e
winget install --id=HTTPToolKit.HTTPToolKit -e
winget install --id=Google.Chrome -e
winget install --id=Docker.DockerDesktop -e
winget install --id=Astronomer.Astro -e
