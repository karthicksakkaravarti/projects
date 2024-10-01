export function status_color(status_code) {
  if (status_code == '400' || status_code == '409') {
    return 'error'
  }
  return 'success'
}

export function exception_rest_api_handler(message) {
  if (typeof message == 'object') {
    var str = ''
    for (var p in message) {
      if (Object.prototype.hasOwnProperty.call(message, p)) {
        str += message[p] + '\n'
      }
    }
    return str
  }
  return message
}

export function extract_api_data(value) {
  let formData = new FormData()
  for (var data of value) {
    if (data.dbfield && (data.value || data.value == false)) {
      // formData[data.dbfield] = data.value
      if (String(typeof data.value) != 'object') {
        formData.append(data.dbfield, data.value)
      } else {
        try {
          for (var object of data.value) {
            formData.append('attachments', object)
          }
        } catch (err) {
          for (const [key, value] of Object.entries(data.value)) {
            // console.log(`${key}: ${value}`);
            formData.append(key, value)
          }

          console.error(err)
        }
      }
    }
  }
  return formData
}
