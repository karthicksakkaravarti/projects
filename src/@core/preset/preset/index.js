import themeConfig from '@themeConfig'

require('./overrides.scss')

// Skins
require('./skins/bordered.scss')
require('./skins/semi-dark.scss')

export default {
  theme: {
    themes: {
      ...themeConfig.themes,
    },
    dark:
      localStorage.getItem('erp-active-theme') === null
        ? themeConfig.app.isDark
        : localStorage.getItem('erp-active-theme') === 'dark',
  },
  rtl: themeConfig.app.isRtl,
}
