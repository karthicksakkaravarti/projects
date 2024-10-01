<template>
  <layout-content-vertical-nav :nav-menu-items="navMenuItems">
    <slot></slot>

    <!-- Slot: Navbar -->
    <template #navbar="{ isVerticalNavMenuActive, toggleVerticalNavMenuActive }">
      <div class="navbar-content-container" :class="{ 'expanded-search': shallShowFullSearch }">
        <!-- Left Content: Search -->
        <div class="d-flex align-center">
          <v-icon v-if="$vuetify.breakpoint.mdAndDown" class="me-3" @click="toggleVerticalNavMenuActive">
            {{ icons.mdiMenu }}
          </v-icon>
          <app-bar-search
            :shall-show-full-search.sync="shallShowFullSearch"
            :data="appBarSearchData"
            :filter="searchFilterFunc"
            :search-query.sync="appBarSearchQuery"
            @update:shallShowFullSearch="
              handleShallShowFullSearchUpdate(isVerticalNavMenuActive, toggleVerticalNavMenuActive)
            "
          ></app-bar-search>
        </div>

        <!-- Right Content: I18n, Light/Dark, Notification & User Dropdown -->
        <div class="d-flex align-center right-row">
          <app-bar-i18n></app-bar-i18n>
          <app-bar-theme-switcher class="mx-4"></app-bar-theme-switcher>
          <app-bar-notification></app-bar-notification>
          <app-bar-user-menu></app-bar-user-menu>
        </div>
      </div>
    </template>

    <!-- Slot: Footer -->
    <template #footer>
      <div class="d-flex justify-space-between">
        <span
          >COPYRIGHT &copy; {{ new Date().getFullYear() }} <a href="" class="text-decoration-none"></a
          ><span class="d-none d-md-inline">, All rights Reserved</span></span
        >
        <div class="align-center d-none d-md-flex">
          <span>v 1.0.1</span>
        </div>
      </div>
    </template>

    <template #v-app-content>
      <app-customizer class="d-none d-md-block"></app-customizer>
      <app-base-drawer></app-base-drawer>
    </template>
  </layout-content-vertical-nav>
</template>

<script>
import LayoutContentVerticalNav from '@/@core/layouts/variants/content/vertical-nav/LayoutContentVerticalNav.vue'
import navMenuItems from '@/navigation/vertical'
import AppCustomizer from '@core/layouts/components/app-customizer/AppCustomizer.vue'

// App Bar Components
import AppBarI18n from '@core/layouts/components/app-bar/AppBarI18n.vue'
import AppBarNotification from '@core/layouts/components/app-bar/AppBarNotification.vue'
import AppBarSearch from '@core/layouts/components/app-bar/AppBarSearch.vue'
import AppBarThemeSwitcher from '@core/layouts/components/app-bar/AppBarThemeSwitcher.vue'
import AppBarUserMenu from '@core/layouts/components/app-bar/AppBarUserMenu.vue'
import AppBaseDrawer from '@/components/Drawer/AppBaseDrawer.vue'
import { mdiHeartOutline, mdiMenu } from '@mdi/js'
import { getVuetify } from '@core/utils'

// Search Data
import appBarSearchData from '@/assets/app-bar-search-data'
import { ref, watch, onMounted} from '@vue/composition-api'
import store from '@/store'

export default {
  components: {
    LayoutContentVerticalNav,
    AppCustomizer,

    // App Bar Components
    AppBarSearch,
    AppBarI18n,
    AppBarThemeSwitcher,
    AppBarUserMenu,
    AppBarNotification,
    AppBaseDrawer
  },
  setup() {
    const $vuetify = getVuetify()
    const localNavMenuItems = ref([...navMenuItems])
    // Search
    const appBarSearchQuery = ref('')
    const shallShowFullSearch = ref(false)
    const maxItemsInGroup = 5
    const totalItemsInGroup = ref({
      pages: 0,
      files: 0,
      contacts: 0,
    })
    watch(appBarSearchQuery, () => {
      totalItemsInGroup.value = {
        pages: 0,
        files: 0,
        contacts: 0,
      }
    })
    const searchFilterFunc = (item, queryText, itemText) => {
      if (item.header || item.divider) return true

      const itemGroup = (() => {
        if (item.to !== undefined) return 'pages'
        if (item.size !== undefined) return 'files'
        if (item.email !== undefined) return 'contacts'

        return null
      })()

      const isMatched = itemText.toLocaleLowerCase().indexOf(queryText.toLocaleLowerCase()) > -1

      if (isMatched) {
        if (itemGroup === 'pages') totalItemsInGroup.value.pages += 1
        else if (itemGroup === 'files') totalItemsInGroup.value.files += 1
        else if (itemGroup === 'contacts') totalItemsInGroup.value.contacts += 1
      }

      return appBarSearchQuery.value && isMatched && totalItemsInGroup.value[itemGroup] <= maxItemsInGroup
    }
    const fetchNavigationItems = async () => {
      try {
        const response = await store.dispatch('GET_ADDONS', 'navigation/')
        localNavMenuItems.value.push(...response.data)
      } catch (error) {
        console.error('Error fetching navigation items:', error)
      }
    }

    onMounted(fetchNavigationItems)

    // ? Handles case where in <lg vertical nav menu is open and search is triggered using hotkey then searchbox is hidden behind vertical nav menu overlaty
    const handleShallShowFullSearchUpdate = (isVerticalNavMenuActive, toggleVerticalNavMenuActive) => {
      if ($vuetify.breakpoint.mdAndDown && isVerticalNavMenuActive) {
        toggleVerticalNavMenuActive()
      }
    }

    return {
      navMenuItems: localNavMenuItems,
      handleShallShowFullSearchUpdate,

      // Search
      appBarSearchQuery,
      shallShowFullSearch,
      appBarSearchData,
      searchFilterFunc,

      icons: {
        mdiMenu,
        mdiHeartOutline,
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.navbar-content-container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-grow: 1;
  position: relative;
}

// ? Handle bg of autocomplete for blured appBar
.v-app-bar.bg-blur {
  .expanded-search {
    ::v-deep .app-bar-autocomplete-box div[role='combobox'] {
      background-color: transparent;
    }

    > .d-flex > button.v-icon {
      display: none;
    }

    // ===

    & > .right-row {
      visibility: hidden;
      opacity: 0;
    }

    ::v-deep .app-bar-search-toggler {
      visibility: hidden;
    }
  }
}
</style>
