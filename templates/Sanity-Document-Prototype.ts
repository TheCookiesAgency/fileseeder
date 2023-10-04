import {defineField, defineType} from 'sanity';
import { prototype } from "./base/prototype";


export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'document',
  fields: [...prototype],
  preview: {
    select: {
      title: 'name',
      subtitle: "language",
    }
  }
})