[CmdletBinding()]
param (
    [switch]
    $Entering
);
if ($Entering) {
    & "$PSScriptRoot\.venv3\Scripts\activate.ps1";
} else {
    deactivate;
}
# This file is used by https://github.com/RobertoRojas/PSLocationTrigger
