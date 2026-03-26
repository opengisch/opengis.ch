const baseUrl = process.env.LIGHTHOUSE_BASE_URL || "http://127.0.0.1:8100"

module.exports = {
  ci: {
    collect: {
      numberOfRuns: 1,
      url: [
        `${baseUrl}/`,
        `${baseUrl}/de/`,
        `${baseUrl}/fr/`,
        `${baseUrl}/it/`,
        `${baseUrl}/core-values/`,
        `${baseUrl}/qgis-support/`,
        `${baseUrl}/qfield-rapidmapper/`,
        `${baseUrl}/category/qfield/highlights/`
      ],
      settings: {
        chromeFlags: "--headless=new --no-sandbox",
        preset: "desktop"
      }
    },
    assert: {
      assertions: {
        "categories:performance": [
          "warn",
          {
            minScore: 0.7
          }
        ],
        "categories:accessibility": [
          "error",
          {
            minScore: 0.9
          }
        ],
        "categories:best-practices": [
          "error",
          {
            minScore: 0.9
          }
        ],
        "categories:seo": [
          "warn",
          {
            minScore: 0.9
          }
        ]
      }
    },
    upload: {
      target: "filesystem",
      outputDir: "./reports/lighthouseci"
    }
  }
}
