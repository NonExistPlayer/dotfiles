{ pkgs, ... }:

{
  xdg.portal.enable = true;
  xdg.portal.extraPortals = with pkgs; [ xdg-desktop-portal-gtk ];
  xdg.portal.config.common.default = [ "gtk" ];

  xdg.mimeApps = {
    enable = true;

    associations.added = {
      "inode/directory" = [ "org.gnome.Nautilus.desktop" ];
    };

    defaultApplications = {
      "inode/directory" = [ "org.gnome.Nautilus.desktop" ];
    };
  };
}
