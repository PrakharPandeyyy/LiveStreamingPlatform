import ReactPlayer from "react-player";

export default function ReactPlay  ({url}) {
  return (
    <ReactPlayer
    url={url}
    controls={true}
    width="100%"
    height="100%"
  />
  )
}
