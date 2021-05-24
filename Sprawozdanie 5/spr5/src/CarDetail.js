import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom';

function CarDetail({match}) {

    useEffect(()=>{
        fetchCar();
    },[]);

    const [car, setCar] = useState([]);

    const fetchCar=async()=>{
        console.log(match.params.id);
        const data = await fetch(`http://127.0.0.1:8000/generic/car/${match.params.id}/`);
        const car = await data.json();
        setCar(car);
        console.log(car);
    }

    return (
        <div>
            <div>
                <h1>Shop page</h1>
            </div>
            <div id="stage">
                {car.name} {car.brand}
                <br/>
                color: {car.color}
                <br/>
                Number of doors: {car.door_number}
            </div>
        </div>
    );
}

export default CarDetail;
