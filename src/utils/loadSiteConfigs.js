import fs from "fs";
import path from "path";

const SITES_DIR = path.join(process.cwd(), "sites");

export const loadSiteConfigs = () => {
  const siteConfigs = [];

  // Read all folders in "sites"
  const siteFolders = fs.readdirSync(SITES_DIR);

  siteFolders.forEach((folder) => {
    const configPath = path.join(SITES_DIR, folder, "site_config.json");

    // Check if site_config.json exists in the folder
    if (fs.existsSync(configPath)) {
      const config = JSON.parse(fs.readFileSync(configPath, "utf-8"));
      siteConfigs.push(config);
    }
  });

  return siteConfigs;
};
