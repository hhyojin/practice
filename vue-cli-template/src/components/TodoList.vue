<template>
        <section>
            <transition-group name="list" tag="ul">
                <li v-for="(todoItem, index) in propsdata2" :key="todoItem" class="shadow">
                    <i class="checkBtn fas fa-check" aria-hidden="true"></i>
                    {{ todoItem }}
                    <span class="removeBtn" type="button" @click="removeTodo(todoItem, index)">
                        <i class="far fa-trash-alt" aria-hidden="true"></i>
                    </span>
                </li>
            </transition-group>
        </section>
</template>

<script>
        export default {
            props: ['propsdata2'],
            methods: {
                removeTodo(todoItem, index){
                   this.$emit('removeTodo_event', todoItem, index);
                }
            }
        }
</script>

<style>
    ul {
        list-style-type: none;
        padding-left: 0;
        margin-top: 0;
        text-align: left;
    }

    li {
        display: flex;
        min-height: 50px;
        height: 50px;
        line-height: 50px;
        margin: 0.5rem 0;
        padding: 0 0.9rem;
        background: white;
        border-radius: 5px;
    }

    .checkBtn{
        line-height: 45px;
        color: #62acde;
        margin-right: 5px;
    }

    .removeBtn{
        margin-left: auto;
        color: #de4343;
    }
</style>

<style scoped>
    .list-enter-active, .list-leave-active {
            transition: all 1s;
        }

    .list-enter, .list-leave-to {
        opacity: 0;
        transform: translateY(30px);
    }
</style>