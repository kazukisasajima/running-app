import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const UserHeader = ({ pageTitle }) => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const links = [
        { path: "/Calc", label: "計算式" },
        { path: "/Training", label: "トレーニング" },
        { path: "/Equivalent", label: "同等" },
    ];

    return (
        <div className="relative bg-blue-500 text-white p-5 flex justify-between items-center">
            <h1 className="text-2xl font-bold">{pageTitle}</h1>

            <div className="relative lg:hidden">
                <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="focus:outline-none">
                    <span className="text-2xl">{isMenuOpen ? '×' : '≡'}</span>
                </button>
            </div>

            <nav className={`lg:hidden absolute top-full right-0 w-48 bg-blue-500 shadow-lg border-t border-gray-700 ${isMenuOpen ? 'block' : 'hidden'}`}>
                {links.map((link, index) => (
                    <Link key={link.path} to={link.path} className={`block text-xl font-semibold py-3 px-4 hover:bg-blue-400 ${index !== links.length - 1 ? 'border-b border-gray-700' : ''}`}>
                        {link.label}
                    </Link>
                ))}
            </nav>

            <nav className="hidden lg:flex space-x-4">
                {links.map(link => (
                    <Link key={link.path} to={link.path} className="text-xl font-semibold py-2 px-4 hover:bg-blue-400">
                        {link.label}
                    </Link>
                ))}
            </nav>
        </div>
    )
}

export default UserHeader