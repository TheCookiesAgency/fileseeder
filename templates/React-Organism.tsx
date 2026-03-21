---
import {getHtmlSimpleCopy} from "@/common/utils/get-html-render";
import { HeadingLevel } from "@repo/constants";
import type { Media, PropsComponentSection } from "@/common/types";
import { t, getCurrentLanguage } from "@repo/i18n";

import {getOptimizedImage} from "@/common/utils/getOptimizedImage";


type Props = PropsComponentSection;

const {  copy, mediaList, headingLevel  = HeadingLevel.P } = Astro.props;

const language = getCurrentLanguage(Astro.currentLocale);

const copy = getHtmlSimpleCopy(data?.copy, headingLevel );

// let optimizedImage;
// if (image) {
//     optimizedImage = getOptimizedImage(image).url();
// }

 ---

<section class={`o-${className}`}>
    <div class={`c-${className}`}>
        <h1>Hola! soy ${NAME},</h1>
        {/*<div class={`${className}__copy`} set:html={copy}/>*/}
        {/*<pre>{JSON.stringify(entry, null, 2)}</pre>*/}
    </div>
</section>
