import React, { useEffect, useState } from 'react';
import { fetchDevices } from '../services/api';

const DeviceList = () => {
    const [devices, setDevices] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const getDevices = async () => {
            try {
                const data = await fetchDevices();
                setDevices(data);
            } catch (error) {
                console.error("Error fetching devices:", error);
            } finally {
                setLoading(false);
            }
        };

        getDevices();
    }, []);

    if (loading) {
        return <div>Loading devices...</div>;
    }

    return (
        <div>
            <h2>Device List</h2>
            <table>
                <thead>
                    <tr>
                        <th>IP Address</th>
                        <th>MAC Address</th>
                        <th>Hostname</th>
                        <th>Vendor</th>
                        <th>Last Seen</th>
                    </tr>
                </thead>
                <tbody>
                    {devices.map((device) => (
                        <tr key={device.mac}>
                            <td>{device.ip}</td>
                            <td>{device.mac}</td>
                            <td>{device.hostname}</td>
                            <td>{device.vendor}</td>
                            <td>{device.last_seen}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DeviceList;