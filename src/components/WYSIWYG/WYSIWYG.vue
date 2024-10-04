<template>
  <div>
    <div id="editor">
    </div>
  </div>
</template>

<script>
export default {
  props: {
    field: { default: {} }
  },
  name: "CKEditorComponent",
  mounted() {
    let script = document.createElement("script");
    script.onload = () => this.initEditor();
    script.src = "https://cdn.ckeditor.com/ckeditor5/38.0.1/super-build/ckeditor.js";
    document.head.appendChild(script);
  },
  methods: {
    initEditor() {
      CKEDITOR.ClassicEditor
        .create(document.querySelector("#editor"),
          {
            toolbar: {
              // Your toolbar configuration here
              // ...
              items: [
                // 'exportPDF', 'exportWord', '|',
                // 'findAndReplace', 'selectAll', '|',
                'heading', '|',
                'bold', 'italic', 'strikethrough', 'underline', 'code', 'subscript', 'superscript', 'removeFormat', '|',
                'bulletedList', 'numberedList', 'todoList', '|',
                'outdent', 'indent', '|',
                'undo', 'redo',
                '-',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'highlight', '|',
                'alignment', '|',
                'link', 'blockQuote', 'insertTable',
                // 'mediaEmbed', 'codeBlock', 'htmlEmbed', 'insertImage',
                '|',
                // 'specialCharacters', 'horizontalLine', 'pageBreak', '|',
                // 'textPartLanguage', '|',
                // 'sourceEditing'
              ],

              shouldNotGroupWhenFull: true
            },
            removePlugins: [
              'CKBox',
              'CKFinder',
              'EasyImage',
              // This sample uses the Base64UploadAdapter to handle image uploads as it requires no configuration.
              // https://ckeditor.com/docs/ckeditor5/latest/features/images/image-upload/base64-upload-adapter.html
              // Storing images as Base64 is usually a very bad idea.
              // Replace it on production website with other solutions:
              // https://ckeditor.com/docs/ckeditor5/latest/features/images/image-upload/image-upload.html
              // 'Base64UploadAdapter',
              'RealTimeCollaborativeComments',
              'RealTimeCollaborativeTrackChanges',
              'RealTimeCollaborativeRevisionHistory',
              'PresenceList',
              'Comments',
              'TrackChanges',
              'TrackChangesData',
              'RevisionHistory',
              'Pagination',
              'WProofreader',
              // Careful, with the Mathtype plugin CKEditor will not load when loading this sample
              // from a local file system (file://) - load this site via HTTP server if you enable MathType.
              'MathType',
              // The following features are part of the Productivity Pack and require additional license.
              'SlashCommand',
              'Template',
              'DocumentOutline',
              'FormatPainter',
              'TableOfContents'
            ],
          })
        .then(editor => {
          // Initialize the editor with the current value
          editor.setData(this.field.value);

          // Listen to changes in the editor and update the field value
          editor.model.document.on('change:data', () => {
              this.field.value = editor.getData();
            });

        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>





<!-- <template>
    <div>
      <b>{{ field }}</b>
      <textarea id="editor">
      </textarea>
    </div>
  </template>
  
  <script>
  import { onMounted, ref, watch } from 'vue';
  
  export default {
    name: "CKEditorComponent",
    props: {
      field: { default: {} }
    },
    data() {
      return {
        editorInstance: null,
        editorConfig: {
          updateSourceElementOnDestroy: true,
          toolbar: {
            // Your toolbar configuration here
            // ...
            items: [
              'exportPDF', 'exportWord', '|',
              'findAndReplace', 'selectAll', '|',
              'heading', '|',
              'bold', 'italic', 'strikethrough', 'underline', 'code', 'subscript', 'superscript', 'removeFormat', '|',
              'bulletedList', 'numberedList', 'todoList', '|',
              'outdent', 'indent', '|',
              'undo', 'redo',
              '-',
              'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'highlight', '|',
              'alignment', '|',
              'link', 'insertImage', 'blockQuote', 'insertTable', 'mediaEmbed', 'codeBlock', 'htmlEmbed', '|',
              'specialCharacters', 'horizontalLine', 'pageBreak', '|',
              'textPartLanguage', '|',
              'sourceEditing'
            ],
            shouldNotGroupWhenFull: true
          },
          list: {
            // Your list configuration here
            // ...
            properties: {
              styles: true,
              startIndex: true,
              reversed: true
            }
          },
          heading: {
            // Your heading configuration here
            // ...
            options: [
              { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
              { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
              { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
              { model: 'heading3', view: 'h3', title: 'Heading 3', class: 'ck-heading_heading3' },
              { model: 'heading4', view: 'h4', title: 'Heading 4', class: 'ck-heading_heading4' },
              { model: 'heading5', view: 'h5', title: 'Heading 5', class: 'ck-heading_heading5' },
              { model: 'heading6', view: 'h6', title: 'Heading 6', class: 'ck-heading_heading6' }
            ]
          },
          placeholder: 'Add Text Here!',
          fontFamily: {
            // Your fontFamily configuration here
            // ...
            options: [
              { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
              { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
              { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
              { model: 'heading3', view: 'h3', title: 'Heading 3', class: 'ck-heading_heading3' },
              { model: 'heading4', view: 'h4', title: 'Heading 4', class: 'ck-heading_heading4' },
              { model: 'heading5', view: 'h5', title: 'Heading 5', class: 'ck-heading_heading5' },
              { model: 'heading6', view: 'h6', title: 'Heading 6', class: 'ck-heading_heading6' }
            ]
          },
          fontSize: {
            // Your fontSize configuration here
            // ...
            options: [10, 12, 14, 'default', 18, 20, 22],
            supportAllValues: true
  
          },
          htmlSupport: {
            // Your htmlSupport configuration here
            // ...
            allow: [
              {
                name: /.*/,
                attributes: true,
                classes: true,
                styles: true
              }
            ]
          },
          htmlEmbed: {
            // Your htmlEmbed configuration here
            // ...
            showPreviews: true
  
          },
          link: {
            // Your link configuration here
            // ...
            decorators: {
              addTargetToExternalLinks: true,
              defaultProtocol: 'https://',
              toggleDownloadable: {
                mode: 'manual',
                label: 'Downloadable',
                attributes: {
                  download: 'file'
                }
              }
            }
          },
          mention: {
            // Your mention configuration here
            // ...
            feeds: [
              {
                marker: '@',
                feed: [
                  '@system_check'
                ],
                minimumCharacters: 1
              }
            ]
          },
          removePlugins: [
            // Your removePlugins configuration here
            // ...
            // These two are commercial, but you can try them out without registering to a trial.
            // 'ExportPdf',
            // 'ExportWord',
            'CKBox',
            'CKFinder',
            'EasyImage',
            // This sample uses the Base64UploadAdapter to handle image uploads as it requires no configuration.
            // https://ckeditor.com/docs/ckeditor5/latest/features/images/image-upload/base64-upload-adapter.html
            // Storing images as Base64 is usually a very bad idea.
            // Replace it on production website with other solutions:
            // https://ckeditor.com/docs/ckeditor5/latest/features/images/image-upload/image-upload.html
            // 'Base64UploadAdapter',
            'RealTimeCollaborativeComments',
            'RealTimeCollaborativeTrackChanges',
            'RealTimeCollaborativeRevisionHistory',
            'PresenceList',
            'Comments',
            'TrackChanges',
            'TrackChangesData',
            'RevisionHistory',
            'Pagination',
            'WProofreader',
            // Careful, with the Mathtype plugin CKEditor will not load when loading this sample
            // from a local file system (file://) - load this site via HTTP server if you enable MathType.
            'MathType',
            // The following features are part of the Productivity Pack and require additional license.
            'SlashCommand',
            'Template',
            'DocumentOutline',
            'FormatPainter',
            'TableOfContents'
          ],
        }
      };
    },
    mounted() {
      let script = document.createElement("script");
      script.onload = () => this.initEditor();
      script.src = "https://cdn.ckeditor.com/ckeditor5/38.0.1/super-build/ckeditor.js";
      document.head.appendChild(script);
    },
    beforeDestroy() {
      if (this.editorInstance) {
        this.editorInstance.destroy();
      }
    },
    methods: {
      async setEditorData(htmlContent) {
        await this.editorInstance.ready;
        console.log(htmlContent)
        this.editorInstance.setData('<p>adasdasd</p>');
      },
      async getEditorData() {
        await this.editorInstance.ready;
        let htmlContent = this.editorInstance.getData();
        console.log(htmlContent);  // or do whatever you want with the HTML content
      },
      initEditor() {
        CKEDITOR.ClassicEditor
          .create(document.querySelector("#editor"), this.editorConfig)
          .then(editor => {
            this.editorInstance = editor;
            // Initialize the editor with the current value
            const htmlString = `
      hrllow
  `;
            const parser = new DOMParser();
            const html = parser.parseFromString(htmlString, 'text/html');
            const body = html.body;
            console.log(body)
            editor.setData(`<b>adsas</b>`);
  
            // Listen to changes in the editor and update the field value
            editor.model.document.on('change:data', () => {
              this.field.value = editor.getData();
            });
            // editor.setData('<div>adasd</div>');
          })
          .catch(error => {
            console.error(error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  #container {
    width: 1000px;
    margin: 20px auto;
  }
  
  .ck-editor__editable[role="textbox"] {
    /* editing area */
    min-height: 200px;
  }
  
  .ck-content .image {
    /* block images */
    max-width: 80%;
    margin: 20px auto;
  }
  </style>
   -->