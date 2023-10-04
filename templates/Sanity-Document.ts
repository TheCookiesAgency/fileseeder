import {defineField, defineType} from 'sanity';
import { landing } from "./base/landing";


export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'document',
  fields: [...landing],
  preview: {
    select: {
      title: 'name',
      subtitle: "language",
    }
  }
})