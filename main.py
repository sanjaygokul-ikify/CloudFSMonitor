import argparse
import json
from src.cloud_storage import CloudStorage
from src.file_system_monitor import FileSystemMonitor
from src.notification_system import NotificationSystem

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='CloudFSMonitor')
    parser.add_argument('--config', type=str, help='Path to configuration file')
    args = parser.parse_args()

    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)

    # Initialize cloud storage, file system monitor, and notification system
    cloud_storage = CloudStorage(config['cloud_storage'])
    file_system_monitor = FileSystemMonitor(cloud_storage)
    notification_system = NotificationSystem(config['notification_system'])

    # Start monitoring and sending alerts
    file_system_monitor.start()
    notification_system.start()

if __name__ == '__main__':
    main()