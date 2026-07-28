{
  imports =
    [
      ./desktop
      ./ranger.nix
      ./neovim.nix
    ];

  nix.settings.experimental-features = "nix-command flakes";
}
