import { BrowserRouter as Router, Route } from "react-router-dom"
import { Header } from "./components/Header"
import { Footer } from "./components/Footer"
import { LatestPairs } from "./components/LatestPairs"

function App() {
  return (
    <Router>
      <>
        <Header />
        <Route path="/latest" component={LatestPairs} />
        <Footer />
      </>
    </Router>
  );
}

export default App;
