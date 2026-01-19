---

import { getHtmlSimpleCopy } from "@/common/utils/get-html-render";
import { t,  DEFAULT_LANGUAGE, type LANGUAGE } from "@repo/i18n";

type Props = {
    data: unknown;
    language: LANGUAGE
}

const { data, language = DEFAULT_LANGUAGE } = Astro.props;

// const copy = getHtmlSimpleCopy(data.copy);

---

  <!--
   <div set:html={copy} />
  -->

<div class={`m-${className}`}>
  <h2>Hola! soy ${NAME}, una molécula</h2>
  <p>
    Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
  </p>
    <pre>${FILE_NAME}</pre>
    <pre>{JSON.stringify(data, null, 2)}</pre>
  <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
</div>

