{
  services.btrfs.autoScrub.enable = true;
  services.btrfs.autoScrub.interval = "weekly";

  services.snapper = {
    snapshotInterval = "1w";
    cleanupInterval = "1m";

    configs = {
      root = {
	SUBVOLUME = "/";
	TIMELINE_CREATE = true;
	TIMELINE_CLEANUP = true;
	TIMELINE_LIMIT_MONTHLY = 1;
      };

      home = {
	SUBVOLUME = "/home";
	TIMELINE_CREATE = true;
	TIMELINE_CLEANUP = true;
	TIMELINE_LIMIT_MONTHLY = 2;
      };
    };
  };
}
