{ pkgs, config, ... }:

let
  dotfilesPath = "${config.home.homeDirectory}/.dotfiles";
  localPath = "${dotfilesPath}/config/nvim";
in
{
  home.packages = with pkgs; [
    neovim

    lua-language-server
    pyright
    nixd
  ];

  home.sessionVariables = {
    EDITOR = "nvim";
    VISUAL = "nvim";
  };

  xdg.configFile."nvim".source = config.lib.file.mkOutOfStoreSymlink localPath;
}
