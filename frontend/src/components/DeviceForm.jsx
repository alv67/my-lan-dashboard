import React, { useState } from 'react';

const DeviceForm = ({ onSubmit }) => {
    const [ip, setIp] = useState('');
    const [mac, setMac] = useState('');
    const [vendor, setVendor] = useState('');
    const [hostname, setHostname] = useState('');
    const [lastSeen, setLastSeen] = useState('');
    const [connectionType, setConnectionType] = useState('');
    const [deviceType, setDeviceType] = useState('');
    const [ipReleaseType, setIpReleaseType] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const deviceData = {
            ip,
            mac,
            vendor,
            hostname,
            lastSeen,
            connectionType,
            deviceType,
            ipReleaseType,
        };
        onSubmit(deviceData);
        resetForm();
    };

    const resetForm = () => {
        setIp('');
        setMac('');
        setVendor('');
        setHostname('');
        setLastSeen('');
        setConnectionType('');
        setDeviceType('');
        setIpReleaseType('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>IP Address:</label>
                <input type="text" value={ip} onChange={(e) => setIp(e.target.value)} required />
            </div>
            <div>
                <label>MAC Address:</label>
                <input type="text" value={mac} onChange={(e) => setMac(e.target.value)} required />
            </div>
            <div>
                <label>Vendor:</label>
                <input type="text" value={vendor} onChange={(e) => setVendor(e.target.value)} />
            </div>
            <div>
                <label>Hostname:</label>
                <input type="text" value={hostname} onChange={(e) => setHostname(e.target.value)} />
            </div>
            <div>
                <label>Last Seen:</label>
                <input type="datetime-local" value={lastSeen} onChange={(e) => setLastSeen(e.target.value)} />
            </div>
            <div>
                <label>Connection Type:</label>
                <input type="text" value={connectionType} onChange={(e) => setConnectionType(e.target.value)} />
            </div>
            <div>
                <label>Device Type:</label>
                <input type="text" value={deviceType} onChange={(e) => setDeviceType(e.target.value)} />
            </div>
            <div>
                <label>IP Release Type:</label>
                <input type="text" value={ipReleaseType} onChange={(e) => setIpReleaseType(e.target.value)} />
            </div>
            <button type="submit">Add Device</button>
        </form>
    );
};

export default DeviceForm;