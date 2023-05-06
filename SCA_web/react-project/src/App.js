import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import TestHome from "./pages/TestHome";
import Contact from "./pages/Contact";
import Result from "./pages/Result";
import TestResult from "./pages/TestResult";

export default function App(){
	return(
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/result/*" element={<Result />} />
				<Route path="/test/*" element={<TestHome />}/>
				<Route path="/test_result/*" element={<TestResult />} />
				<Route path="/contact/*" element={<Contact />} />
			</Routes>
		</BrowserRouter>
		
	)
	
}