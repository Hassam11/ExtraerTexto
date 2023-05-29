import { Descriptions } from "antd";
import MyContext from "./Contexto";
import { useContext } from "react";

const DescribeString = ({contenido}) => {
  return (
      <div>
        <Descriptions title="Info Image">
          <Descriptions.Item label="Contenido">
            {contenido.Contenido}
          </Descriptions.Item>
          <Descriptions.Item label="Confianza">
            {contenido.Confianza}
          </Descriptions.Item>
        </Descriptions>
      </div>
  );
};

export default DescribeString;
