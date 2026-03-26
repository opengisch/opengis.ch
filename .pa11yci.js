const baseUrl = process.env.PA11Y_BASE_URL || "http://127.0.0.1:8099";
const chromeExecutable = process.env.CHROME_BIN || undefined;

module.exports = {
  defaults: {
    standard: "WCAG2AA",
    timeout: 30000,
    concurrency: 1,
    runners: ["axe"],
    ignore: ["color-contrast"],
    chromeLaunchConfig: {
      executablePath: chromeExecutable,
      args: ["--headless=new", "--no-sandbox", "--disable-dev-shm-usage"],
    },
  },
  urls: [
    `${baseUrl}/`,
    `${baseUrl}/de/`,
    `${baseUrl}/fr/`,
    `${baseUrl}/it/`,
    `${baseUrl}/qgis-support/`,
    `${baseUrl}/qfield-rapidmapper/`,
    `${baseUrl}/core-values/`,
    `${baseUrl}/category/qfield/highlights/`,
    `${baseUrl}/de/category/qfield-de/highlights/`,
    `${baseUrl}/fr/category/qfield/highlights/`,
    `${baseUrl}/it/category/qfield-it/highlights/`,
  ],
};
