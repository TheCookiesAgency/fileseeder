---
import {sanityClient} from "sanity:client";
import type { ${NAME} } from "@/shared/sanity/sanity.types";


const {  id} = Astro.props;
// change firsLetter to lowercase in query
const data = await sanityClient.fetch<{ ${NAME} }>(
    `*[_id == "${id}" ][0]{ ...${NAME}}`,
);

 ---
<section class={`o-${className}`}>
  <div class={`c-${className}`}>
      <h1>Hola! soy ${NAME},</h1>
      <pre>{JSON.stringify(data,  null, 2)}</pre>
  </div>
</section>
