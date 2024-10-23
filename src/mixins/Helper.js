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
                this.$router.push({ name: 'Project Dashboard', params: { pid: Detail.id } })

            }
            if (type == 'repositories') {
                // View Dashboard
                this.$router.push({ name: 'repository-files', params: { pid: Detail.id } })

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
