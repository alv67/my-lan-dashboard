import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DeviceList from './components/DeviceList';
import DeviceForm from './components/DeviceForm';
import ScanButton from './components/ScanButton';

const App = () => {
    return (
        <Router>
            <div>
                <h1>My LAN Dashboard</h1>
                <ScanButton />
                <Switch>
                    <Route path="/devices" component={DeviceList} />
                    <Route path="/add-device" component={DeviceForm} />
                    <Route path="/" exact>
                        <h2>Welcome to My LAN Dashboard</h2>
                        <p>Use the navigation to scan your network and manage devices.</p>
                    </Route>
                </Switch>
            </div>
        </Router>
    );
};

export default App;