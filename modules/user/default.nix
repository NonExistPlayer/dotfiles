{
  imports =
    [
      ./niri.nix
      ./ranger.nix
      ./kitty.nix
      ./neovim.nix
    ];

  nix.settings.experimental-features = "nix-command flakes";
}
