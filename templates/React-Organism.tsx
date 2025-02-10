---
import {getHtmlSimpleCopy} from "@/shared/utils/get-html-render";

import type {TagTitle} from "@/shared/utils/get-html-render";
import type {CollectionName} from "@/content/config";
import type {Data} from "@/shared/utils/thecookies";
import {getEntry} from "astro:content";
import type {HomeEntry} from "@/content/sanity-home-collection";

interface Props {
    _id: string;
    collection: CollectionName;
    headingLevel?: TagTitle
}

const {  _id, headingLevel, collection = "home"  } = Astro.props;
const entry = await getEntry(collection, _id) as Data<HomeEntry>;

const data = entry.data.${lowerCamelName};
const copy = getHtmlSimpleCopy(data?.copy, headingLevel );

 ---

<section class={`o-${className}`}>
    <div class={`c-${className}`}>
        <h1>Hola! soy ${NAME},</h1>
        <div class={`${className}__copy`} set:html={copy}/>
        <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
</section>
