---

import { getHtmlSimpleCopy } from "@/common/utils/get-html-render";

type Props = {
    data: unknown;
}

const { data } = Astro.props;

// const copy = getHtmlSimpleCopy(data.copy);

---

// <div set:html={copy} />

<div className={`m-${className}`}>
  <h2>Hola! soy ${NAME}, una molécula</h2>
  <p>
    Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
    <pre>${FILE_NAME}</pre>
    <pre>{JSON.stringify(data, null, 2)}</pre>
  </p>
  <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
</div>

