import * as React from "react";
import { PropsWithChildren } from "react";
#if (${translation} != "")import { useTranslation } from "react-i18next";#end 

type Props${NAME} = PropsWithChildren<{
    element: string;
}>

const ${NAME}: React.FC<Props${NAME}> = (props: Props${NAME}) => {
#if (${translation} != "")  const { t } = useTranslation("${className}"); #end
  return (
    <div className={`m-${className}`}>
      <h2>Hola! soy ${NAME}, una molécula</h2>
      <p>
        Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
        <pre>${FILE_NAME}</pre>
      </p>
       #if (${translation} != "")<blockquote>{t("${className}.name")}</blockquote>#end
      <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
    </div>
  );
};

export default ${NAME};
