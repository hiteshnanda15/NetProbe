import subprocess
import platform


def run_traceroute(hostname):

    system = platform.system()

    try:

        if system == "Darwin":
            # macOS
            command = [
                "traceroute",
                "-m", "15",
                "-q", "1",
                "-w", "2",
                hostname
            ]

        elif system == "Linux":
            # Linux
            command = [
                "traceroute",
                "-m", "15",
                "-q", "1",
                "-w", "2",
                hostname
            ]

        elif system == "Windows":
            # Windows
            command = [
                "tracert",
                "-h", "15",
                hostname
            ]

        else:

            return {
                "status": "ERROR",
                "output": "Unsupported operating system."
            }

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=40
        )

        if result.returncode == 0:

            return {
                "status": "SUCCESS",
                "output": result.stdout
            }

        else:

            return {
                "status": "ERROR",
                "output": result.stderr
            }

    except FileNotFoundError:

        return {
            "status": "ERROR",
            "output": (
                "Traceroute command is not installed "
                "or not available on this system."
            )
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "ERROR",
            "output": "Traceroute timed out."
        }

    except Exception as e:

        return {
            "status": "ERROR",
            "output": str(e)
        }