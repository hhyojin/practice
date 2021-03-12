<template>
        <div id="app">
          <TodoHeader></TodoHeader>
          <TodoInput v-on:addTodo_event="addTodo_method"></TodoInput>
          <TodoList v-bind:propsdata2="todoItems" @removeTodo_event="removeTodo"></TodoList>
          <TodoFooter v-on:removeAll_event="clearAll"></TodoFooter>
        </div>
</template>

<script>
  import TodoHeader from './components/TodoHeader.vue'
  import TodoInput from './components/TodoInput.vue'
  import TodoList from './components/TodoList.vue'
  import TodoFooter from './components/TodoFooter.vue'

    export default {
      data(){
        return{
          todoItems: []
        }
      },
      methods: {
        addTodo_method(todoItem){
          localStorage.setItem(todoItem, todoItem);
          this.todoItems.push(todoItem);
        },
        clearAll(){
          localStorage.clear();
          this.todoItems =[];
        },
        removeTodo(todoItem, index){
          localStorage.removeItem(todoItem);
          this.todoItems.splice(index,1);
        }
      },
      components: {
        'TodoHeader': TodoHeader,
        'TodoInput': TodoInput,
        'TodoList': TodoList,
        'TodoFooter': TodoFooter
      },
      created() {
        if(localStorage.length > 0){
          for(var i =0 ; i<localStorage.length; i++){
              this.todoItems.push(localStorage.key(i));
          }
        }
      }
                
    }
</script>

<style>

    body{
      text-align: center;
      background-color: #f6f6f8;
    }

    input{
      border-style: groove;
      width: 200px;
            }

    button{
      border-style: groove;
    }

    .shadow{
      box-shadow: 5px 10px 10px rgba(0,0,0,0.03)
    }

</style>