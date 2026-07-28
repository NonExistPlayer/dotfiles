{
  imports =
    [
      ./desktop
      ./neovim.nix
      ./ranger.nix
      ./zellij.nix
    ];

  nix.settings.experimental-features = "nix-command flakes";
}
