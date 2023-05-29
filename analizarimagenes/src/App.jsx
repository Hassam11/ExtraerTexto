import { useState } from "react";
import TableStrings from "./components/TableStrings";
import DescribeString from "./components/DescribeString";
import { uploadFile } from "./firebase";
import { Button, Image, Space } from "antd";
import { DownloadOutlined } from "@ant-design/icons";

function App() {
  const [file, setFile] = useState(null);
  const [link, setLink] = useState("");
  const [contenido, setContenido] = useState("");
  const [texto, setTexto] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await uploadFile(file);
      setLink(result);
    } catch (error) {
      console.log(error);
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api", {
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ link }),
      });

      if (response.ok) {
        const data = await response.json();
        setContenido(data["vision_result"]);
        setTexto(data["texto_result"]);
      } else {
        console.error("Error en la solicitud:", response.status);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <div className="mx-auto w-3/5 items-center text-center bg-slate-50">
        <div>
          <form className="items-center text-center flex flex-col">
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <Space size={12}>
              <Image
                width={400}
                src={link}
                placeholder={<Image preview={false} src={link} width={400} />}
              />
            </Space>
            <Button
              className="bg-slate-700 font-bold hover:bg-slate-800 text-white hover:text-white hover:border-white"
              icon={<DownloadOutlined />}
              type="primary"
              size={"large"}
              onClick={handleSubmit}
            >
              Enviar
            </Button>
          </form>
        </div>
        <div>
          <DescribeString contenido={contenido} />
          <TableStrings texto={texto} />
        </div>
      </div>
    </>
  );
}

export default App;
