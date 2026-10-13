{ pkgs, inputs, ... }:

let
  zen = inputs.zen-browser.packages.${pkgs.system}.default;
  happ = pkgs.callPackage "${inputs.happ}/happ.nix" {};
in
{
  imports =
    [
       ../modules/user
    ];

  home.username = "nonex";
  home.homeDirectory = "/home/nonex";

  nixpkgs.config.allowUnfree = true;

  services.syncthing.enable = true;

  # My packages that I need but not belong to my dotfiles/ricing
  home.packages = with pkgs; [
    telegram-desktop
    zen
    vlc
    kdePackages.kdenlive
    steam
    srb2
  ];

  xdg.autostart = {
    enable = true;
    entries = 
    [
      "${zen}/share/applications/zen.desktop"
      "${pkgs.telegram-desktop}/share/applications/org.telegram.desktop.desktop"
      "${pkgs.steam}/share/applications/steam.desktop"
      "${happ}/share/applications/Happ.desktop"
    ];
  };

  xdg.configFile."niri/personal.kdl".text = ''
    input {
      keyboard {
	xkb {
	    layout "us,ru"
	    options "grp:caps_toggle,compose:ralt"
	}
      }
    }

    window-rule {
      match app-id=r#"(zen|firefox)$"#

      open-maximized true
      open-on-workspace "browser"
    }

    window-rule {
      match app-id="steam"

      open-maximized true
      open-on-workspace "games"
    }

    window-rule {
      match app-id="steam"
      exclude title="Steam"

      open-floating true
    }

    window-rule {
      match app-id="org.telegram.desktop"
      
      open-maximized true
      open-on-workspace "chat"
    }
  '';

  nixpkgs.overlays = [
    (final: prev: {
      steam = prev.steam.override {
        extraArgs = "-cef-disable-gpu-compositing";
      };
    })   
  ];
  

  programs.obsidian.enable = true;

  programs.git = {
    enable = true;

    settings = {
      user.name = "NonExistPlayer";
      user.email = "nonexistplayer@gmail.com";

      alias = {
        s = "status";
        l = "log --oneline";
      };
    };
  };

  home.stateVersion = "26.05";
}
