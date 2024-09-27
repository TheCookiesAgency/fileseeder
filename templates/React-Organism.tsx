---
import {getHtmlSimpleCopy} from "@/shared/utils/get-html-render";

import type {TagTitle} from "@/shared/utils/get-html-render";


interface Props {
    _id: string;
    collection: CollectionName;
    headingLevel?: TagTitle
}

const {  _id, headingLevel, collection } = Astro.props;
const entry: Data<{ ${lowerCamelName}: ${NAME}}>  = await getEntry(collection, _id);
const data = entry.data.${lowerCamelName} as ${NAME}Entry;
const copy = getHtmlSimpleCopy(data.copy, headingLevel );

 ---

<section class={`o-${className}`}>
    <div class={`c-${className}`}>
        <h1>Hola! soy ${NAME},</h1>
        <div class={`${className}__copy`} set:html={copy}/>
        <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
</section>
