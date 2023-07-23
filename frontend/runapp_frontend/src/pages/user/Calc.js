import React, { useState } from 'react';
import UserHeader from '../../components/Header/UserHeader'

const Calc = () => {
    const [distance, setDistance] = useState('');
    const [time, setTime] = useState('');
    const [vdot, setVDOT] = useState(null);
    const [paces, setPaces] = useState({});

    const calculateVDOT = () => {
        let calculatedVDOT = (distance / time) * 2100;  // Simplified VDOT formula
        setVDOT(calculatedVDOT);

        // Simplified pace calculations (use actual logic from the Daniels Running Formula)
        let dummyFactor = calculatedVDOT / 50;  // A dummy factor to simulate paces. Replace with actual logic.
        setPaces({
            '1km': {
                E: dummyFactor * 6,
                M: dummyFactor * 5.5,
                T: dummyFactor * 5,
                I: dummyFactor * 4.5,
                R: dummyFactor * 4
            },
            // Add similar entries for 1200m, 800m, etc.
        });
    };

  return (
    <div>
        <UserHeader pageTitle="計算式" />

        <div className="p-4">
                <div className="mb-4">
                    <label className="block text-sm font-bold mb-2">距離 (Km):</label>
                    <input type="number" value={distance} onChange={e => setDistance(e.target.value)} className="shadow appearance-none border rounded w-full py-2 px-3" />
                </div>
                
                <div className="mb-4">
                    <label className="block text-sm font-bold mb-2">時間 (分):</label>
                    <input type="number" value={time} onChange={e => setTime(e.target.value)} className="shadow appearance-none border rounded w-full py-2 px-3" />
                </div>
                
                <button onClick={calculateVDOT} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">計算</button>

                {vdot && (
                    <div className="mt-4">
                        <p>VDOT: {vdot}</p>
                        <p>1km Eペース: {paces['1km'].E} 分/km</p>
                        <p>1km Mペース: {paces['1km'].M} 分/km</p>
                        <p>1km Tペース: {paces['1km'].T} 分/km</p>
                        <p>1km Iペース: {paces['1km'].I} 分/km</p>
                        <p>1km Rペース: {paces['1km'].R} 分/km</p>
                        {/* ... Display similar entries for 1200m, 800m, etc. ... */}
                    </div>
                )}
            </div>
        
    </div>
  )
}

export default Calc