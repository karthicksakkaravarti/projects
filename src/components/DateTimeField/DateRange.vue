<template>
    <!-- TODO: Enable next and privous based on date selection -->
    <div>
        <v-btn-toggle>
            <v-btn x-small text dense  @click="selectPreviousPeriod" :disabled="readonly">
                <v-icon>mdi-arrow-left-drop-circle</v-icon>
            </v-btn>

            <v-menu max-width="750" v-model="menu" :disabled="readonly" :close-on-click="false"
                :close-on-content-click="false" offset-y>
                <template v-slot:activator="{ on, attrs }">

                    <v-btn outlined  small v-bind="attrs" v-on="on">
                        <v-icon>mdi-calendar</v-icon>
                        {{ formatDateToHumanReadable(dates[0]) }} - {{ formatDateToHumanReadable(dates[1]) }}
                    </v-btn>

                </template>
                <v-card>
                    <v-card-text>
                        <v-row class="ma-0 pa-0">
                            <v-col class="ma-0 pa-0">
                                <v-text-field dense outlined label="From Date" hide-details v-model="dateRange[0]"
                                    @input="handleDateInput" :readonly="readonly"></v-text-field>
                                <v-date-picker id="picker1" ref="picker1" v-model="dates" :events="events"
                                    :event-color="eventColor" :picker-date.sync="pickerPage1" multiple no-title full-width
                                    flat></v-date-picker>
                            </v-col>
                            <v-col class="ma-0 pa-0 ml-2">
                                <v-text-field dense outlined label="To Date" hide-details v-model="dateRange[1]"
                                    @input="handleDateInput" :readonly="readonly"></v-text-field>
                                <v-date-picker id="picker2" ref="picker2" v-model="dates" :events="events"
                                    :event-color="eventColor" :picker-date.sync="pickerPage2" multiple no-title
                                    full-width></v-date-picker>
                            </v-col>

                            <v-col class="ma-0 pa-0 ml-3">
                                <v-spacer class="mb-10"></v-spacer>
                                <v-list>
                                    <v-list-item-group v-model="quickFilter">
                                        <v-list-item value='today' @click="selectToday">
                                            <v-list-item-content>
                                                <v-list-item-title>Today</v-list-item-title>
                                            </v-list-item-content>
                                        </v-list-item>
                                        <v-list-item value="lastWeek" @click="selectLastWeek">
                                            <v-list-item-content>
                                                <v-list-item-title>Last Week</v-list-item-title>
                                            </v-list-item-content>
                                        </v-list-item>
                                        <v-list-item value='week' @click="selectWeek">
                                            <v-list-item-content>
                                                <v-list-item-title>Week</v-list-item-title>
                                            </v-list-item-content>
                                        </v-list-item>
                                        <v-list-item value="month" @click="selectMonth">
                                            <v-list-item-content>
                                                <v-list-item-title>Month</v-list-item-title>
                                            </v-list-item-content>
                                        </v-list-item>
                                        <v-list-item value="year" @click="selectYear">
                                            <v-list-item-content>
                                                <v-list-item-title>Year</v-list-item-title>
                                            </v-list-item-content>
                                        </v-list-item>
                                    </v-list-item-group>
                                </v-list>
                            </v-col>
                        </v-row>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn small outlined color="primary" @click="menu = false">Close</v-btn>
                        <v-btn small :outlined="!changes" color="success" @click="apply">Apply</v-btn>
                    </v-card-actions>
                </v-card>
            </v-menu>

            <v-btn small text @click="selectNextPeriod" :disabled="readonly">
                <v-icon>mdi-arrow-right-drop-circle</v-icon>
            </v-btn>


        </v-btn-toggle>


    </div>
</template>

<script>
import { Helper } from '@/mixins/Helper'

