---

import { getHtmlSimpleCopy } from "@/common/utils/get-html-render";
import { t,  getCurrentLanguage } from "@repo/i18n";

type Props = {
    data: unknown;
}

const { data } = Astro.props;

const language = getCurrentLanguage(Astro.currentLocale);


// const copy = getHtmlSimpleCopy(data.copy);

---

    <!--
     <div set:html={copy} />
    -->
<div className={`c-${className}`}>
  <div className={`m-${className}`}>
    <h2>Hola! soy ${NAME}, una molécula</h2>
    <p>
      Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
    </p>
    <pre>${FILE_NAME}</pre>
    <pre>{JSON.stringify(data, null, 2)}</pre>
    <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
  </div>
</div>

