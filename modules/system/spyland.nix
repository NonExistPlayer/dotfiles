{
  programs.spyland = {
    enable = true;

    settings = {
      groups = [
	{
	  name = "  Games";
	  color = "green";

	  app_ids = [ "cs2" ];
	  workspaces = [];
	}
      ];
      aliases = [
	{
	  name = "Zen Browser";
	  color = "#FFAAAA";

	  app_ids = [ "zen" ];
	}
	{
	  name = "Obsidian";
	  color = "dark_magenta";

	  app_ids = [ "md.obsidian.Obsidian" ];
	}
	{
	  name = "Steam";
	  color = "dark_blue";

	  app_ids = [ "steam" ];
	}
	{
	  name = "Counter-Strike 2";
	  color = "yellow";

	  app_ids = [ "cs2" ];
	}
	{
	  name = "Amberol";
	  color = "cyan";

	  app_ids = [ "io.bassi.Amberol" ];
	}
	{
	  name = "Telegram";
	  color = "cyan";

	  app_ids = [ "org.telegram.desktop" ];
	}
      ];
    };
  };
  services.spylandd.enable = true;
  services.spylandd.backends.niri.enable = true;
}
