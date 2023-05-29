import { Divider, List } from "antd";

const TableStrings = ({texto}) => {
  return (  
    <div>
      <Divider orientation="center">Frases de la imagen</Divider>
      <List
        size="small"
        bordered={true}
        split={true}
        dataSource={texto}
        renderItem={(item) => (
          <List.Item className="text-xl font-medium">{item.content}</List.Item>
        )}
      />
    </div>
  );
};

export default TableStrings;
