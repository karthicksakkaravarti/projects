<template>
  <div>
    <v-autocomplete
      color="primary"
      :search-input.sync="search"
      :loading="isLoading"
      :items="users"
      v-model="ComputedUsers"
      :item-text="itemtext"
      :item-value="itemvalue"
      :rules="rules"
      :filter="filterObject"
      clearable
      dense
      :placehoder="placehoder"
      :label="label"
      :outlined="outlined"
      :readonly="readonly"
      :multiple="multiple"
    >

      <template v-if="!readonly" v-slot:label>
        {{ label }} <span style="color: red" v-if="field && field.required">*</span>
      </template>

      <template v-slot:item="data">
        <template>
          <v-list-item-avatar>
            <v-avatar color="primary" size="30">

              <img v-if="avatarURL" :src="stringFormat(avatarURL, data.item.employee_id)"
              :alt="data.item.full_name
                  .split(' ')
                  .map(str => str[0])
                  .join('')"
                  :class="`white--text ${data.item.full_name.split(' ').length > 2 ? 'text-caption' : ''} `" />

              <span v-else :class="`white--text ${data.item.full_name.split(' ').length > 2 ? 'text-caption' : ''} `">{{
                data.item.full_name
                  .split(' ')
                  .map(str => str[0])
                  .join('')
              }}</span>
            </v-avatar>
          </v-list-item-avatar>
          <v-list-item-content >
            <v-list-item-title>{{ data.item.full_name }} ( {{ data.item.employee_id }} )</v-list-item-title>
            <v-list-item-subtitle>{{ data.item.title }}</v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </template>

      <template v-slot:selection="data">
        <v-chip
          v-bind="data.attrs"
          :input-value="data.selected"
          @click="data.select"
        >
          <v-avatar left color="primary" size="30">
            <img v-if="avatarURL" :src="stringFormat(avatarURL, data.item.employee_id)"
              :alt="data.item.full_name
                  .split(' ')
                  .map(str => str[0])
                  .join('')"
                  :class="`white--text ${data.item.full_name.split(' ').length > 2 ? 'text-caption' : ''} `" />
          </v-avatar>
          {{ data.item.full_name }}

        </v-chip>

      </template>

      <template v-slot:prepend>
        <v-icon
          v-if="ComputedUsers !== $store.state.user.name"
          title="Assign to me" @click="selectMe">
          {{ assignToMe }}
        </v-icon>
      </template>

    </v-autocomplete>
  </div>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'

// Mixins
import { Users } from '@/mixins/Users'
export default {
  mixins: [Users],
  components: {
    BaseButton,
  },
  props: {
    label: { required: true, type: String },
    field: { default: {} },
    rows: { default: 5 },
    rowheight: { default: 20 },
    prependicon: { default: '' },
    appendicon: { default: '' },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    dropdownitems: [],
    placehoder: { default: '' },
    itemtext: '',
    itemvalue: '',
    loading: false,
    outlined: { default: false },
    readonly: { default: false },
    avatarURL: { default: '/pm/api/users/{}/profile/' },
    assignToMe: { default: 'mdi-account-check-outline' },
    multiple: { default: false }
  },

  computed: {
    rules() {
      var data = []
      if (this.field && this.field.required) {
        data.push(v => !!v || this.field.name + ' is required')
      } else {
        data = []
      }
      return data
    },
    ComputedUsers: {
      get() {
        return this.field.value
      },
      set(newName) {
        // Setting Field
        this.field.value = newName
        return ''
      },
    },
    // ComputedUserItems: {
    //   get() {
    //     return this.UsersList
    //   },
    //   set(newName) {
    //     return ''
    //   },
    // },
  },
  mounted() {
    try {
      if (this.field.valuelist && this.field.valuelist.length > 0) {
        this.SetUsersList(this.field.valuelist)
      } else {
        this.isLoading = true;
        this.API_MASTER_USERS('').then(data => {
          if (data.data.results.length != 0) {
            this.SetUsersList(data.data.results);
          }
          this.isLoading = false;
        }).catch(() => {
          this.isLoading = false;
        })
      }
    } catch (err) {
      console.error(err)
    }
  },
  data() {
    return {
      search: '',
      isLoading: false,
      users: [],
    }
  },
  watch: {
    field: {
      handler(value) {
        if (value && value.name == 'Cost Center') {
          this.$store.state.Drawer.DrawerForm.filter(obj => {
            return obj.name == 'Department'
          })[0].value = value.valuelist.filter(obj => {
            return obj.id == value.value
          })[0].name
        }
      },
      deep: true,
    },
    search(val) {
      // Items have already been requested
      if (this.isLoading) return
      this.isLoading = true
      if (val) {
        this.API_MASTER_USERS('?search=' + val)
          .then(data => {
            if (data.data.results.length != 0) {
              this.SetUsersList(data.data.results)
            }
            this.isLoading = false
          })
          .catch(() => {
            this.isLoading = false
          })
      } else {
        this.isLoading = false
      }
    },
  },

  methods: {
    SetUsersList(value) {
      this.users = value
    },

    filterObject(item, queryText, itemText) {
      return (
        item.full_name.toLocaleLowerCase().indexOf(queryText.toLocaleLowerCase()) >
          -1 ||
        item.username.toLocaleLowerCase().indexOf(queryText.toLocaleLowerCase()) > -1
        ||
        item.employee_id.toLocaleLowerCase().indexOf(queryText.toLocaleLowerCase()) > -1
      );
    },

    selectMe () {
      this.SetUsersList(this.field.valuelist ? this.field.valuelist : []);
      this.users.push(this.$store.state.user.user_master);
      this.ComputedUsers = this.$store.state.user[this.itemvalue];
    },

    stringFormat(string, value) {
      return string.replace(/{}/g, String(value));
    }
  },
}
</script>

<style></style>
