// Form Fields
import TextField from '@/components/TextField/TextField.vue'
import DateField from '@/components/DateTimeField/DateField.vue'
import TimePicker from '@/components/DateTimeField/TimePicker.vue'
import TextArea from '@/components/TextField/TextArea.vue'
import AutoComplete from '@/components/DropDown/AutoComplete.vue'
import Button from '@/components/Button/BaseButton.vue'
import Users from '@/components/AutoComplete/Users.vue'
import DateRange from '@/components/DateTimeField/DateRange.vue'
import CheckBox from '@/components/Checkbox/CheckBox.vue'
import Attachment from '@/components/FileUpload/Attachment.vue'
import WYSIWYG from '@/components/WYSIWYG/WYSIWYG.vue'
import ViewList from '@/components/DataTable/ViewList.vue'
import CustomView from '@/components/Menus/CustomView.vue'

import Section from '@/components/Helpers/Section.vue'
import Success from '@/components/Animation/Success.vue'
import Failed from '@/components/Animation/Failed.vue'

// Custom Form
// import TimeSheetSubmissionForm from '@/apps/timesheet/forms/TimeSheetSubmissionForm.vue'
// import EditTimesheet from '@/apps/timesheet/forms/EditTimesheet.vue'
// import SplitWorklogForm from '@/apps/timesheet/forms/SplitWorklogForm.vue'
// import LogTimeForm from '@/apps/timesheet/forms/LogTimeForm.vue'

// Components
// import WorkLogDetails from '@/apps/timesheet/components/WorkLogDetails.vue'
// import ResourceConfirmation from '@/apps/project/components/ResourceConfirmation.vue'

// Integration
// import FileList from '@/Integration/Microsoft/Sharepoint/Drive/FileList.vue'
// import Kudos from '@/Integration/Kudos/forms/Kudos.vue'
// import TalentPlus from '@/Integration/SkillsManagement/forms/TalentPlus.vue'
// import Myassets from '@/Integration/MyAsset/forms/Myassets.vue'
// import Helpcenter from '@/Integration/Helpcenter/forms/Helpcenter.vue'

// Service
// import EmailTemplate from '@/Services/EmailService/components/EmailTemplate.vue'

export const ModuleImport = {
  components: {
    TextField,
    DateField,
    TextArea,
    AutoComplete,
    Button,
    Users,
    TimePicker,
    DateRange,
    CheckBox,
    Attachment,
    WYSIWYG,
    ViewList,
    CustomView,

    Section,
    Success,
    Failed,

    // TimeSheetSubmissionForm,
    // EditTimesheet,
    // SplitWorklogForm,
    // LogTimeForm,

    // WorkLogDetails,
    // ResourceConfirmation,

    FileList,
    // Kudos,
    // TalentPlus,
    // Myassets,
    // Helpcenter,

    // EmailTemplate,
  },
}
