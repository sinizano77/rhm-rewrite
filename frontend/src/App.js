// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        gameId: 0,
        gameName: "",
        groupId: 0,
        gamePlatform: "",
        pointMeter: false,
        skillStar: false,
        twoPlayer: false,
        imageFile: "",
        difficulty: 0.0
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/data").then(
          result => result.json().then(
            data => {
                // Attatching data received from api
                setdata({
                    gameId: data.game_id,
                    gameName: data.game_name,
                    groupId: data.group_id,
                    gamePlatform: data.game_platform,
                    pointMeter: data.point_meter,
                    skillStar: data.skill_star,
                    twoPlayer: data.two_player,
                    imageFile: data.image_file,
                    difficulty: data.difficulty,
                })
                console.log(data);
            })
        );
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>gameId: {data.gameId}</p>
                <p>gameName: {data.gameName}</p>
                <p>groupId: {data.groupId}</p>
                <p>gamePlatform: {data.gamePlatform}</p>
                <p>pointMeter: {data.pointMeter}</p>
                <p>skillStar: {data.skillStar}</p>
                <p>twoPlayer: {data.twoPlayer}</p>
                <p>imageFile: {data.imageFile}</p>
                <p>difficulty: {data.difficulty}</p>
 
            </header>
        </div>
    );
}
 
export default App;