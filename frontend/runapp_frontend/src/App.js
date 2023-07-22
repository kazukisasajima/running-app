import {BrowserRouter, Routes, Route} from "react-router-dom";

import Calc from "./pages/user/Calc";
import Equivalent from "./pages/user/Equivalent";
import Training from "./pages/user/Training";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/Calc" element={<Calc/>} />
                <Route path="/Equivalent" element={<Equivalent/>} />
                <Route path="/Training" element={<Training/>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
