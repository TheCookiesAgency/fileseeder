import {defineField, defineType} from 'sanity'

export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'object',
  fields: [
    defineField({
      name: 'content',
      title: 'Texto y fotos',
      type: 'copyAndMedia'
    }),
  ],
  preview: {
    select: {
      title: 'name',
    }
  }
})