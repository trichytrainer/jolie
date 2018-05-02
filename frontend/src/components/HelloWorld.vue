<template>
  <div class="hello">
    <div class="editor" id="editor">
      <monaco-editor
        height="600"
        :language="language"
        :code="initialCode"
        :editorOptions="options"
        @mounted="onMounted"
        @codeChange="onCodeChange"
      >
      </monaco-editor>
    </div>
  </div>
</template>

<script>
import * as monaco from 'monaco-editor'
import MonacoEditor from 'vue-monaco-editor'

export default {
  name: 'HelloWorld',
  components: {
    MonacoEditor
  },
  props: {
    msg: String
  },
  data: function () {
    return {
      language: 'python',
      options: {},
      initialCode: 'def your_code():\n\treturn',
      userCode: null
    }
  },
  methods: {
    onMounted: function () {
    },
    onCodeChange: function (editor) {
      this.userCode = editor.getValue()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.editor {
  text-align: left;
}
</style>
