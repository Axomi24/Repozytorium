import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom';

function Shop() {

    useEffect(()=>{
        fetchCars();
    },[]);

    const [cars, setCars] = useState([]);

    const fetchCars=async()=>{
        const data = await fetch('http://127.0.0.1:8000/car/');
        const cars = await data.json();
        console.log(cars);
        setCars(cars);
    }

    return (
        <div>
            <div id="shop">
                <h1>Shop page</h1>
                {cars.map(car=>(
                    <h1 key={car.id}>
                        <Link to={`/shop/${car.id}`}>{car.name}</Link>
                    </h1>
                ))}
            </div>
            <div id="stage">
                <h1>Select a vehicle!</h1>
            </div>
        </div>
    );
}

export default Shop;
