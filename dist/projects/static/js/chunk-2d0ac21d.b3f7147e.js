(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0ac21d"],{"17de":function(t,e,s){"use strict";s.r(e);var n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-app",[s("TodoList")],1)},a=[],r=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-container",{staticStyle:{"max-width":"500px"}},[s("v-text-field",{attrs:{label:"What are you working on?",solo:""},on:{keydown:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.create.apply(null,arguments)}},scopedSlots:t._u([{key:"append",fn:function(){return[s("v-fade-transition",[t.newTask?s("v-icon",{on:{click:t.create}},[t._v(" mdi-plus-circle ")]):t._e()],1)]},proxy:!0}]),model:{value:t.newTask,callback:function(e){t.newTask=e},expression:"newTask"}}),s("h2",{staticClass:"text-h4 success--text pl-4"},[t._v(" Tasks:  "),s("v-fade-transition",{attrs:{"leave-absolute":""}},[s("span",{key:"tasks-"+t.tasks.length},[t._v(" "+t._s(t.tasks.length)+" ")])])],1),s("v-divider",{staticClass:"mt-4"}),s("v-row",{staticClass:"my-1",attrs:{align:"center"}},[s("strong",{staticClass:"mx-4 info--text text--darken-2"},[t._v(" Remaining: "+t._s(t.remainingTasks)+" ")]),s("v-divider",{attrs:{vertical:""}}),s("strong",{staticClass:"mx-4 success--text text--darken-2"},[t._v(" Completed: "+t._s(t.completedTasks)+" ")]),s("v-spacer"),s("v-progress-circular",{staticClass:"mr-2",attrs:{value:t.progress}})],1),s("v-divider",{staticClass:"mb-4"}),t.tasks.length>0?s("v-card",[s("v-slide-y-transition",{staticClass:"py-0",attrs:{group:"",tag:"v-list"}},[t._l(t.tasks,(function(e,n){return[0!==n?s("v-divider",{key:n+"-divider"}):t._e(),s("v-list-item",{key:n+"-"+e.text},[s("v-list-item-action",[s("v-checkbox",{attrs:{color:e.done?"grey":"primary"},scopedSlots:t._u([{key:"label",fn:function(){return[s("div",{staticClass:"ml-4",class:e.done?"grey--text":"primary--text",domProps:{textContent:t._s(e.title)}})]},proxy:!0}],null,!0),model:{value:e.done,callback:function(s){t.$set(e,"done",s)},expression:"task.done"}})],1),s("v-spacer"),s("v-scroll-x-transition",[e.done?s("v-icon",{attrs:{color:"success"}},[t._v(" mdi-check ")]):t._e()],1),s("v-icon",{staticClass:"ml-2",attrs:{color:"error"},on:{click:function(s){return t.deleteTask(e)}}},[t._v(" mdi-delete ")])],1)]}))],2)],1):t._e()],1)},i=[],o=(s("4de4"),s("d3b7"),s("4360")),c={data:function(){return{tasks:[],newTask:null}},computed:{completedTasks:function(){return this.tasks.filter((function(t){return t.done})).length},progress:function(){return this.completedTasks/this.tasks.length*100},remainingTasks:function(){return this.tasks.length-this.completedTasks}},created:function(){this.fetchTasks()},methods:{fetchTasks:function(){var t=this;o["a"].dispatch("TodoStore/GET_TODO").then((function(e){t.tasks=e.data.results})).catch((function(t){console.error(t)}))},create:function(){var t=this;o["a"].dispatch("TodoStore/POST_TODO",{title:this.newTask,completed:!1}).then((function(e){t.tasks.push(e.data),t.newTask=null})).catch((function(t){console.error(t)}))},deleteTask:function(t){var e=this;o["a"].dispatch("TodoStore/DELETE_TODO",t.id).then((function(){e.tasks=e.tasks.filter((function(e){return e.id!==t.id}))})).catch((function(t){console.error(t)}))}}},l=c,d=s("2877"),u=s("6544"),k=s.n(u),p=s("b0af"),v=s("ac7c"),f=s("a523"),h=s("ce7e"),m=s("0789"),T=s("132d"),x=s("da13"),_=s("1800"),g=s("490a"),y=s("0fd9"),w=s("2fa4"),C=s("8654"),V=Object(d["a"])(l,r,i,!1,null,null,null),b=V.exports;k()(V,{VCard:p["a"],VCheckbox:v["a"],VContainer:f["a"],VDivider:h["a"],VFadeTransition:m["d"],VIcon:T["a"],VListItem:x["a"],VListItemAction:_["a"],VProgressCircular:g["a"],VRow:y["a"],VScrollXTransition:m["e"],VSlideYTransition:m["g"],VSpacer:w["a"],VTextField:C["a"]});var O={components:{TodoList:b}},S=O,E=s("7496"),D=Object(d["a"])(S,n,a,!1,null,null,null);e["default"]=D.exports;k()(D,{VApp:E["a"]})}}]);
//# sourceMappingURL=chunk-2d0ac21d.b3f7147e.js.map