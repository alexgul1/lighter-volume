#!/usr/bin/env python3
"""
Script to inspect nado-protocol SDK structure.
Run: pip install nado-protocol && python inspect_sdk.py > sdk_structure.txt
"""
import inspect
import sys

def print_module_structure(module, prefix="", max_depth=3, current_depth=0):
    """Recursively print module structure"""
    if current_depth >= max_depth:
        return

    for name in sorted(dir(module)):
        if name.startswith("_"):
            continue

        try:
            obj = getattr(module, name)
        except Exception:
            continue

        obj_type = type(obj).__name__

        if inspect.isclass(obj):
            print(f"{prefix}class {name}:")
            # Print methods
            for method_name in sorted(dir(obj)):
                if method_name.startswith("_"):
                    continue
                try:
                    method = getattr(obj, method_name)
                    if callable(method):
                        try:
                            sig = inspect.signature(method)
                            print(f"{prefix}  def {method_name}{sig}")
                        except (ValueError, TypeError):
                            print(f"{prefix}  def {method_name}(...)")
                except Exception:
                    pass

        elif inspect.isfunction(obj):
            try:
                sig = inspect.signature(obj)
                print(f"{prefix}def {name}{sig}")
            except (ValueError, TypeError):
                print(f"{prefix}def {name}(...)")

        elif inspect.ismodule(obj):
            print(f"{prefix}module {name}")

def main():
    print("=" * 60)
    print("NADO-PROTOCOL SDK STRUCTURE")
    print("=" * 60)
    print()

    try:
        import nado_protocol
        print(f"Package version: {getattr(nado_protocol, '__version__', 'unknown')}")
        print(f"Package location: {nado_protocol.__file__}")
        print()

        # List all submodules
        print("Top-level contents:")
        print("-" * 40)
        for name in sorted(dir(nado_protocol)):
            if not name.startswith("_"):
                obj = getattr(nado_protocol, name)
                print(f"  {name}: {type(obj).__name__}")
        print()

        # Try to import common submodules
        submodules = [
            "nado_protocol.client",
            "nado_protocol.engine",
            "nado_protocol.utils",
            "nado_protocol.utils.order",
            "nado_protocol.types",
            "nado_protocol.signing",
        ]

        for mod_name in submodules:
            print(f"\n{'=' * 60}")
            print(f"MODULE: {mod_name}")
            print("=" * 60)
            try:
                mod = __import__(mod_name, fromlist=[""])
                print_module_structure(mod, prefix="  ")
            except ImportError as e:
                print(f"  Not found: {e}")
            except Exception as e:
                print(f"  Error: {e}")

        # Show example usage if available
        print("\n" + "=" * 60)
        print("EXAMPLE USAGE (if documented)")
        print("=" * 60)

        # Try to find NadoClient or similar
        try:
            from nado_protocol import NadoClient
            print(f"\nNadoClient found!")
            print(f"Signature: {inspect.signature(NadoClient)}")
        except ImportError:
            pass

        try:
            from nado_protocol.client import NadoClient
            print(f"\nnado_protocol.client.NadoClient found!")
            print(f"Signature: {inspect.signature(NadoClient)}")
        except ImportError:
            pass

        try:
            from nado_protocol import create_client
            print(f"\ncreate_client found!")
            print(f"Signature: {inspect.signature(create_client)}")
        except ImportError:
            pass

    except ImportError as e:
        print(f"ERROR: nado-protocol not installed")
        print(f"Run: pip install nado-protocol")
        print(f"Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
