---
import {getHtmlSimpleCopy} from "@/common/utils/get-html-render";

import type {TagTitle} from "@/common/utils/get-html-render";
import type { Data } from "@/common/astro";
import type { LandingPage } from "@/common/types";
import type { ${NAME} } from "@/common/sanity/sanity.types";

import { type CollectionKey, getEntry } from "astro:content";
import {getOptimizedImage} from "@/common/sanity/getOptimizedImage";


interface Props {
    _id: string;
    collection?: CollectionKey;
    headingLevel?: TagTitle
}

const {  _id, headingLevel, collection = "home"  } = Astro.props;
const entry = await getEntry(collection, _id) as Data<LandingPage & { ${lowerCamelName} : ${NAME} } >;

// const data = entry.data?.${lowerCamelName};
// const copy = getHtmlSimpleCopy(data?.copy, headingLevel );

// let optimizedImage;
// if (image) {
//     optimizedImage = getOptimizedImage(image).url();
// }

 ---

<section class={`o-${className}`}>
    <div class={`c-${className}`}>
        <h1>Hola! soy ${NAME},</h1>
        {/*<div class={`${className}__copy`} set:html={copy}/>*/}
        <pre>{JSON.stringify(entry, null, 2)}</pre>
    </div>
</section>
