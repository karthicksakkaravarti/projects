(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0c45ea"],{"3b16":function(t,e,r){"use strict";r.r(e);var o=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("view-list",{attrs:{options:{store_action_name:"ProjectStore/GET_PROJECTS",filter_table:"projects"},type:"project"},scopedSlots:t._u([{key:"top-right",fn:function(){return[r("Button",{staticClass:"mt-0",attrs:{outlined:!0,rounded:!0,mdi_icon:"mdi-plus",click:"OpenDrawerOnClick",title:"Create Project",tooltip:"Create Project",options:{ShowAppBarOnDrawer:!0,DrawerSize:"30%",DrawerFormType:"projects",DrawerFormTitle:"Create Project",DrawerAddons:"/addons/apps/project/api/projects",DrawerFormAPICall:!0,DrawerFilterForm:!1,DrawerMutation:"mutation__drawer",DrawerActionType:"new",DrawerFormSubmit:{btn_name:"Create Project",store_action_name:"ProjectStore/CREATE_PROJECT",custom_action:"",data:""}}}})]},proxy:!0},{key:"item-name",fn:function(e){var o=e.item;return[r("span",[t._v(t._s(o.name))])]}},{key:"item-status",fn:function(e){var o=e.item;return[r("span",[r("v-chip",{attrs:{small:""}},[t._v(t._s(o.status))])],1)]}},{key:"item-description",fn:function(e){var o=e.item;return[r("span",{domProps:{innerHTML:t._s(o.description)}})]}}])})},n=[],a=r("5530"),c=r("2f62"),i=r("88fa"),s=r("56d7"),u={mixins:[i["a"]],name:"ProjectList",data:function(){return{}},computed:Object(a["a"])(Object(a["a"])({},Object(c["c"])("ProjectStore",["allProjects"])),{},{projects:function(){return this.allProjects}}),created:function(){var t=this;this.GET_PROJECTS(),s["bus"].$on("form_success",(function(e,r){var o=arguments.length>2&&void 0!==arguments[2]?arguments[2]:null;console.log(e,r,o),t.$store.dispatch("CloseDrawer"),t.GET_PROJECTS()}))},methods:Object(a["a"])(Object(a["a"])({},Object(c["b"])("ProjectStore",["GET_PROJECTS"])),{},{viewProject:function(t){alert("View details for project ID: ".concat(t))}})},p=u,l=r("2877"),m=r("6544"),d=r.n(m),j=r("cc20"),w=Object(l["a"])(p,o,n,!1,null,null,null);e["default"]=w.exports;d()(w,{VChip:j["a"]})}}]);
//# sourceMappingURL=chunk-2d0c45ea.315fd56b.js.map