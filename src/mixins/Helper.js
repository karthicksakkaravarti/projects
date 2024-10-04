export const Helper = {
    methods: {
        formatDateToHumanReadable(date) {
            const d = new Date(date);
            const day = String(d.getDate()).padStart(2, '0');
            const monthIndex = d.getMonth();

            // Array of month names
            const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            const monthName = monthNames[monthIndex];
            const year = d.getFullYear();

            return `${day}/${monthName}/${year}`;
        },
        generate_component(Detail){
            if(Detail.type[0] == 'project'){
                if (Detail.status == '0' || Detail.status == 'BU Head Approval') {
                    return 'BUHeadApproval'
                }
                else if (Detail.status == '0' || Detail.status == 'Project Planning') {
                    return 'ProjectPlanning'
                }
                else if (Detail.status == '0' || Detail.status == 'ALM Setup') {
                    return 'ALMSetup'
                }
            }
            if(Detail.type[0] == 'timesheet'){
                return 'WorkLogDetails2'
            }
            return 'FormGenerator'
        },

        generate_route(Detail, type='project', mode='null') {
            console.log(type, mode)
            if (type == 'project') {
                // View Dashboard
                if (mode == 'view'){
                    this.$router.push({ name: 'Project Dashboard', params: { pid: Detail.id } })
                    return
                }

                if (Detail.status === 'DRAFT') {
                    localStorage.setItem('newProjectID', Detail.id)
                    this.$store.dispatch('OpenDrawerOnClick', {
                        ShowAppBarOnDrawer: true,
                        DrawerSize: '70%',
                        DrawerFormType: 'NewProject',
                        DrawerFormTitle: 'Update Project',
                        DrawerExtraParam: `&action=edit&id=${Detail.id}`,
                        DrawerFormAPICall: false,
                        DrawerMutation: 'mutation__drawer',
                        DrawerActionType: 'edit',
                        DrawerFormSubmit: {
                            btn_name: 'Update',
                            store_action_name: 'ProjectStore/PROJECT_API_PROJECT_POST',
                            custom_action: 'project_create',
                        },
                    })
                    return;
                }

                if (Detail.status == '0' || Detail.status == 'BU Head Approval') {
                    this.$router.push({ name: 'BU Head Approval', params: { pid: Detail.id } })
                } else if (Detail.status == 1 || Detail.status == 'Need Info') {
                    this.$store.dispatch('OpenDrawerOnClick', {
                        ShowAppBarOnDrawer: true,
                        DrawerSize: '50%',
                        DrawerFormType: 'NewProject',
                        DrawerFormTitle: 'Edit Project',
                        DrawerFormAPICall: true,
                        DrawerMutation: 'mutation__drawer',
                        DrawerActionType: 'edit',
                        DrawerExtraParam: '&pid=' + Detail.id,
                        DrawerFormSubmit: {
                        btn_name: 'Update Project',
                        store_action_name: 'ProjectStore/PROJECT_API_PROJECT_POST',
                        custom_action: Detail.id + '/project_update',
                        },
                    })
                } else if (Detail.status == 2 || Detail.status == 'Project Planning') {
                    this.$router.push({ name: 'Project Planning', params: { pid: Detail.id } })
                } else if (Detail.status == 6 || Detail.status == 'ALM Setup') {
                    this.$router.push({ name: 'ALM Setup', params: { pid: Detail.id } })
                } else if (Detail.status == 16 || Detail.status == 'ALM Verification') {
                    this.$router.push({ name: 'ALM Verification', params: { pid: Detail.id } })
                } else {
                    this.$router.push({ name: 'Project Dashboard', params: { pid: Detail.id } })
                }
            }
            if (type == 'users' || type == 'rm_users') {
                if (Detail.employee_id){
                    this.$router.push({ name: 'RM User View', params: { id: Detail.employee_id } })
                }
                if (Detail.resource_id){
                    this.$router.push({ name: 'RM User View', params: { id: Detail.resource_id } })
                }
            }

            if (type === 'time_sheet_approval') {
                this.$router.push({ name: 'Timesheet', query: {
                    view: 'Project',
                    range: `${Detail.start_date}_${Detail.end_date}`,
                    user: Detail.user.employee_id
                }});
            }
        },
        dependencystatusColor (status) {
            if (status == 'Planned') return 'orange'
            else if (status == 'Execution') return 'green'
            else if (status == 'Project Planning') return 'green'
            else if (status == 'Customer Support') return 'orange'
            else if (status == 'Delivered') return 'green'
            else if (status == 'Rejected') return 'red'
            else if (status == 'Closed') return 'green'
            else if (status == 'Completed') return 'green'
            else if (status == 'PLM Rejected') return 'red'
            else if (status == 'BU Head Rejected') return 'red'
            else if (status == 'Suspended') return 'red'
            else if (status == 'onTrack') return 'green'
            else if (status == 'OnTrack') return 'green'
            else if (status == 'AtRisk') return 'red'
            else if (status == 'Slipped') return 'red'
            else if (status == 'Blocked') return 'red'
            else return 'blue'
        },

        milestonestatuscolor(status){
            if (status == 'Planned') return 'orange'
            else if (status == 'Execution') return 'green'
            else if (status == 'Project Planning') return 'green'
            else if (status == 'Customer Support') return 'orange'
            else if (status == 'Delivered') return 'green'
            else if (status == 'Rejected') return 'red'
            else if (status == 'Closed') return 'green'
            else if (status == 'Completed') return 'green'
            else if (status == 'PLM Rejected') return 'red'
            else if (status == 'BU Head Rejected') return 'red'
            else if (status == 'Suspended') return 'red'
            else if (status == 'onTrack') return 'green'
            else if (status == 'OnTrack') return 'green'
            else if (status == 'AtRisk') return 'red'
            else if (status == 'Slipped') return 'red'
            else if (status == 'Blocked') return 'red'
            else return 'blue'
        },

        riskcolor(status){
            if (status == 'Planned') return 'orange'
            else if (status == 'Execution') return 'green'
            else if (status == 'Project Planning') return 'green'
            else if (status == 'Customer Support') return 'orange'
            else if (status == 'Delivered') return 'green'
            else if (status == 'Rejected') return 'red'
            else if (status == 'Closed') return 'green'
            else if (status == 'Completed') return 'green'
            else if (status == 'PLM Rejected') return 'red'
            else if (status == 'BU Head Rejected') return 'red'
            else if (status == 'Suspended') return 'red'
            else if (status == 'onTrack') return 'green'
            else if (status == 'OnTrack') return 'green'
            else if (status == 'AtRisk') return 'red'
            else if (status == 'Slipped') return 'red'
            else if (status == 'Blocked') return 'red'
            else if (status == 'Yet to Occurred') return 'orange'
            else if (status == 'No More Risk') return 'orange'
            else if (status == 'Occurred') return 'red'
            else if (status == 'Closed') return 'green'
            else return 'blue'
        },

        CRColor (status) {
            if (status == 'PLM Approval') return 'orange'
            // else if (status == 'Execution') return 'green'
            else if (status == 'BU Head Approval') return 'orange'
            else if (status == 'PLM Rejected') return 'red'
            else if (status == 'Resource Planning') return 'orange'
            else if (status == 'BU Head Rejected') return 'red'
            else if (status == 'Completed') return 'green'
            else if (status == 'Suspended') return 'red'
            else return 'blue'
        },

        generate_cr_route(item){
            this.$router.push({ name: 'CR Approval', params: { pid: item.project_details, crid : item.id } })
        },

        navigate_route(endpoint){
            this.$router.push(endpoint)
        }
    },

    filters: {
        capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        },

        currency_format: function (value) {
            if (typeof value !== 'number') {
                return value
            }
            var formatter = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'USD',
            })
            return formatter.format(value)
        },
    },
}
