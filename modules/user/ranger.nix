{ ... }:

{
  programs.ranger.enable = true;

  programs.bash.bashrcExtra = ''
  if [ -n \"$RANGER_LEVEL\" ]; then export PS1=\"[ranger]$PS1\"; fi
  '';
}
