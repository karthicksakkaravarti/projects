<template>
  <div>
    <!-- Form Drawer -->
    <v-navigation-drawer
      v-if="$store.state.Drawer.DrawerModel"
      v-model="$store.state.Drawer.DrawerModel"
      :width="$store.state.Drawer.DrawerSize"
      height="100%"
      app
      right
      temporary
      :permanent="$store.state.Drawer.DrawerModel"
    >
      <v-app-bar v-if="$store.state.Drawer.DrawerShowAppBar" dense elevation="0" flat rounded shaped>
        <v-menu rounded open-on-hover top dense offset-x style="max-width: 600px">
          <template v-slot:activator="{ on, attrs }">
            <v-icon color="primary" v-bind="attrs" v-on="on" @click="showBar = true">mdi-apps</v-icon>
          </template>

          <!-- <v-list dense>
            <v-list-item-group v-model="defaultApp">
              <v-list-item :value="item.name" v-for="(item, index) in $store.state.Apps" :key="index">
                <v-list-item-icon
                  ><v-icon color="primary">{{ item.icon }}</v-icon></v-list-item-icon
                >

                <v-list-item-title>{{ item.name }}</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list> -->
        </v-menu>

        {{
          $store.state.Drawer.DrawerFormTitle ? $store.state.Drawer.DrawerFormTitle : $store.state.Drawer.DrawerFormType
        }}
        <v-spacer></v-spacer>
        <BaseButton :icon="true" mdi_icon="mdi-close" click="CloseDrawer" :options="{}" tooltip="Close" />&nbsp;&nbsp;
      </v-app-bar>

      <v-overlay absolute :value="$store.state.Drawer.DrawerLoader">
        <v-progress-circular color="primary" indeterminate size="30"></v-progress-circular>
      </v-overlay>
      <!-- Forms Type -->
      <v-card elevation="0" :disabled="$store.state.Drawer.DrawerLoader">
        <v-card-text class="ma-0 pa-0">
          <FilterForm
            v-if="$store.state.Drawer.DrawerFilterForm"
            drawer="Drawer"
            :FORMDATA="$store.state.Drawer.DrawerForm"
            ref="Drawer_filter"
          />
          <FormGenerator v-if="$store.state.Drawer.DrawerFormAPICall" drawer="Drawer" ref="Drawer_form" />
          <template v-else>
            <component
              :is="$store.state.Drawer.DrawerFormType"
              :searchTeam="$store.state.Drawer.DrawerFormSubmit.field"
            ></component>
          </template>
        </v-card-text>
      </v-card>
      <template v-slot:append v-if="$store.state.Drawer.DrawerFilterForm || $store.state.Drawer.DrawerFormAPICall">
        <div class="ma-2 d-flex justify-start">
          <template v-if="$store.state.Drawer.DrawerFormSubmit && $store.state.Drawer.DrawerFormSubmit.btn_name">
            <v-btn
              v-if="$store.state.Drawer.DrawerFilterForm"
              small
              color="primary"
              @click="drawer_filter_generation"
              >{{ $store.state.Drawer.DrawerFormSubmit.btn_name }}</v-btn
            >
            <v-btn v-else small color="primary" @click="drawer_form_submit">{{
              $store.state.Drawer.DrawerFormSubmit.btn_name
            }}</v-btn>
            <v-divider class="ma-1" vertical></v-divider>
          </template>
          <BaseButton color="error" title="Cancel" click="CloseDrawer" :options="{}" />
        </div>
      </template>
    </v-navigation-drawer>

    <!-- SecondDrawer -->
    <v-navigation-drawer
      v-model="$store.state.SecondDrawer.DrawerModel"
      :width="$store.state.SecondDrawer.DrawerSize"
      app
      right
      temporary
      :permanent="$store.state.SecondDrawer.DrawerModel"
    >
      <v-card elevation="0" :disabled="$store.state.SecondDrawer.DrawerLoader">
        <v-card-text class="ma-0 pa-0">
          <FormGenerator drawer="SecondDrawer" ref="SecondDrawer_form" />
        </v-card-text>
      </v-card>
      <!-- <v-app-bar v-if="$store.state.SecondDrawer.DrawerShowAppBar" dense elevation="0" flat rounded shaped
        >New Customer<v-spacer></v-spacer>
        <BaseButton
          :icon="true"
          mdi_icon="mdi-close"
          click="CloseSecondDrawer"
          :options="{}"
          tooltip="Close"
        />&nbsp;&nbsp;
      </v-app-bar> -->
      <!-- <NewCustomer v-if="$store.state.SecondDrawer.DrawerFormType == 'NewCustomer'" /> -->
      <template v-slot:append>
        <div class="ma-2 d-flex justify-start">
          <v-btn small color="primary" @click="second_drawer_form_submit">{{
            $store.state.SecondDrawer.DrawerFormSubmit.btn_name
          }}</v-btn>
          <v-divider class="ma-1" vertical></v-divider>
          <BaseButton color="error" title="Cancel" click="CloseSecondDrawer" :options="{}" />
        </div>
      </template>
    </v-navigation-drawer>
  </div>
</template>

<script>
import UserInfo from '@/components/Forms/UserInfo.vue'
// import SearchGLPI from '@/apps/project/views/SearchGLPI.vue'
import BaseButton from '@/components/Button/BaseButton.vue'
// import ResourceAdd from '@/components/Forms/ResourceAdd.vue'
// import NewCustomer from '@/components/Forms/NewCustomer.vue'
// import NewCR from '@/components/Forms/NewCR.vue'
import FormGenerator from '@/components/Forms/FormGenerator.vue'
import FilterForm from '@/components/Forms/FilterForm.vue'

export default {
  data() {
    return {
      showBar: false,
      defaultApp: 'Project',
    }
  },
  components: {
    UserInfo,
    // SearchGLPI,
    BaseButton,
    // NewCustomer,
    // NewCR,
    FormGenerator,
    // ResourceAdd,
    FilterForm,
  },
  watch: {
    defaultApp(value) {
      console.log(value)
      if (value == 'Customer') {
        this.$store.dispatch('OpenDrawerOnClick', {
          ShowAppBarOnDrawer: true,
          DrawerSize: '35%',
          DrawerFormType: 'NewCustomer',
          DrawerFormAPICall: true,
          DrawerMutation: 'mutation__second_drawer',
        })
      }
    },
  },
  methods: {
    drawer_form_submit() {
      this.$refs.Drawer_form.form_validation()
    },

    drawer_filter_generation() {
      this.$refs.Drawer_filter.filter_generation()
    },

    second_drawer_form_submit() {
      this.$refs.SecondDrawer_form.form_validation()
    },
  },
}
</script>
