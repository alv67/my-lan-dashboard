from flask import Blueprint, request, jsonify
from backend.db.models import Device
from backend.utils.network import scan_network
from datetime import datetime

devices_bp = Blueprint('devices', __name__)

@devices_bp.route('/api/devices/scan', methods=['POST'])
def scan_devices():
    ip_range = request.json.get('ip_range', '192.168.1.0/24')
    devices = scan_network(ip_range)
    return jsonify(devices), 200

@devices_bp.route('/api/devices', methods=['GET'])
def get_devices():
    devices = Device.query.all()
    return jsonify([device.to_dict() for device in devices]), 200

@devices_bp.route('/api/devices', methods=['POST'])
def add_device():
    data = request.json
    new_device = Device(
        ip=data['ip'],
        mac=data['mac'],
        vendor=data.get('vendor', ''),
        hostname=data.get('hostname', ''),
        last_seen=datetime.now(),
        ip_type=data.get('ip_type', ''),
        connection_type=data.get('connection_type', ''),
        device_type=data.get('device_type', ''),
        last_ip=data.get('last_ip', '')
    )
    new_device.save()
    return jsonify(new_device.to_dict()), 201

@devices_bp.route('/api/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    device = Device.query.get_or_404(device_id)
    return jsonify(device.to_dict()), 200

@devices_bp.route('/api/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    device = Device.query.get_or_404(device_id)
    data = request.json
    device.ip = data.get('ip', device.ip)
    device.mac = data.get('mac', device.mac)
    device.vendor = data.get('vendor', device.vendor)
    device.hostname = data.get('hostname', device.hostname)
    device.last_seen = datetime.now()
    device.ip_type = data.get('ip_type', device.ip_type)
    device.connection_type = data.get('connection_type', device.connection_type)
    device.device_type = data.get('device_type', device.device_type)
    device.last_ip = data.get('last_ip', device.last_ip)
    device.save()
    return jsonify(device.to_dict()), 200

@devices_bp.route('/api/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    device = Device.query.get_or_404(device_id)
    device.delete()
    return jsonify({'message': 'Device deleted successfully'}), 204