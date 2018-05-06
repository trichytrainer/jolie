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
    <v-btn color="info" @click="submit()">Submit</v-btn>
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
    },
    submit: function () {
      this.$http.post('http://localhost:5000/home', {code: this.userCode}).then(response => {
        console.log(response)
      }).catch(err => {
        console.log(err)
      }) 
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
  width: 100%;
}
</style>