export default {
    data: () => ({
        startDate: '',
        endDate: '',

        menu: false,
        dark: false,
        vertical: false,
        events: [],
        eventColor: {},
        dateRange: [],
        dateRangePrevious: [],
        pickerPage1: null,
        pickerPage2: null,
        pickerPage1Adjusted: false,
        pickerPage2Adjusted: false,
        shadeAccent: true,
        changes: false,
        quickFilter: 'week'
    }),
    mixins: [Helper],
    props: {
        readonly: { default: false }
    },
    computed: {
        dates: {
            get() {
                if (!this.dateRange.length) {
                    this.dateRange = this.getDefaultDates()
                    this.render()
                }
                return this.dateRange
            },
            set(value) {
                if (value.length) {
                    if (value.length == 2) {
                        this.dateRange = value;
                    } else {
                        let difference = []
                        value.length == 1 ? difference = this.arrayDifference(this.dateRangePrevious, value) : difference = this.arrayDifference(value, this.dateRange)
                        if (difference.length) {
                            this.dateRange = difference
                        }
                    }
                }
                this.render()
                this.dateRangePrevious = this.dateRange
            }
        },
        valid: function () {
            return this.dates.length === 2
        }
    },
    methods: {
        handleDateInput() {
            if (this.validDate(this.dateRange[0]) && this.validDate(this.dateRange[1])) {
                this.setDateRange([this.dateRange[0], this.dateRange[1]]);
            }
        },
        validDate(dateString) {
            const date = new Date(dateString);
            return !isNaN(date.getTime());
        },
        selectLastWeek() {
            const today = new Date();
            const day = today.getDay();
            const lastWeekStart = new Date(today.getFullYear(), today.getMonth(), today.getDate() - day - 6);
            const lastWeekEnd = new Date(lastWeekStart.getFullYear(), lastWeekStart.getMonth(), lastWeekStart.getDate() + 6);

            this.dateRange = [this.formatDate(lastWeekStart), this.formatDate(lastWeekEnd)];
            this.render();
            this.bringDateIntoView();
        },
        // Select the next period based on the quickFilter.
        selectNextPeriod() {
            console.log(this.quickFilter)
            switch (this.quickFilter) {
                case 'today':
                    const nextDay = new Date(this.dateRange[1]);
                    nextDay.setDate(nextDay.getDate() + 1);
                    this.dateRange = [this.formatDate(nextDay), this.formatDate(nextDay)];
                    break;
                case 'week':
                    const nextWeekStart = new Date(this.dateRange[1]);
                    nextWeekStart.setDate(nextWeekStart.getDate() + 1);
                    const nextWeekEnd = new Date(nextWeekStart);
                    nextWeekEnd.setDate(nextWeekEnd.getDate() + 6);
                    this.dateRange = [this.formatDate(nextWeekStart), this.formatDate(nextWeekEnd)];
                    break;
                case 'month':
                    const nextMonthStart = new Date(this.dateRange[1]);
                    nextMonthStart.setDate(nextMonthStart.getDate() + 1);
                    const nextMonthEnd = new Date(nextMonthStart.getFullYear(), nextMonthStart.getMonth() + 1, 0);
                    this.dateRange = [this.formatDate(nextMonthStart), this.formatDate(nextMonthEnd)];
                    break;
                case 'year':
                    const nextYearStart = new Date(this.dateRange[1]);
                    nextYearStart.setDate(nextYearStart.getDate() + 1);
                    const nextYearEnd = new Date(nextYearStart.getFullYear() + 1, 11, 31);
                    this.dateRange = [this.formatDate(nextYearStart), this.formatDate(nextYearEnd)];
                    break;
            }
            this.render();
            this.bringDateIntoView();
            this.$emit("dates", this.dateRange)
        },

        // Select the previous period based on the quickFilter.
        selectPreviousPeriod() {
            console.log(this.quickFilter)
            switch (this.quickFilter) {
                case 'today':
                    const previousDay = new Date(this.dateRange[0]);
                    previousDay.setDate(previousDay.getDate() - 1);
                    this.dateRange = [this.formatDate(previousDay), this.formatDate(previousDay)];
                    break;
                case 'week':
                    const previousWeekStart = new Date(this.dateRange[0]);
                    previousWeekStart.setDate(previousWeekStart.getDate() - 7);
                    const previousWeekEnd = new Date(previousWeekStart);
                    previousWeekEnd.setDate(previousWeekEnd.getDate() + 6);
                    this.dateRange = [this.formatDate(previousWeekStart), this.formatDate(previousWeekEnd)];
                    break;
                case 'month':
                    const previousMonthEnd = new Date(this.dateRange[0]);
                    previousMonthEnd.setDate(previousMonthEnd.getDate() - 1);
                    const previousMonthStart = new Date(previousMonthEnd.getFullYear(), previousMonthEnd.getMonth(), 1);
                    this.dateRange = [this.formatDate(previousMonthStart), this.formatDate(previousMonthEnd)];
                    break;
                case 'year':
                    const previousYearEnd = new Date(this.dateRange[0]);
                    previousYearEnd.setDate(previousYearEnd.getDate() - 1);
                    const previousYearStart = new Date(previousYearEnd.getFullYear(), 0, 1);
                    this.dateRange = [this.formatDate(previousYearStart), this.formatDate(previousYearEnd)];
                    break;
            }
            this.render();
            this.bringDateIntoView();
            this.$emit("dates", this.dateRange)
        },
        // Day Fitler
        selectToday() {
            const today = new Date();
            const formattedToday = this.formatDate(today);
            this.dateRange = [formattedToday, formattedToday];
            this.render();
            this.bringDateIntoView();
        },
        selectWeek() {
            const today = new Date();
            const day = today.getDay(); // Get the current day of week (0-6). 0 is Sunday.

            let weekStart;
            if (day === 0) { // If today is Sunday
                weekStart = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 6);
            } else if (day === 6) { // If today is Saturday
                weekStart = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 5);
            } else { // If today is a weekday
                weekStart = new Date(today.getFullYear(), today.getMonth(), today.getDate() - day + 1);
            }
            const weekEnd = new Date(weekStart.getFullYear(), weekStart.getMonth(), weekStart.getDate() + 6);

            this.dateRange = [this.formatDate(weekStart), this.formatDate(weekEnd)];
            this.render();
            this.bringDateIntoView();
        },
        selectMonth() {
            const today = new Date();
            const monthStart = new Date(today.getFullYear(), today.getMonth(), 1);
            const monthEnd = new Date(today.getFullYear(), today.getMonth() + 1, 0);
            this.dateRange = [this.formatDate(monthStart), this.formatDate(monthEnd)];
            this.render();
            this.bringDateIntoView();
        },
        selectYear() {
            const today = new Date();
            const yearStart = new Date(today.getFullYear(), 0, 1);
            const yearEnd = new Date(today.getFullYear(), 11, 31);
            this.dateRange = [this.formatDate(yearStart), this.formatDate(yearEnd)];
            this.render();
            this.bringDateIntoView();
        },
        apply() {
            if (this.dateRange.length === 1) {
                this.dateRange = [...this.dateRange, ...this.dateRange];
            }
            this.$emit("dates", this.dateRange)
            this.menu = false
        },
        render() {
            this.events = this.getDateRange(this.dates)
            this.eventColor = this.buildEventColors(this.events)
        },
        addDaysToDate(date, days) {
            var d = new Date(date)
            d.setDate(d.getDate() + days)
            return d
        },
        formatDate(date) {
            return date.toISOString().split('T')[0]
        },
        buildEventColors(range) {
            let colors = {}
            for (let i = 0; i < range.length; i++) {
                let accentShade = ''
                this.shadeAccent ? (this.dark ? accentShade = 'darken-2' : accentShade = 'lighten-2') : accentShade = ''
                colors[range[i]] = 'red ' + accentShade + ' v-date-picker-table__event'
                if (i === 0) {
                    colors[range[i]] += ' v-date-picker-table__event--start'
                }
                if (i === range.length - 1) {
                    colors[range[i]] += ' v-date-picker-table__event--end'
                }
            }
            return colors
        },
        getDateRange(dates) {
            let date1 = new Date(dates[0])
            let date2 = new Date(dates[dates.length - 1])
            let cur = new Date(Math.min(date1, date2)), range = []
            while (cur <= Math.max(date1, date2)) {
                range.push(this.formatDate(new Date(cur)))
                cur.setDate(cur.getDate() + 1)
            }
            return range;
        },
        getDefaultDates() {
            const currentDate = new Date();
            const year = currentDate.getFullYear();
            const month = currentDate.getMonth();
            const firstDay = new Date(year, month, 2).toISOString().substr(0, 10);
            const lastDay = new Date(year, month + 1, 1).toISOString().substr(0, 10);
            if (!this.quickFilter) {
                this.$emit("dates", [firstDay, lastDay])
            }

            return [
                firstDay, lastDay
            ]
        },
        setDefaultDates() {
            this.dateRange = this.getDefaultDates()
            this.render()
            this.bringDateIntoView()
        },
        clearDates() {
            this.dateRange = []
        },
        arrayDifference(array1, array2) {
            return array1.filter(function (i) {
                return array2.indexOf(i) < 0
            })
        },
        parsePickerPage(date) {
            let dateParts = date.split('-')
            return {
                year: parseInt(dateParts[0]),
                month: parseInt(dateParts[1])
            }
        },
        increasePickerPage(pickerPage) {
            pickerPage.month == 12 ? (pickerPage.year++, pickerPage.month = 1) : pickerPage.month++
            return pickerPage
        },
        decreasePickerPage(pickerPage) {
            pickerPage.month == 1 ? (pickerPage.year--, pickerPage.month = 12) : pickerPage.month--
            return pickerPage
        },
        pickerPageToString(pickerPage) {
            pickerPage.month < 10 ? pickerPage.month = '0' + pickerPage.month.toString() : pickerPage.month = pickerPage.month.toString()
            return pickerPage.year.toString() + '-' + pickerPage.month
        },
        bringDateIntoView() {
            if (this.dateRange.length > 0) {
                this.pickerPage1 = this.pickerPageToString(this.parsePickerPage(this.dateRange[0]))
            }
            this.changes = true
        },

        setDateRange(value) {
            this.dateRange = value
            this.render()
            this.bringDateIntoView()
        }
    },
    mounted() {
        if (this.quickFilter == 'week') {
            this.selectWeek()
            this.apply()
        }
    },
    watch: {
        startDate(value) {
            if (this.validDate(value)) {
                this.dateRange[0] = value;
            }
        },
        endDate(value) {
            if (this.validDate(value)) {
                this.dateRange[1] = value;
            }
        },
        dark(value) {
            this.render()
        },
        shadeAccent(value) {
            this.render()
        },
        pickerPage1(value) {
            if (!this.pickerPage1Adjusted) {
                this.pickerPage2Adjusted = true
                this.pickerPage2 = this.pickerPageToString(this.increasePickerPage(this.parsePickerPage(value)))
            }
            this.pickerPage1Adjusted = false
        },
        pickerPage2(value) {
            if (!this.pickerPage2Adjusted) {
                this.pickerPage1Adjusted = true
                this.pickerPage1 = this.pickerPageToString(this.decreasePickerPage(this.parsePickerPage(value)))
            }
            this.pickerPage2Adjusted = false
        }
    }
}
</script>

<style scoped >
#picker1.v-picker .v-date-picker-header .v-btn:last-of-type,
#picker2.v-picker .v-date-picker-header .v-btn:first-of-type {
    display: none;
}

.v-picker.v-card {
    box-shadow: none;
}

.v-date-picker-table--date table {
    border-collapse: separate;
    border-spacing: 0px 8px;
}

.v-date-picker-table--date table td {
    /*   border: 1px solid blue; */
}

.v-date-picker-table__event {
    z-index: -1;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    border-radius: 0;
    transform: none;
}

.v-date-picker-table__event--start {
    margin-left: 50%
}

.v-date-picker-table__event--end {
    margin-right: 50%;
    width: auto;
}
</style>
