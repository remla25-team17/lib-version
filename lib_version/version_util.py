import importlib.metadata

class VersionUtil:

    def get_version(package_name: str = "lib-version") -> str:
        try:
            return importlib.metadata.version(package_name)
        except ImportError:
            return "unknown"