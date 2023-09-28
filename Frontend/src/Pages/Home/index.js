import React from "react";
import Navbar from "../../components/Navbar";

import "./style.css";
import ReactPlay from "../../components/ReactPlayer/ReactPlayer";

export default function Home() {
  return (
    <div className="home_wrapper">
      <Navbar />
      <div className="home_content">
        <div className="searchbar">
          <form>
            <input type="text" placeholder="Search" />
          </form>
        </div>
        <div className="videoplayer_wrapper">
          <div className="video_player">
            <ReactPlay url="https://www.youtube.com/watch?v=PrYfOzRYwFc&ab_channel=7cloudsChill" />
          </div>
        </div>
      </div>
      <img
        className="img"
        src="https://img.freepik.com/free-photo/black-white-details-moon-texture-concept_23-2149535764.jpg?w=1800&t=st=1695835218~exp=1695835818~hmac=4a98fb16ca06bd6b8923cb8c84c2448098d144694d1e7fa3f9e366832ff415cd"
        alt="img"
      ></img>
    </div>
  );
}
