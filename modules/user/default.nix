{
  imports =
    [
      ./niri.nix
      ./ranger.nix
      ./kitty.nix
      ./neovim.nix
      ./waybar.nix
    ];

  nix.settings.experimental-features = "nix-command flakes";
}
