(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0a36fa"],{"01be":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-card",{attrs:{elevation:"0"}},[a("v-card-text",[a("v-row",[a("v-col",{attrs:{cols:"12",sm:"2"}},[a("b",[t._v("CATEGORIES")]),a("v-list",[a("v-divider"),a("v-list",{attrs:{nav:"",dense:""}},[a("v-list-item-group",{attrs:{color:"primary"},model:{value:t.selectedItem,callback:function(e){t.selectedItem=e},expression:"selectedItem"}},t._l(t.items,(function(e,n){return a("v-list-item",{key:n},[a("v-list-item-content",[a("v-list-item-title",[t._v(t._s(e.text))])],1)],1)})),1)],1)],1)],1),a("v-col",{attrs:{cols:"12",sm:"10"}},[a("view-list",{attrs:{options:{store_action_name:"GET_ADDONS",filter_table:"appsInstaller"},type:"appsInstaller"},scopedSlots:t._u([{key:"item-is_installed",fn:function(e){var n=e.item;return[a("v-chip",{attrs:{"x-small":""}},[t._v(" "+t._s(n.is_installed?"Installed":"Not Installed")+" ")])]}},{key:"item-app_name",fn:function(e){var n=e.item;return[a("span",{staticClass:"text-capitalize"},[a("v-avatar",{staticClass:"white--text",attrs:{color:"primary",size:"30"}},[t._v(t._s(n.app_name[0]))]),t._v(" "+t._s(n.app_name)+" ")],1)]}},{key:"item-actions",fn:function(e){var n=e.item;return[n.is_installed?t._e():a("v-btn",{attrs:{"x-small":"",color:"primary"},on:{click:function(e){return t.installAddons(n.app_name)}}},[t._v(" Install ")])]}}])})],1)],1)],1)],1)},s=[],i=a("88fa"),l=a("4360"),r={mixins:[i["a"]],setup:function(){var t=[{text:"ALL"},{text:"Sales"},{text:"Services"},{text:"Accounting"},{text:"Inventory"},{text:"Manufacturing"},{text:"Website"},{text:"Marketing"},{text:"Human Resources"},{text:"Productive"},{text:"Administration"}],e=0,a="";function n(t){l["a"].dispatch("POST_ADDONS",{query:"install/",body:{app_name:t}}).then((function(t){window.location.reload()}))}return{items:t,selectedItem:e,search:a,installAddons:n}}},o=r,c=a("2877"),d=a("6544"),m=a.n(d),v=a("8212"),u=a("8336"),p=a("b0af"),_=a("99d9"),f=a("cc20"),x=a("62ad"),I=a("ce7e"),b=a("8860"),V=a("da13"),w=a("5d23"),y=a("1baa"),k=a("0fd9"),h=Object(c["a"])(o,n,s,!1,null,null,null);e["default"]=h.exports;m()(h,{VAvatar:v["a"],VBtn:u["a"],VCard:p["a"],VCardText:_["b"],VChip:f["a"],VCol:x["a"],VDivider:I["a"],VList:b["a"],VListItem:V["a"],VListItemContent:w["a"],VListItemGroup:y["a"],VListItemTitle:w["c"],VRow:k["a"]})}}]);
//# sourceMappingURL=chunk-2d0a36fa.96c8bbbb.js.map